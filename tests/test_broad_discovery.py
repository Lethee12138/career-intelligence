"""v0.2.1 Pilot regressions for broad discovery and funnel boundaries."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from discovery_guard import discovery_coverage_errors
from search_execution import coverage_audit, intake_batch, route_pool

F = json.loads((ROOT / 'tests/fixtures/search-execution.json').read_text())
DATE = F['as_of']


def hypothesis(identifier, root, ai='NONE', axes=()):
    return {'id': identifier, 'role_or_family': identifier, 'why_generated': 'Grounded capability transfer',
            'actual_work_and_outputs': ['bounded reviewed work'], 'capability_root_refs': [root],
            'ai_involvement': ai, 'cross_domain_axes': list(axes), 'traditional_media_only': False}


def broad_report():
    roots = [{'id': 'product', 'category': 'PRODUCT', 'relevant': True},
             {'id': 'research', 'category': 'RESEARCH', 'relevant': True},
             {'id': 'transformation', 'category': 'TRANSFORMATION', 'relevant': True},
             {'id': 'media', 'category': 'MEDIA', 'relevant': True}]
    return {'ai_neutral_by_default': True, 'recent_evidence_ai_heavy': True,
            'capability_roots_considered': roots,
            'role_hypotheses': [hypothesis('Digital Product', 'product'),
                                hypothesis('Customer Research', 'research'),
                                hypothesis('Business Improvement', 'transformation', 'AI-ENABLED'),
                                hypothesis('Audience Product', 'media', 'NONE', ('MEDIA', 'AUDIENCE', 'DIGITAL'))]}


class BroadDiscoveryAndFunnel(unittest.TestCase):
    def test_A_ai_heavy_recent_evidence_retains_non_ai_roots(self):
        report = broad_report()
        self.assertEqual([], discovery_coverage_errors(report))
        for h in report['role_hypotheses']:
            h['ai_involvement'] = 'AI-CORE'
        self.assertIn('AI-heavy evidence narrowed discovery to AI roles', discovery_coverage_errors(report))

    def test_B_media_communication_produces_adjacent_crossing(self):
        report = broad_report()
        media = report['role_hypotheses'][-1]
        media.update(role_or_family='Content / Creator Product',
                     cross_domain_axes=['MEDIA', 'CONTENT', 'PRODUCT'])
        self.assertEqual([], discovery_coverage_errors(report))
        media.update(cross_domain_axes=['MEDIA'], traditional_media_only=True)
        self.assertIn('media/communication roots lack adjacent cross-domain hypothesis',
                      discovery_coverage_errors(report))

    def test_C_majority_concentration_is_result_bias_not_market_distribution(self):
        candidates = [
            {'role_family': 'Product', 'industry': 'Technology', 'company': 'OneCo',
             'employment_market': 'China', 'city': city, 'ai_involvement': 'AI-CORE',
             'discovery_source': ['https://one.example/jobs/' + city]}
            for city in ('Hangzhou', 'Shanghai', 'Shenzhen')]
        candidates.append({'role_family': 'Research', 'industry': 'Consumer', 'company': 'OtherCo',
                           'employment_market': 'UK', 'city': 'London', 'ai_involvement': 'NONE',
                           'discovery_source': ['https://other.example/job']})
        audit = coverage_audit(candidates, coverage_reviewed=True)
        self.assertEqual('COVERAGE_BIAS_DETECTED', audit['coverage_state'])
        self.assertTrue({'company', 'industry'}.issubset({b['axis'] for b in audit['biases']}))
        self.assertTrue(all(b['meaning'] == 'RESULT_SET_CONCENTRATION_ONLY' for b in audit['biases']))

    def test_D_three_targeted_do_not_shrink_discovery_or_fast_pool(self):
        intake = intake_batch(F['batch'], DATE, 'LIVE')
        routed = route_pool(intake, F['pool'], 3)
        self.assertEqual(3, routed['targeted_candidate_count'])
        self.assertGreaterEqual(routed['fast_lane_count'], 1)
        self.assertGreater(routed['opportunity_pool_count'], routed['targeted_candidate_count'])

    def test_E_targeted_wip_cap_only_limits_deep_preparation(self):
        intake = intake_batch(F['batch'], DATE, 'LIVE')
        routed = route_pool(intake, F['pool'], 2)
        self.assertEqual(2, routed['targeted_active_count'])
        self.assertGreater(routed['opportunity_pool_count'], 2)
        self.assertEqual('DEEP_ANALYSIS_AND_MATERIAL_PREPARATION_ONLY', routed['targeted_wip_applies_to'])

    def test_F_missing_candidate_context_forces_preliminary_no_active_or_fast(self):
        candidate = copy.deepcopy(F['batch']['candidates'][0])
        candidate['strongest_evidence_refs'] = 'UNKNOWN'
        candidate['screen'] = {}
        batch = {'batch_id': 'missing-context', 'candidate_context': {
                    'new_ssot': False, 'provenance': 'MISSING', 'as_of': DATE,
                    'scope': 'THIS_ROUTING_RUN_ONLY', 'evidence_refs': []},
                 'candidates': [candidate]}
        routed = route_pool(intake_batch(batch, DATE, 'LIVE'), {'entries': []})
        self.assertEqual('PRELIMINARY_CONTEXT_REQUIRED', routed['routing_state'])
        self.assertEqual((0, 0), (routed['targeted_active_count'], routed['fast_lane_count']))
        self.assertEqual('PRELIMINARY_CONTEXT_REQUIRED', routed['routes'][0]['queue_state'])
        self.assertIs(False, routed['candidate_context']['new_ssot'])

    def test_G_human_ai_evidence_cannot_bypass_agent_technical_must(self):
        candidate = copy.deepcopy(F['batch']['candidates'][0])
        candidate.update(ai_involvement='AGENT-CORE', technical_depth_requirement='ENGINEERING-CORE',
                         candidate_zone='CURRENTLY_TOO_FAR', strongest_capability_match='Human-AI workflow evidence')
        for review in ('qualification_review', 'work_right_review'):
            checks = candidate[review]['checks' if review == 'qualification_review' else 'qualification_checks']
            checks[0].update(result='FAIL', verified=True,
                             requirement='RAG, SQL, Python and architecture are mandatory')
        routed = route_pool(intake_batch({'candidates': [candidate]}, DATE, 'LIVE'), {'entries': []})
        self.assertEqual('SKIP', routed['routes'][0]['route'])
        self.assertEqual('ENGINEERING-CORE', routed['routes'][0]['technical_depth_requirement'])

    def test_H_better_non_ai_role_can_precede_ai_role(self):
        bad = next(copy.deepcopy(c) for c in F['batch']['candidates'] if c.get('company') == 'Synthetic bad')
        good = next(copy.deepcopy(c) for c in F['batch']['candidates'] if c.get('company') == 'Synthetic hz')
        bad.update(ai_involvement='AI-CORE', technical_depth_requirement='HIGH', candidate_zone='STRATEGIC_STRETCH')
        good.update(ai_involvement='NONE', technical_depth_requirement='LOW', candidate_zone='CORE_COMFORT')
        routed = route_pool(intake_batch({'candidates': [bad, good]}, DATE, 'LIVE'), {'entries': []})
        by_company = {r['company']: r for r in routed['routes']}
        self.assertEqual('WATCH_VERIFY', by_company['Synthetic bad']['route'])
        self.assertEqual('FAST_APPLY', by_company['Synthetic hz']['route'])
        self.assertIs(routed['ai_neutral_by_default'], True)

    def test_I_latest_batch_does_not_erase_existing_reviewed_role(self):
        current = copy.deepcopy(F['batch']['candidates'][0])
        old = copy.deepcopy(F['pool']['entries'][0])
        old.update(pool_id='OLD-HIGH', human_reviewed=True, lane='TARGETED', queue_state='WATCH')
        routed = route_pool(intake_batch({'candidates': [current]}, DATE, 'LIVE'),
                            {'entries': [old], 'company_constraints': {}})
        self.assertEqual(1, len(routed['existing_pool_continuity']))
        self.assertEqual('NEEDS_REVALIDATION', routed['existing_pool_continuity'][0]['continuity_state'])


if __name__ == '__main__':
    unittest.main()
