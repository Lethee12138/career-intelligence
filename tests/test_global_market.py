import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from global_market_guard import authorization_review, strategy_scope, market_identity_errors, comparison_errors, benefits_comparison_errors, scoped_city_preferences
from job_quality_guard import pay_basis_errors
D=json.loads((ROOT/'tests/fixtures/global-market-synthetic.json').read_text());C=D['cases'];DATE=D['as_of']

class GlobalMarketTests(unittest.TestCase):
    def test_A_foreign_company_in_China(self):
        j=C['CN-mnc'];self.assertEqual([],market_identity_errors(j))
        self.assertEqual('China',j['employment_market']);self.assertEqual('foreign multinational',j['company_type'])
        self.assertEqual('UNKNOWN',j['employer_sponsorship']['status'])

    def test_B_UK_unknown_sponsorship_stays_open_for_strategy(self):
        a=authorization_review(C['UK-verify'],DATE)
        self.assertEqual('SPONSORSHIP_REQUIRED',a['sponsorship_need']);self.assertEqual('SPONSORSHIP_VERIFY',a['resolution_state'])
        self.assertEqual('VERIFY',a['qualification']);self.assertFalse(a['market_exclusion'])
        self.assertTrue(strategy_scope(a,True).startswith('STRATEGY_ONLY'))

    def test_C_UK_unavailable_is_specific_job_failure(self):
        a=authorization_review(C['UK-unavailable'],DATE)
        self.assertEqual('SPONSORSHIP_UNAVAILABLE',a['resolution_state']);self.assertEqual('NOT ELIGIBLE',a['qualification'])
        self.assertEqual('STOP_FULL_MATERIALS',strategy_scope(a,True));self.assertFalse(a['market_exclusion'])

    def test_D_other_market_verified_sponsorship_normal_assessment(self):
        a=authorization_review(C['SG-available'],DATE)
        self.assertEqual('SPONSORSHIP_AVAILABLE',a['resolution_state']);self.assertEqual('ELIGIBLE',a['qualification'])
        self.assertEqual('NORMAL_CORE_GATES_REQUIRED',strategy_scope(a,True));self.assertEqual('NOT_ASSERTED',a['visa_issued'])

    def test_E_other_market_unknown_neither_pass_nor_fail(self):
        a=authorization_review(C['AU-verify'],DATE)
        self.assertEqual('SPONSORSHIP_VERIFY',a['resolution_state']);self.assertEqual('VERIFY',a['qualification'])

    def test_F_currency_conversion_is_not_quality_conclusion(self):
        for basis in ['FX_ONLY','NOMINAL_NUMBER']:
            self.assertTrue(comparison_errors({'conclusion_basis':basis,'asserts_financial_winner':True}))
        self.assertEqual([],comparison_errors({'asserts_financial_winner':False,'conclusion_basis':'CONTEXT_REVIEW_PENDING'}))
        self.assertTrue(comparison_errors({'asserts_financial_winner':True,'conclusion_basis':'CONTEXT','context':{}}))

    def test_G_benefit_labels_not_equivalent(self):
        a,b=D['benefit_examples']
        self.assertTrue(benefits_comparison_errors(a,b,equivalent_asserted=True))
        self.assertEqual([],benefits_comparison_errors(a,b,equivalent_asserted=False))

    def test_H_China_city_preference_does_not_become_global(self):
        self.assertTrue(scoped_city_preferences(D['city_preference'],'China'))
        for m in ['UK','Singapore','Germany','Australia','USA']:
            self.assertEqual([],scoped_city_preferences(D['city_preference'],m))

    def test_I_Chinese_company_London_is_UK_market(self):
        j=C['UK-verify'];self.assertEqual('UK',j['employment_market'])
        self.assertEqual('Chinese multinational',j['company_type']);self.assertEqual([],market_identity_errors(j))
        self.assertTrue(market_identity_errors({**j,'employment_market':'China'}))

    def test_J_visa_failure_does_not_mutate_candidate_or_hypothesis(self):
        j=copy.deepcopy(C['UK-unavailable']);j['capability_profile']={'workflow':'INFERRED'};before=copy.deepcopy(j)
        a=authorization_review(j,DATE)
        self.assertEqual(before,j);self.assertEqual('NONE',a['capability_effect']);self.assertEqual('HIGH',j['capability_fit'])

    def test_scope_date_and_source_mismatch_cannot_confirm_sponsor(self):
        for change in [{'role_key':'other-role'},{'market':'UK'},{'applicable_as_of':'2025-01-01'},{'refs':[]},{'authority_for_job':False}]:
            j=copy.deepcopy(C['SG-available']);j['employer_sponsorship'].update(change)
            self.assertEqual('VERIFY',authorization_review(j,DATE)['qualification'])

    def test_sponsor_available_does_not_prove_candidate_route_conditions(self):
        j=copy.deepcopy(C['SG-available']);j['employer_sponsorship']['candidate_route_conditions_verified']=False
        a=authorization_review(j,DATE);self.assertEqual('SPONSORSHIP_AVAILABLE',a['resolution_state']);self.assertEqual('VERIFY',a['qualification'])
        j['qualification_checks'][0]['result']='FAIL'
        self.assertEqual('NOT ELIGIBLE',authorization_review(j,DATE)['qualification'])

    def test_other_route_verify_and_existing_right_override_sponsor_need(self):
        j=copy.deepcopy(C['UK-unavailable']);j['other_route']['status']='POSSIBLE_UNVERIFIED'
        a=authorization_review(j,DATE);self.assertEqual('OTHER_ROUTE_VERIFY',a['resolution_state']);self.assertEqual('VERIFY',a['qualification'])
        j['candidate_authorization'].update(status='ALREADY_AUTHORISED',valid_for_role=True)
        a=authorization_review(j,DATE);self.assertEqual('ALREADY_AUTHORISED',a['resolution_state']);self.assertEqual('ELIGIBLE',a['qualification'])
        j['candidate_authorization']['valid_for_role']=False
        self.assertEqual('VERIFY',authorization_review(j,DATE)['qualification'])

    def test_international_currency_components_are_supported_without_FX_logic(self):
        for currency in ['RMB','CNY','GBP','SGD','EUR','AUD','USD','CAD']:
            self.assertEqual([],pay_basis_errors([{'currency':currency,'period':'YEAR','gross_net':'GROSS','included_in_guaranteed':True,'guaranteed':True,'obtainable':True,'refs':['SYN:pay']}]))
        self.assertTrue(pay_basis_errors([{'currency':'UNKNOWN','included_in_guaranteed':True}]))

    def test_unknown_candidate_rights_or_alternative_routes_cannot_fail_closed_as_no_route(self):
        j=copy.deepcopy(C['UK-unavailable']);j['candidate_authorization']['status']='UNKNOWN'
        self.assertEqual('VERIFY',authorization_review(j,DATE)['qualification'])
        j=copy.deepcopy(C['UK-unavailable']);j['other_route']['refs']=[]
        self.assertEqual('VERIFY',authorization_review(j,DATE)['qualification'])

if __name__=='__main__':unittest.main()
