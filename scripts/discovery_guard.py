"""Pure checks on manually grounded discovery inputs; not an inference engine.

No source I/O, semantic verification, search, profile mutation or recommendations.
"""
from copy import deepcopy
from guard import iso, known

STATUSES = {'SELF_IDENTIFIED', 'DEMONSTRATED', 'INFERRED', 'POTENTIAL'}
CONFIDENCE = {'STRONG', 'MODERATE', 'TENTATIVE'}


def capability_errors(capability, records):
    errors = []
    status = capability.get('epistemic_status')
    if status not in STATUSES:
        errors.append('invalid epistemic status')
    if capability.get('confidence') not in CONFIDENCE:
        errors.append('categorical confidence required')
    refs = capability.get('evidenceRefs', [])
    grounded = [records[r] for r in refs if r in records]
    if not refs or len(grounded) != len(refs):
        errors.append('unresolved evidence')
    if any(not r.get('source_ref') or not known(r.get('locator')) for r in grounded):
        errors.append('source trace missing')
    if status == 'POTENTIAL' and grounded and all(r.get('candidate_signal') is False for r in grounded):
        errors.append('no candidate-attributable weak signal')
    if status == 'SELF_IDENTIFIED' and not any(r.get('explicit_user_claim') is True for r in grounded):
        errors.append('explicit user claim required')
    if status == 'DEMONSTRATED' and not any(
        r.get('direct_verified') is True and r.get('supports_bounded_capability') is True
        for r in grounded
    ):
        errors.append('direct verified bounded evidence required')
    if status == 'INFERRED':
        usable = [r for r in grounded if r.get('behavior_reviewed') is True
                  and r.get('ownership') in {'CLEAR', 'PARTIAL'}
                  and known(r.get('ownership_boundary'))
                  and r.get('signal') == 'BEHAVIOR'
                  and known(r.get('context'))]
        distinct = {r['context'] for r in usable}
        strong_single = any(all(r.get(k) is True for k in
                                ('strong_single_reviewed', 'decision', 'execution', 'result'))
                            and r.get('ownership') == 'CLEAR' for r in usable)
        if not (len(distinct) >= 2 or strong_single):
            errors.append('insufficient distinct owned behavior')
        for field in ('repetition_signal', 'ownership_boundary', 'limitations', 'counterevidence'):
            if not known(capability.get(field)):
                errors.append('inference missing ' + field)
    return errors


def route_errors(route, bridge, capabilities, records):
    required = {'A': ('seed', 'support', 'counter', 'adjacent', 'contradiction_sought'),
                'B': ('capability_id', 'problem', 'team', 'role'),
                'C': ('capability_id', 'plausible_use', 'team', 'role'),
                'D': ('problem_pattern', 'problem_refs', 'teams', 'responsibilities', 'search_terms')}
    if route not in required:
        return ['unknown route']
    errors = ['missing bridge: ' + k for k in required[route] if not bridge.get(k)]
    if route in {'B', 'C'}:
        c = capabilities.get(bridge.get('capability_id'), {})
        allowed = {'SELF_IDENTIFIED', 'DEMONSTRATED'} if route == 'B' else {'INFERRED'}
        if c.get('epistemic_status') not in allowed:
            errors.append('capability status cannot enter route')
        errors.extend(capability_errors(c, records))
        if route == 'C' and c.get('ownership_strength') not in {'CLEAR', 'PARTIAL'}:
            errors.append('ownership insufficient')
    if route == 'D':
        refs = bridge.get('problem_refs', [])
        contexts = {records[r]['context'] for r in refs if r in records
                    and records[r].get('problem_reviewed') is True
                    and known(records[r].get('context'))}
        if len(contexts) < 2:
            errors.append('repeated problem trace required')
    return errors


def question_action(*, existing_reviewed, material, signal_history=(), repeated=False,
                    retrievable=True, jd_specific=False, relevant_jd=False):
    if not existing_reviewed:
        return 'READ_EXISTING'
    if (not material or repeated or not retrievable or (jd_specific and not relevant_jd)
            or list(signal_history[-2:]) == [False, False]):
        return 'STOP'
    return 'SELECTIVE' if signal_history else 'BROAD'


def mt_disposition(*, clear_function, low_sales_rotation_risk, high_career_value,
                   equal_direct_value=True, unusually_clear_fit=False):
    if not all(v is True for v in (clear_function, low_sales_rotation_risk, high_career_value)):
        return 'DEFER_MT'
    if equal_direct_value and unusually_clear_fit is not True:
        return 'PREFER_DIRECT_FUNCTION'
    return 'RETAIN_MT_FOR_REVIEW'


def market_update(hypothesis, observation, as_of):
    """Append a scoped observation; never promote a report to current authority.

    Caller supplies reviewed duty comparison. This does not decide eligibility.
    """
    result = deepcopy(hypothesis)
    o = deepcopy(observation)
    state = 'UNVALIDATED'
    dated = iso(o.get('observed_at'))
    day = iso(as_of)
    valid = (known(o.get('job_key')) and o.get('refs') and dated is not None
             and day is not None and dated <= day
             and o.get('source_kind') in {'ORIGINAL_JD', 'EXTERNAL_REPORT'}
             and o.get('duties_compared') is True)
    if valid:
        current = (o.get('source_kind') == 'ORIGINAL_JD'
                   and o.get('inspected_original') is True
                   and o.get('authority_for_job') is True and dated == day)
        o['validation_scope'] = 'CURRENT_JOB' if current else 'HISTORICAL_OR_REPORTED_JOB'
        if o.get('hard_mismatch') is True and known(o.get('mismatch_reason')):
            state = 'CONTRADICTED'
        elif current and o.get('duties_confirm') is True:
            state = 'VALIDATED_BY_CURRENT_JD'
        else:
            state = 'MARKET_SIGNAL_FOUND'
    else:
        o['validation_scope'] = 'INSUFFICIENT_MARKET_EVIDENCE'
    o['state'] = state
    result.setdefault('validation_history', []).append(o)
    # State is scoped to this observation, never a family-wide deletion.
    result['market_validation_state'] = state
    result['validation_job_key'] = o.get('job_key', 'UNKNOWN')
    result['recommendation'] = 'HYPOTHESIS_ONLY; /analyse-job required for job decision'
    return result
