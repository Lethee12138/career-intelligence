import copy
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from job_quality_guard import quality_review, hardship_review, pay_basis_errors
from guard import preparation_gate
D=json.loads((ROOT/'tests/fixtures/job-quality-synthetic.json').read_text())
O=D['offers']

class JobQualityTests(unittest.TestCase):
    def test_A_high_fit_bad_workload_downgrades_without_changing_capability(self):
        q=quality_review(O['A-pressure'])
        self.assertEqual('HIGH',q['capability_fit']);self.assertEqual('Low Priority',q['recommendation'])
        self.assertIn('PERFORMANCE_ENVIRONMENT_RISK',q['performance_environment_risks'])

    def test_B_pay_premium_does_not_erase_sustainability(self):
        self.assertGreater(O['A-pressure']['base_salary_rmb_month_gross'],O['B-sustainable']['base_salary_rmb_month_gross'])
        self.assertEqual('Low Priority',quality_review(O['A-pressure'])['recommendation'])
        self.assertEqual('Apply',quality_review(O['B-sustainable'])['recommendation'])
        for pay in [12000,15000,25000]:
            self.assertEqual('Low Priority',quality_review({**O['A-pressure'],'base_salary_rmb_month_gross':pay})['recommendation'])

    def test_C_good_environment_cannot_cure_confirmed_contextual_floor(self):
        self.assertEqual('Not Viable Currently',quality_review(O['C-low-floor'])['recommendation'])
        case=copy.deepcopy(O['C-low-floor']);case['observations'][0]['floor_context']['human_confirmed']=False
        q=quality_review(case);self.assertNotEqual('Not Viable Currently',q['recommendation']);self.assertTrue(q['verify_items'])

    def test_D_startup_label_not_a_gate(self):
        q=quality_review(O['E-startup-value']);self.assertEqual('Apply',q['recommendation'])
        for company in ['large established','mid-size','early-stage startup']:
            case=copy.deepcopy(O['E-startup-value']);case['context']['company_type']=company
            self.assertEqual(q,quality_review(case))

    def test_E_stability_alone_does_not_dominate_value(self):
        self.assertEqual('Low Priority',quality_review(O['D-stable-low-value'])['recommendation'])
        q=quality_review(O['E-startup-value'])
        self.assertEqual('Apply',q['recommendation']);self.assertTrue(q['tradeable'])

    def test_F_usable_leave_is_a_meaningful_preference(self):
        a,b=(quality_review(O[k]) for k in ['F-leave5','G-leave15'])
        self.assertFalse(a['positives']);self.assertEqual('STRONG_PREFERENCE',b['positives'][0]['strength'])
        case=copy.deepcopy(O['G-leave15']);case['observations'][0]['signal']='unusable_leave'
        self.assertEqual('Low Priority',quality_review(case)['recommendation'])

    def test_G_uncertain_bonus_never_becomes_guaranteed_comparison(self):
        self.assertEqual([],pay_basis_errors(D['pay_components']))
        components=copy.deepcopy(D['pay_components']);components[0]['included_in_guaranteed']=True
        self.assertTrue(pay_basis_errors(components))
        q=quality_review(O['H-bonus']);self.assertEqual('POSITIVE_BONUS',q['positives'][0]['strength'])
        self.assertEqual('STRONG_PREFERENCE',quality_review(O['I-base'])['positives'][0]['strength'])

    def test_H_normal_80_percent_vs_long_risky_probation(self):
        self.assertFalse(quality_review(O['J-probation-normal'])['concerns'])
        self.assertEqual('Low Priority',quality_review(O['K-probation-risk'])['recommendation'])
        self.assertEqual('UNKNOWN',O['K-probation-risk']['terms']['elimination_rate'])

    def test_I_hybrid_cannot_cancel_severe_concerns(self):
        case=copy.deepcopy(O['A-pressure'])
        case['observations']+=copy.deepcopy(O['C-low-floor']['observations'][2:])
        q=quality_review(case);self.assertEqual('Low Priority',q['recommendation'])
        self.assertTrue(any(p['signal']=='hybrid' for p in q['positives']))

    def test_J_brand_does_not_fill_unknown_culture(self):
        q=quality_review(O['L-brand-unknown'])
        self.assertIn('Team/Manager Environment',q['unknown_topics'])
        self.assertEqual('UNKNOWN',q['job_quality_fit']);self.assertFalse(q['performance_environment_risks'])

    def test_no_universal_salary_floor_or_upper_cap(self):
        for salary in [4500,5500,8500,9000,50000]:
            q=quality_review({**O['L-brand-unknown'],'base_salary_rmb_month_gross':salary})
            self.assertEqual('UNKNOWN',q['job_quality_fit']);self.assertEqual('Apply',q['recommendation'])

    def test_unreviewed_or_unreferenced_rumor_remains_verify(self):
        case=copy.deepcopy(O['A-pressure'])
        for o in case['observations']:o['reviewed']=False
        q=quality_review(case);self.assertFalse(q['concerns']);self.assertTrue(q['verify_items'])
        for o in case['observations']:o.update(reviewed=True,refs=[])
        self.assertFalse(quality_review(case)['concerns'])

    def test_hardship_requires_bounded_cost_duration_and_credible_return(self):
        self.assertEqual('INSUFFICIENT_JUSTIFICATION',hardship_review({'specific_return':'young people should suffer'}))
        p=dict(cost='two brief planned peaks',duration='two months',specific_return='own scoped product launch',return_refs=['SYN:project-plan'],mitigation='time off and manager support',review_or_exit_condition='review after first peak',return_credible_reviewed=True,cost_bounded_reviewed=True)
        self.assertTrue(hardship_review(p).startswith('HUMAN_TRADEOFF_REVIEW'))
        for k in ['cost','duration','return_refs','review_or_exit_condition']:
            self.assertEqual('INSUFFICIENT_JUSTIFICATION',hardship_review({**p,k:'UNKNOWN'}))

    def test_unknown_quality_alone_does_not_block_existing_preparation_gate(self):
        a=dict(role_key='SYN:ready',source_status={'role_key':'SYN:ready','status':'OPEN','live_verified':True,'refs':['SYN:authority']},qualification='ELIGIBLE',evidence_justifies_preparation=True,recommendation='Apply',critical_unknowns=[],one_active_application=False)
        a['job_quality']=quality_review(O['L-brand-unknown'])
        self.assertEqual('READY_FOR_REVIEW',preparation_gate(a)['gate'])
        a['qualification']='VERIFY';self.assertEqual('PREPARATION_HOLD',preparation_gate(a)['gate'])

    def test_known_bad_quality_never_promotes_existing_not_viable(self):
        case={**O['A-pressure'],'base_recommendation':'Not Viable Currently'}
        self.assertEqual('Not Viable Currently',quality_review(case)['recommendation'])
        case={**O['B-sustainable'],'base_recommendation':'Explore'}
        self.assertEqual('Explore',quality_review(case)['recommendation'])

if __name__=='__main__':unittest.main()
