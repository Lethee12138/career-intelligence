"""v0.2.2 synthetic UK work-right routing regressions."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from global_market_guard import authorization_review
from search_execution import intake_batch, route_pool

F = json.loads((ROOT / 'tests/fixtures/search-execution.json').read_text())
DATE = F['as_of']


def condition(role_key, status, applies_at='UNKNOWN'):
    return {'role_key': role_key, 'market': 'UK', 'reviewed': True,
            'refs': ['SYN:' + role_key + ':' + status], 'applicable_as_of': DATE,
            'status': status, 'applies_at': applies_at}


def current_right_candidate():
    candidate = next(copy.deepcopy(item) for item in F['batch']['candidates']
                     if item.get('employment_market') == 'UK')
    work = candidate['work_right_review']
    work['candidate_authorization'].update(
        status='ALREADY_AUTHORISED', valid_for_role=True,
        future_sponsorship_need='UNKNOWN', future_need_within_role='UNKNOWN',
        permanent_unrestricted_right=False)
    work['employer_sponsorship'].update(
        status='UNKNOWN', authority_for_job=False,
        sponsor_capability='UNKNOWN', candidate_route_conditions_verified=False)
    work['permanent_unrestricted_right_requirement'] = condition(candidate['role_key'], 'NO')
    work['explicit_no_sponsorship'] = condition(candidate['role_key'], 'NO')
    candidate['screen']['career_value'] = 'REASONABLE'
    candidate['screen']['application_cost'] = 'LOW'
    return candidate


def route(candidate):
    intake = intake_batch({'batch_id': 'SYN-UK-ROUTING', 'candidates': [candidate]}, DATE, 'LIVE')
    return intake['candidates'][0], route_pool(intake, {'entries': [], 'company_constraints': {}})['routes'][0]


class UKWorkRightRouting(unittest.TestCase):
    def test_current_right_pass_future_sponsorship_unknown_keeps_fast_ready(self):
        candidate, routed = route(current_right_candidate())
        self.assertEqual('ELIGIBLE', candidate['qualification_status'])
        self.assertEqual(('FAST_APPLY', 'FAST_READY'), (routed['route'], routed['readiness_state']))
        self.assertEqual({'LONG_TERM_IMMIGRATION_RISK', 'FUTURE_SPONSORSHIP_VERIFY'},
                         set(routed['work_right_risks']))

    def test_sponsor_licence_alone_is_not_exact_role_sponsorship(self):
        candidate = current_right_candidate()
        work = candidate['work_right_review']
        work['candidate_authorization'].update(status='NO_CURRENT_RIGHT', valid_for_role=False,
                                               future_sponsorship_need='REQUIRED')
        work['employer_sponsorship'].update(sponsor_capability='CONFIRMED', status='UNKNOWN',
                                            authority_for_job=False)
        reviewed = authorization_review(work, DATE)
        self.assertEqual('CONFIRMED', reviewed['employer_sponsor_capability'])
        self.assertEqual('UNKNOWN', reviewed['exact_role_sponsorship'])
        self.assertEqual('VERIFY', reviewed['qualification'])

    def test_permanent_unrestricted_right_hard_gate_still_blocks(self):
        candidate = current_right_candidate()
        work = candidate['work_right_review']
        work['permanent_unrestricted_right_requirement'] = condition(candidate['role_key'], 'YES', 'START_DATE')
        _, routed = route(candidate)
        self.assertEqual('SKIP', routed['route'])
        self.assertEqual('NOT_ELIGIBLE_PERMANENT_RIGHT_REQUIREMENT', routed['readiness_state'])

    def test_explicit_no_sponsorship_with_future_need_is_real_risk(self):
        candidate = current_right_candidate()
        work = candidate['work_right_review']
        work['candidate_authorization'].update(future_sponsorship_need='REQUIRED',
                                               future_need_within_role=True)
        work['explicit_no_sponsorship'] = condition(candidate['role_key'], 'YES')
        work['employer_sponsorship'].update(status='DOES_NOT', authority_for_job=True)
        reviewed, routed = route(candidate)
        self.assertEqual('NOT ELIGIBLE', reviewed['qualification_status'])
        self.assertEqual('SKIP', routed['route'])
        self.assertIn('LONG_TERM_ELIGIBILITY_RISK', routed['work_right_risks'])

    def test_unknown_current_work_right_remains_watch(self):
        candidate = current_right_candidate()
        candidate['work_right_review']['candidate_authorization'].update(status='UNKNOWN', valid_for_role=False)
        _, routed = route(candidate)
        self.assertEqual('WATCH_VERIFY', routed['route'])
        self.assertEqual('VERIFY_CURRENT_WORK_RIGHT', routed['next_human_action'])
        self.assertEqual('WATCH_VERIFY_CURRENT_WORK_RIGHT', routed['readiness_state'])

    def test_exact_role_sponsorship_does_not_override_other_hard_gate(self):
        candidate = current_right_candidate()
        work = candidate['work_right_review']
        work['candidate_authorization'].update(status='NO_CURRENT_RIGHT', valid_for_role=False,
                                               future_sponsorship_need='REQUIRED')
        work['employer_sponsorship'].update(status='OFFERS', authority_for_job=True,
                                            sponsor_capability='CONFIRMED',
                                            candidate_route_conditions_verified=True)
        candidate['qualification_review']['checks'][0].update(result='FAIL', verified=True)
        reviewed, routed = route(candidate)
        self.assertEqual('ROLE_SPONSORSHIP_CONFIRMED', reviewed['work_right']['routing_readiness'])
        self.assertEqual('NOT ELIGIBLE', reviewed['qualification_status'])
        self.assertEqual('SKIP', routed['route'])

    def test_uk_future_risk_does_not_spill_into_other_markets(self):
        candidate = current_right_candidate()
        candidate['employment_market'] = 'CHINA'
        candidate['country'] = 'CHINA'
        candidate['work_right_review']['employment_market'] = 'CHINA'
        for record in candidate['work_right_review'].values():
            if isinstance(record, dict) and record.get('market') == 'UK':
                record['market'] = 'CHINA'
        reviewed, routed = route(candidate)
        self.assertEqual([], reviewed['work_right']['risk_flags'])
        self.assertEqual('STANDARD_REVIEW', routed['work_right_readiness'])


if __name__ == '__main__':
    unittest.main()
