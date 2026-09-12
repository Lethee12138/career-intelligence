"""Structured boundary regressions. Semantic generation is reviewed separately."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from discovery_guard import capability_errors, route_errors, question_action, mt_disposition, market_update
from guard import work_style, qualification

CASE = json.loads((ROOT / 'tests/fixtures/slice2-cases.json').read_text())


def inferred(refs=('DNEG', 'Circular Flow')):
    return {'epistemic_status': 'INFERRED', 'confidence': 'MODERATE',
            'evidenceRefs': list(refs), 'repetition_signal': 'Research/framing to workflow decisions and tested prototype across distinct contexts',
            'ownership_strength': 'PARTIAL', 'ownership_boundary': 'Candidate product decisions; AI implementation and team research separated',
            'limitations': 'Historical secondary evidence; no production result',
            'counterevidence': 'Commercial analytics and complete event trace missing'}


class DiscoveryBoundaries(unittest.TestCase):
    def setUp(self):
        self.records = copy.deepcopy(CASE['projects'])

    def test_A_completed_outputs_do_not_become_direct_verified_capabilities(self):
        for name in self.records:
            c = inferred([name]); c['epistemic_status'] = 'DEMONSTRATED'
            self.assertIn('direct verified bounded evidence required', capability_errors(c, self.records))

    def test_B_repeated_owned_behavior_allows_bounded_inference(self):
        self.assertEqual([], capability_errors(inferred(), self.records))

    def test_B_one_tool_or_copied_context_cannot_establish_stable_capability(self):
        for signal in ('TOOL', 'COURSE', 'POLISHED_CV', 'AI_IMPLEMENTATION'):
            records = copy.deepcopy(self.records)
            for r in records.values(): r['signal'] = signal
            self.assertIn('insufficient distinct owned behavior', capability_errors(inferred(), records))
        self.records['Circular Flow']['context'] = 'DNEG'
        self.assertIn('insufficient distinct owned behavior', capability_errors(inferred(), self.records))

    def test_C_seed_bridge_requires_counter_and_alternative(self):
        bridge = dict(seed='PM', support=['DNEG'], counter=['Commercial analytics absent'],
                      adjacent=['Product discovery'], contradiction_sought='hard technical JD')
        self.assertEqual([], route_errors('A', bridge, {}, self.records))
        del bridge['counter']
        self.assertTrue(route_errors('A', bridge, {}, self.records))

    def test_D_degree_does_not_block_capability_but_hard_jd_gate_is_shared(self):
        c = inferred(); c['education'] = CASE['candidate']['education']
        self.assertEqual([], capability_errors(c, self.records))
        self.assertEqual('NOT ELIGIBLE', qualification([{'hierarchy':'MUST', 'result':'FAIL',
                         'verified':True, 'refs':['SYNTHETIC original JD major gate']}], True))

    def test_E_problem_route_accepts_non_media_teams_without_known_title(self):
        for teams in (['banking internal tools', 'manufacturing workflow'], ['retail services', 'public services']):
            b = dict(problem_pattern='workflow visibility', problem_refs=['DNEG','Circular Flow'],
                     teams=teams, responsibilities='make state and decisions visible', search_terms=['workflow', 'prototype'])
            self.assertEqual([], route_errors('D', b, {}, self.records))
        b['problem_refs'] = ['DNEG']
        self.assertTrue(route_errors('D', b, {}, self.records))

    def test_F_title_never_overrides_core_revenue_duties(self):
        for title in CASE['title_examples']:
            d = [{'title':title, 'signal':'revenue_ownership', 'core_daily':True}]
            self.assertEqual('LOW', work_style(d, [])['work_style'])

    def test_G_normal_collaboration_neutral_revenue_negative(self):
        for signal in CASE['candidate']['preferences']['neutral']:
            self.assertEqual('NO_NEGATIVE_SIGNAL', work_style([{'signal':signal,'core_daily':True}], [])['work_style'])
        for signal in CASE['candidate']['preferences']['avoid']:
            self.assertEqual('LOW', work_style([{'signal':signal,'core_daily':True}], [])['work_style'])

    def test_H_mt_needs_all_conditions_and_direct_function_wins_equal_value(self):
        args = dict(clear_function=True, low_sales_rotation_risk=True, high_career_value=True)
        self.assertEqual('PREFER_DIRECT_FUNCTION', mt_disposition(**args))
        self.assertEqual('RETAIN_MT_FOR_REVIEW', mt_disposition(**args, unusually_clear_fit=True))
        for key in args:
            self.assertEqual('DEFER_MT', mt_disposition(**{**args,key:'UNKNOWN'}))

    def test_I_weak_single_potential_not_inferred(self):
        c = inferred(['DNEG']); self.records['DNEG']['signal'] = 'TOOL'
        self.assertTrue(capability_errors(c, self.records))
        c['epistemic_status'] = 'POTENTIAL'; c['confidence'] = 'TENTATIVE'
        self.assertEqual([], capability_errors(c, self.records))

    def test_team_owned_result_is_not_candidate_potential(self):
        c = inferred(['AR Seedlings+']); c['epistemic_status'] = 'POTENTIAL'
        self.records['AR Seedlings+']['candidate_signal'] = False
        self.assertIn('no candidate-attributable weak signal', capability_errors(c, self.records))

    def test_J_real_reported_job_contradiction_retains_history_and_scope(self):
        h = {'role_or_family':'Applied AI Product','why_generated':'Owned product decisions',
             'market_validation_state':'UNVALIDATED','validation_history':[]}
        before = copy.deepcopy(h)
        result = market_update(h, CASE['market_observation'], CASE['as_of'])
        self.assertEqual(h, before)
        self.assertEqual('CONTRADICTED', result['market_validation_state'])
        self.assertEqual('HISTORICAL_OR_REPORTED_JOB', result['validation_history'][-1]['validation_scope'])
        self.assertEqual('Applied AI Product', result['role_or_family'])

    def test_current_jd_branch_is_explicitly_synthetic_control(self):
        o = {**CASE['market_observation'], 'job_key':'SYNTHETIC/current-positive',
             'refs':['SYNTHETIC JD'], 'observed_at':CASE['as_of'], 'source_kind':'ORIGINAL_JD',
             'inspected_original':True, 'authority_for_job':True, 'hard_mismatch':False, 'duties_confirm':True}
        self.assertEqual('VALIDATED_BY_CURRENT_JD', market_update({},o,CASE['as_of'])['market_validation_state'])
        for key, value in [('inspected_original',False),('authority_for_job',False),('observed_at','2026-09-10')]:
            self.assertEqual('MARKET_SIGNAL_FOUND', market_update({}, {**o,key:value},CASE['as_of'])['market_validation_state'])

    def test_taxonomy_future_and_untraced_observations_cannot_validate(self):
        for change in ({'source_kind':'TAXONOMY'}, {'observed_at':'2099-01-01'}, {'refs':[]}, {'job_key':'UNKNOWN'}, {'duties_compared':False}):
            r = market_update({}, {**CASE['market_observation'], **change}, CASE['as_of'])
            self.assertEqual('UNVALIDATED', r['market_validation_state'])

    def test_B_explicit_self_claim_keeps_its_status_and_needs_problem_team_bridge(self):
        c = inferred(['DNEG']); c['epistemic_status'] = 'SELF_IDENTIFIED'
        b = dict(capability_id='c',problem='ambiguous workflow',team='internal tools',role='product discovery')
        self.assertTrue(route_errors('B',b,{'c':c},self.records))
        self.records['DNEG']['explicit_user_claim'] = True
        self.assertEqual([], route_errors('B',b,{'c':c},self.records))
        del b['problem']; self.assertTrue(route_errors('B',b,{'c':c},self.records))
        self.assertEqual('SELF_IDENTIFIED', c['epistemic_status'])

    def test_C_hidden_route_rejects_unknown_ownership_and_potential(self):
        c = inferred(); b = dict(capability_id='c',plausible_use='workflow decisions',team='internal tools',role='product')
        self.assertEqual([], route_errors('C',b,{'c':c},self.records))
        c['ownership_strength'] = 'UNKNOWN'; self.assertTrue(route_errors('C',b,{'c':c},self.records))
        c['epistemic_status'] = 'POTENTIAL'; self.assertTrue(route_errors('C',b,{'c':c},self.records))

    def test_strong_single_exception_requires_all_owned_phases(self):
        c = inferred(['DNEG']); r = self.records['DNEG']
        r.update(ownership='CLEAR',strong_single_reviewed=True,decision=True,execution=True,result=True)
        self.assertEqual([], capability_errors(c,self.records))
        r['execution'] = False
        self.assertTrue(capability_errors(c,self.records))

    def test_no_numeric_confidence_or_missing_trace(self):
        c = inferred(); c['confidence'] = 0.9
        self.assertTrue(capability_errors(c,self.records))
        c = inferred(['missing']); self.assertTrue(capability_errors(c,self.records))
        c = inferred(); del c['limitations']; self.assertTrue(capability_errors(c,self.records))

    def test_question_existing_broad_selective_stop(self):
        self.assertEqual('READ_EXISTING',question_action(existing_reviewed=False,material=True))
        args = dict(existing_reviewed=True,material=True)
        self.assertEqual('BROAD',question_action(**args))
        self.assertEqual('SELECTIVE',question_action(**args,signal_history=[False,True]))
        self.assertEqual('STOP',question_action(**args,signal_history=[True,False,False]))
        for change in ({'repeated':True},{'retrievable':False},{'material':False},{'jd_specific':True}):
            self.assertEqual('STOP',question_action(**{**args,**change}))


if __name__ == '__main__': unittest.main()
