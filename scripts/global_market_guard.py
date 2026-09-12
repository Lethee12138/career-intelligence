"""Pure role-scoped market checks on reviewed inputs, not immigration advice.

No legal research, source verification, market estimates, capability mutation,
country exclusion, financial calculator or replacement of existing live gates.
"""
from guard import iso, qualification


def bound(record, job, as_of):
    day = iso(as_of)
    return (bool(job.get('role_key')) and job.get('role_key') != 'UNKNOWN'
            and bool(job.get('employment_market')) and job.get('employment_market') != 'UNKNOWN'
            and record.get('role_key') == job.get('role_key')
            and record.get('market') == job.get('employment_market')
            and record.get('reviewed') is True and bool(record.get('refs'))
            and record.get('applicable_as_of') == as_of and day is not None)


def authorization_review(job, as_of):
    c, s, other = (job.get(k, {}) for k in ('candidate_authorization', 'employer_sponsorship', 'other_route'))
    need, state, gate = 'UNKNOWN', 'SPONSORSHIP_VERIFY', 'VERIFY'
    reasons = []
    candidate_known = bound(c, job, as_of)
    sponsor_known = bound(s, job, as_of) and s.get('authority_for_job') is True
    if candidate_known and c.get('status') == 'ALREADY_AUTHORISED':
        if c.get('valid_for_role') is True:
            state, gate = 'ALREADY_AUTHORISED', 'ELIGIBLE'
            need = 'NOT_REQUIRED'
        else:
            reasons.append('authorization restrictions/applicability unresolved')
    elif candidate_known and c.get('status') == 'NO_CURRENT_RIGHT':
        need = 'SPONSORSHIP_REQUIRED'
        if sponsor_known and s.get('status') == 'OFFERS':
            state = 'SPONSORSHIP_AVAILABLE'
            if s.get('candidate_route_conditions_verified') is True:
                gate = 'ELIGIBLE'
            else:
                reasons.append('employer support is not candidate route eligibility')
        elif bound(other, job, as_of) and other.get('status') == 'POSSIBLE_UNVERIFIED':
            state = 'OTHER_ROUTE_VERIFY'
            reasons.append('alternative route requires verification')
        elif sponsor_known and s.get('status') == 'DOES_NOT':
            if bound(other, job, as_of) and other.get('status') == 'NO_OTHER_ROUTE':
                state, gate = 'SPONSORSHIP_UNAVAILABLE', 'NOT ELIGIBLE'
                reasons.append('exact job excludes sponsorship; no applicable candidate route')
            else:
                reasons.append('no sponsorship; other candidate routes unresolved')
        else:
            reasons.append('job-specific sponsorship unresolved')
    else:
        reasons.append('candidate current work rights unresolved')
    other_gate = qualification(job.get('qualification_checks', []), job.get('qualification_coverage_complete') is True)
    overall = ('NOT ELIGIBLE' if 'NOT ELIGIBLE' in (gate, other_gate)
               else 'ELIGIBLE' if gate == other_gate == 'ELIGIBLE' else 'VERIFY')
    return {'sponsorship_need': need, 'resolution_state': state, 'work_right_gate': gate,
            'other_qualification': other_gate, 'qualification': overall, 'reasons': reasons,
            'role_key': job.get('role_key', 'UNKNOWN'), 'scope': 'THIS_JOB_ONLY',
            'visa_issued': 'NOT_ASSERTED', 'capability_effect': 'NONE', 'market_exclusion': False}


def strategy_scope(review, worthwhile):
    if review['qualification'] == 'NOT ELIGIBLE':
        return 'STOP_FULL_MATERIALS'
    if review['qualification'] == 'VERIFY':
        return 'STRATEGY_ONLY; WORK_RIGHT_OR_QUALIFICATION_OPEN' if worthwhile else 'VERIFY_BEFORE_FURTHER_EFFORT'
    return 'NORMAL_CORE_GATES_REQUIRED'


def market_identity_errors(job):
    errors = []
    market = job.get('employment_market')
    country = job.get('work_location', {}).get('country')
    if not market or market == 'UNKNOWN':
        errors.append('employment jurisdiction unresolved')
    if not country or country == 'UNKNOWN':
        errors.append('work country unresolved')
    if market != country and job.get('cross_border_arrangement_reviewed') is not True:
        errors.append('market/location mismatch needs cross-border review')
    return errors


def comparison_errors(comparison):
    errors = []
    if comparison.get('conclusion_basis') in {'NOMINAL_NUMBER', 'FX_ONLY'}:
        errors.append('currency conversion is not an offer-quality conclusion')
    if comparison.get('asserts_financial_winner') is True:
        for field in ('pay_basis', 'taxes', 'living_rent_costs', 'benefits', 'hours',
                      'pension_social_insurance', 'relocation', 'visa_costs_constraints'):
            v = comparison.get('context', {}).get(field, {})
            if not v.get('refs') or v.get('reviewed') is not True or v.get('status') not in {'KNOWN', 'NOT_APPLICABLE'}:
                errors.append('comparison context unresolved: ' + field)
    return errors


def benefits_comparison_errors(a, b, equivalent_asserted=False):
    if not equivalent_asserted:
        return []
    fields = ('contribution', 'eligibility', 'access', 'local_treatment')
    if a.get('market') != b.get('market') and any(
        not x.get('refs') or not all(x.get(f) and x[f] != 'UNKNOWN' for f in fields) for x in (a, b)):
        return ['benefit labels are not equivalent across markets']
    return []


def scoped_city_preferences(preference, market):
    return list(preference.get('cities', [])) if preference.get('market') == market else []
