"""Synthetic structural behavior, not independent model/search validation."""
import copy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from search_execution import make_handoff, intake_batch, route_pool

F = json.loads((Path(__file__).parent / 'fixtures/search-execution.json').read_text())
DATE = F['as_of']


def run(batch=None, pool=None, limit=4, mode='LIVE'):
    i = intake_batch(batch or F['batch'], DATE, mode)
    return i, route_pool(i, F['pool'] if pool is None else pool, limit)


def route_of(routes, company):
    return next(r for r in routes['routes'] if r['company'] == company)


class ExecutionTests(unittest.TestCase):
    def test_A_two_sources_one_identity_preserve_provenance(self):
        i,_=run();c=next(c for c in i['candidates'] if len(c['raw_variants'])==2)
        self.assertEqual(['raw-sz','raw-sz-linkedin'],c['merged_from'])
        self.assertEqual(2,len(c['provenance']));self.assertEqual(11,i['candidate_count'])

    def test_B_similar_title_different_BG_city_not_merged(self):
        i,_=run();same=[c for c in i['candidates'] if c['company']=='Synthetic sz']
        self.assertEqual(2,len(same));self.assertEqual({'Shenzhen','Shanghai'},{c['city'] for c in same})

    def test_C_official_closed_beats_open_discovery(self):
        i,r=run();c=next(c for c in i['candidates'] if c['company']=='Synthetic closed')
        self.assertEqual('CLOSED',c['intake_state']);self.assertEqual('SKIP',route_of(r,c['company'])['route'])

    def test_D_nonpreferred_city_does_not_erase_value(self):
        _,r=run();self.assertEqual('TARGETED_PREPARE',route_of(r,'Synthetic sz')['route'])
        self.assertEqual('FAST_APPLY',route_of(r,'Synthetic hz')['route'])

    def test_E_UK_sponsor_unknown_not_skip(self):
        _,r=run();o=route_of(r,'Synthetic uk')
        self.assertEqual(('WATCH_VERIFY','VERIFY_SPONSORSHIP'),(o['route'],o['next_human_action']))

    def test_F_overseas_sponsor_available_normal(self):
        _,r=run();o=route_of(r,'Synthetic sg')
        self.assertEqual('TARGETED_PREPARE',o['route']);self.assertEqual('SPONSORSHIP_AVAILABLE',o['work_right_friction'])

    def test_G_quality_matters(self):
        _,r=run();o=route_of(r,'Synthetic bad')
        self.assertEqual('WATCH_VERIFY',o['route']);self.assertEqual('VERIFY_JOB_QUALITY',o['next_human_action'])
        self.assertEqual('LOW',o['job_quality']['job_quality_fit'])

    def test_H_unfamiliar_title_can_route_high(self):
        _,r=run();o=route_of(r,'Synthetic sz')
        self.assertEqual('Workflow Steward',o['role_title']);self.assertEqual('TARGETED_PREPARE',o['route'])

    def test_I_AI_title_wrong_duties(self):
        _,r=run();o=route_of(r,'Synthetic trap')
        self.assertEqual('SKIP',o['route']);self.assertIn('presales',o['priority_rationale'][0])

    def test_J_applied_duplicate_not_new_active(self):
        _,r=run();o=route_of(r,'Synthetic applied')
        self.assertEqual(('EXISTING_POOL','HOLD'),(o['queue_state'],o['next_human_action']))
        self.assertEqual('NOT_SET_BY_ROUTING',o['application_status'])

    def test_K_targeted_WIP_full_queues(self):
        pool=copy.deepcopy(F['pool']);pool['entries'] += [{'lane':'TARGETED','queue_state':'ACTIVE'}]*4
        _,r=run(pool=pool);o=route_of(r,'Synthetic sz')
        self.assertEqual('TARGETED_PREPARE',o['route']);self.assertEqual('QUEUED',o['queue_state'])
        self.assertEqual('HOLD',o['next_human_action'])

    def test_L_partial_salary_not_auto_skip(self):
        _,r=run();o=route_of(r,'Synthetic partial')
        self.assertEqual('FAST_APPLY',o['route']);self.assertEqual('PARTIAL',o['calibration_context']['traceability_status'])

    def test_handoff_axes_active_markets_bounds_no_private_pool(self):
        h=make_handoff(F['discovery'],'S',DATE,F['pool'])
        self.assertEqual({'title','responsibility','problem','output','negative'},{q['axis'] for q in h['query_sets']})
        self.assertEqual('ACTIVE',h['market_scope'][1]['status']);self.assertTrue(h['target_is_advisory'])
        self.assertNotIn('screen',h['existing_pool']['entries'][0]);self.assertFalse(h['external_action'])

    def test_missing_optional_inputs_and_no_hypothesis(self):
        h=make_handoff({},'S',DATE)
        self.assertEqual('READ_EXISTING_DISCOVERY',h['handoff_state']);self.assertEqual('UNKNOWN',h['existing_pool_coverage'])

    def test_nonmutating(self):
        before=copy.deepcopy(F);run();make_handoff(F['discovery'],'S',DATE,F['pool']);self.assertEqual(before,F)

    def test_stale_authority_cannot_route_active(self):
        _,r=run(mode='HISTORICAL_SNAPSHOT')
        self.assertFalse(any(o['queue_state']=='ACTIVE' for o in r['routes']))
        b=copy.deepcopy(F['batch']);b['candidates'][0]['observations'][0]['observed_at']='2025-01-01'
        _,r=run(batch=b);self.assertEqual('WATCH_VERIFY',route_of(r,'Synthetic sz')['route'])

    def test_conflicting_official_ID_shared_URL_not_merged_or_active(self):
        a=copy.deepcopy(F['batch']['candidates'][0]);b=copy.deepcopy(a);b['identity']['official_job_id']='OTHER'
        i,r=run(batch={'batch_id':'collision','candidates':[a,b]})
        self.assertEqual(2,i['candidate_count']);self.assertEqual(2,len({c['candidate_id'] for c in i['candidates']}))
        self.assertTrue(all(o['route']=='WATCH_VERIFY' for o in r['routes']))

    def test_conflicting_authority_payload_not_selected_silently(self):
        a=copy.deepcopy(F['batch']['candidates'][0]);b=copy.deepcopy(a);b['requirements']=['different']
        i,r=run(batch={'candidates':[a,b]});self.assertEqual(1,i['candidate_count'])
        self.assertEqual('WATCH_VERIFY',r['routes'][0]['route'])

    def test_malformed_and_weak_stay_discovered(self):
        i,r=run(batch={'candidates':[{'company':{},'identity':[],'screen':'bad','observations':'bad'},42]})
        self.assertTrue(all(c['intake_state']=='DISCOVERED' for c in i['candidates']))
        self.assertTrue(all(o['route']=='WATCH_VERIFY' for o in r['routes']))

    def test_wrong_role_qualification_or_authority_cannot_pass(self):
        for field in ['qualification_review','observations']:
            a=copy.deepcopy(F['batch']['candidates'][0])
            if field=='observations':a[field][0]['role_key']='wrong'
            else:a[field]['role_key']='wrong'
            _,r=run(batch={'candidates':[a]});self.assertEqual('WATCH_VERIFY',r['routes'][0]['route'])

    def test_defensible_stretch_remains_usable(self):
        a=copy.deepcopy(F['batch']['candidates'][0]);a['screen']['responsibility_match']='DEFENSIBLE_STRETCH'
        _,r=run(batch={'candidates':[a]});self.assertEqual('TARGETED_PREPARE',r['routes'][0]['route'])

    def test_company_constraint_and_future_dates(self):
        pool={'entries':[],'company_constraints':{'Synthetic sz':'FULL'}}
        _,r=run(pool=pool);self.assertEqual('HOLD',route_of(r,'Synthetic sz')['next_human_action'])
        a=copy.deepcopy(F['batch']['candidates'][0]);a['source_capture_date']='2030-01-01'
        _,r=run(batch={'candidates':[a]});self.assertEqual('WATCH_VERIFY',r['routes'][0]['route'])

    def test_calibration_only_quality_signal_cannot_downgrade(self):
        a=copy.deepcopy(F['batch']['candidates'][0]);a['screen']['quality_observations']=[{
            'basis':'DATED_CALIBRATION','signal':'low_pay_context','reviewed':True,'refs':['calibration'],
            'source_scope':'SCOPED_EVIDENCE','rationale':'old directional salary'}]
        _,r=run(batch={'candidates':[a]});self.assertEqual('TARGETED_PREPARE',r['routes'][0]['route'])

    def test_E2E_two_lanes_existing_guards_and_lineage(self):
        from run_search_execution_fixture import run_fixture
        result=run_fixture()
        self.assertEqual(2,result['selected_deep_analysis_count'])
        self.assertEqual({'TARGETED','FAST'},{c['lane'] for c in result['chains']})
        for c in result['chains']:
            self.assertEqual(c['analysis']['id'],c['brief']['analysis_ref'])
            self.assertEqual(c['analysis']['role_key'],c['brief']['role_key'])
            self.assertEqual('READY_FOR_REVIEW',c['brief']['gate'])
            self.assertEqual('PREPARATION_HOLD',c['checks']['historical_control_gate']['gate'])
            self.assertEqual('PARTIAL',c['analysis']['matches'][1]['match_level'])
        self.assertFalse(result['external_search_performed'])

    def test_active_market_query_gap_not_silently_China_only(self):
        d=copy.deepcopy(F['discovery'])
        for h in d['role_hypotheses']:h['search_terms'].pop('UK')
        h=make_handoff(d,'S',DATE)
        self.assertIn('UK',h['coverage_gaps'])
        self.assertEqual('EXPAND_ACTIVE_MARKET_QUERIES',h['handoff_state'])

    def test_order_independent_strongest_identity(self):
        a=copy.deepcopy(F['batch']['candidates'][0]);b=copy.deepcopy(a)
        b['identity'].pop('official_job_id');b['observations']=[]
        i,_=run(batch={'candidates':[a,b]});j,_=run(batch={'candidates':[b,a]})
        self.assertEqual(i['candidates'][0]['candidate_id'],j['candidates'][0]['candidate_id'])

    def test_normalized_candidate_can_be_pool_snapshot(self):
        i,_=run(batch={'candidates':[F['batch']['candidates'][0]]})
        entry=copy.deepcopy(i['candidates'][0]);entry['application_status']='APPLIED'
        r=route_pool(i,{'entries':[entry]})
        self.assertEqual('EXISTING_POOL',r['routes'][0]['queue_state'])

    def test_same_URL_newer_authority_payload_beats_old_snapshot(self):
        current=copy.deepcopy(F['batch']['candidates'][0]);old=copy.deepcopy(current)
        old['observations'][0].update(observed_at='2026-09-12',status='CLOSED')
        old['responsibilities']=['Old different duties'];old['screen']['as_of']='2026-09-12'
        old['qualification_review']['as_of']='2026-09-12'
        i,r=run(batch={'candidates':[old,current]})
        self.assertEqual('SCREEN_READY',i['candidates'][0]['intake_state'])
        self.assertEqual(current['responsibilities'],i['candidates'][0]['responsibilities'])
        self.assertEqual('TARGETED_PREPARE',r['routes'][0]['route'])

if __name__=='__main__':unittest.main()
