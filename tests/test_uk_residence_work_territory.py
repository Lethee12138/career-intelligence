"""v0.2.3 synthetic UK residence/work-territory regressions."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from global_market_guard import authorization_review
from guard import preparation_gate
from search_execution import route_pool, intake_batch, make_handoff
from test_uk_work_right_routing import current_right_candidate


DATE = '2026-09-13'


def reviewed(role_key, field, status, country=None):
    record = {'role_key': role_key, 'market': 'UK', 'reviewed': True,
              'refs': [f'SYN:{role_key}:{field}:{status}'],
              'applicable_as_of': DATE, 'status': status}
    if country is not None:
        record['country'] = country
    return record


def territory_candidate():
    candidate = current_right_candidate()
    candidate['hybrid'] = 'Home Based'
    role_key = candidate['role_key']
    work = candidate['work_right_review']
    work.update(
        current_residence=reviewed(role_key, 'residence', 'OUTSIDE_UK', 'China'),
        required_work_territory=reviewed(role_key, 'territory', 'UK_ONLY', 'UK'),
        residence_requirement=reviewed(role_key, 'residence_requirement',
                                       'MUST_BE_UK_BASED_BY_START_DATE'),
        overseas_remote_allowed=reviewed(role_key, 'overseas_remote', 'NO'),
        relocation_before_start=reviewed(role_key, 'relocation', 'UNKNOWN'),
    )
    return candidate


def route(candidate):
    intake = intake_batch({'batch_id': 'SYN-UK-TERRITORY', 'candidates': [candidate]}, DATE, 'LIVE')
    routed = route_pool(intake, {'entries': [], 'company_constraints': {}})
    return intake['candidates'][0], routed['routes'][0]


class UKResidenceWorkTerritory(unittest.TestCase):
    def test_home_based_with_uk_authority_is_not_global_remote(self):
        candidate = territory_candidate()
        reviewed_work = authorization_review(candidate['work_right_review'], DATE)
        self.assertEqual('UK_ONLY', reviewed_work['required_work_territory'])
        self.assertEqual('NO', reviewed_work['overseas_remote_allowed'])
        self.assertNotEqual('GLOBAL_REMOTE', reviewed_work['required_work_territory'])
        self.assertEqual('RELOCATION_OR_START_LOCATION_VERIFY', reviewed_work['territory_readiness'])

    def test_outside_uk_start_requirement_with_unknown_relocation_watches(self):
        candidate, routed = route(territory_candidate())
        self.assertEqual('PASS', candidate['work_right']['current_work_right'])
        self.assertEqual('VERIFY', candidate['work_right']['work_right_at_required_location_and_start_date'])
        self.assertEqual('VERIFY', candidate['qualification_status'])
        self.assertEqual(('WATCH_VERIFY', 'VERIFY_RELOCATION_OR_START_LOCATION'),
                         (routed['route'], routed['next_human_action']))

    def test_outside_uk_possible_relocation_still_verifies_start_location(self):
        candidate = territory_candidate()
        candidate['work_right_review']['relocation_before_start'] = reviewed(
            candidate['role_key'], 'relocation', 'CONFIRMED_POSSIBLE')
        reviewed_candidate, routed = route(candidate)
        self.assertEqual('PASS', reviewed_candidate['work_right']['work_right_at_required_location_and_start_date'])
        self.assertEqual('RELOCATION_OR_START_LOCATION_VERIFY', reviewed_candidate['work_right']['territory_readiness'])
        self.assertEqual(('WATCH_VERIFY', 'VERIFY_RELOCATION_OR_START_LOCATION'),
                         (routed['route'], routed['next_human_action']))

    def test_outside_uk_and_cannot_relocate_is_not_viable_currently(self):
        candidate = territory_candidate()
        candidate['work_right_review']['relocation_before_start'] = reviewed(
            candidate['role_key'], 'relocation', 'CONFIRMED_NOT_POSSIBLE')
        reviewed_candidate, routed = route(candidate)
        self.assertEqual('FAIL', reviewed_candidate['work_right']['work_right_at_required_location_and_start_date'])
        self.assertEqual('NOT_VIABLE_CURRENTLY', reviewed_candidate['work_right']['territory_status'])
        self.assertEqual('NOT ELIGIBLE', reviewed_candidate['qualification_status'])
        self.assertEqual(('SKIP', 'NOT_VIABLE_CURRENTLY'),
                         (routed['route'], routed['readiness_state']))

    def test_no_sponsorship_and_future_need_remain_long_term_risk(self):
        candidate = territory_candidate()
        work = candidate['work_right_review']
        work['relocation_before_start'] = reviewed(candidate['role_key'], 'relocation', 'CONFIRMED_POSSIBLE')
        work['candidate_authorization'].update(future_sponsorship_need='REQUIRED',
                                               future_need_within_role=False)
        work['explicit_no_sponsorship'] = reviewed(candidate['role_key'], 'no_sponsorship', 'YES')
        work['employer_sponsorship'].update(status='DOES_NOT', authority_for_job=True)
        reviewed_candidate, routed = route(candidate)
        self.assertIn('LONG_TERM_ELIGIBILITY_RISK', reviewed_candidate['work_right']['risk_flags'])
        self.assertEqual('VERIFY', reviewed_candidate['qualification_status'])
        self.assertEqual('WATCH_VERIFY', routed['route'])

    def test_explicit_global_remote_does_not_impose_uk_residence(self):
        candidate = territory_candidate()
        work = candidate['work_right_review']
        work['required_work_territory'] = reviewed(candidate['role_key'], 'territory', 'GLOBAL_REMOTE')
        work['residence_requirement'] = reviewed(candidate['role_key'], 'residence_requirement',
                                                 'NO_SPECIFIC_RESIDENCE_REQUIREMENT')
        work['overseas_remote_allowed'] = reviewed(candidate['role_key'], 'overseas_remote', 'YES')
        reviewed_candidate, routed = route(candidate)
        self.assertEqual('PASS', reviewed_candidate['work_right']['territory_status'])
        self.assertEqual('GLOBAL_REMOTE_ALLOWED', reviewed_candidate['work_right']['territory_readiness'])
        self.assertEqual([], reviewed_candidate['work_right']['territory_risks'])
        self.assertNotEqual('VERIFY_RELOCATION_OR_START_LOCATION', routed['next_human_action'])

    def test_current_work_right_pass_does_not_override_territory_gate(self):
        candidate = territory_candidate()
        reviewed_candidate, routed = route(candidate)
        self.assertEqual('PASS', reviewed_candidate['work_right']['current_work_right'])
        self.assertEqual('VERIFY', reviewed_candidate['work_right']['territory_gate'])
        self.assertEqual('WATCH_VERIFY', routed['route'])

    def test_territory_failure_keeps_capability_and_evidence_history(self):
        candidate = territory_candidate()
        before = copy.deepcopy(candidate['screen']['dimensions'])
        reviewed_candidate, _ = route(candidate)
        self.assertEqual(before, reviewed_candidate['screen']['dimensions'])
        self.assertEqual('REVIEWED_SYNTHETIC', reviewed_candidate['screen']['dimensions']['Capability Fit']['judgment'])
        self.assertEqual('REVIEWED_SYNTHETIC', reviewed_candidate['screen']['dimensions']['Evidence Fit']['judgment'])

    def test_prepare_holds_material_territory_unknown_until_human_accepts(self):
        analysis = {
            'role_key': 'SYN:territory',
            'qualification': 'ELIGIBLE',
            'source_status': {'role_key': 'SYN:territory', 'status': 'OPEN',
                              'live_verified': True, 'refs': ['SYN:authority']},
            'evidence_justifies_preparation': True,
            'recommendation': 'Apply', 'critical_unknowns': [],
            'one_active_application': False,
            'work_territory': {'territory_material': True, 'territory_gate': 'VERIFY',
                               'territory_readiness': 'RELOCATION_OR_START_LOCATION_VERIFY'},
        }
        self.assertEqual('PREPARATION_HOLD', preparation_gate(analysis)['gate'])
        analysis['human_accepts_territory_uncertainty'] = True
        self.assertEqual('READY_FOR_REVIEW', preparation_gate(analysis)['gate'])

    def test_find_jobs_handoff_requires_territory_fields(self):
        handoff = make_handoff({}, 'SYN-TERRITORY-HANDOFF', DATE)
        self.assertEqual('0.2.4', handoff['schema_version'])
        self.assertTrue({'work_right_review.current_residence',
                         'work_right_review.required_work_territory',
                         'work_right_review.residence_requirement',
                         'work_right_review.overseas_remote_allowed',
                         'work_right_review.relocation_before_start',
                         'work_right_review.work_right_at_required_location_and_start_date'}
                        .issubset(set(handoff['candidate_fields_required'])))


if __name__ == '__main__':
    unittest.main()
