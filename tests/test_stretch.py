"""Focused Core integration checks and counterfactuals; no old fixture changes."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from stretch_guard import stretch_errors, fact_atom_errors, stretch_match_errors, trace_errors, HARD
from guard import preparation_gate
D=json.loads((ROOT/'tests/outputs/core-integration-trace.json').read_text())
E=json.loads((ROOT/'tests/fixtures/evidence-excerpts.json').read_text())['evidence']

class CoreStretch(unittest.TestCase):
    def setUp(self):
        self.c=copy.deepcopy(D['claims']['S-AI'])

    def test_A_tool_only_has_no_explainable_engineering_bridge(self):
        self.c.update(bridge_reasoning='UNKNOWN',adjacency_reviewed=False)
        self.assertTrue(stretch_errors(self.c,set(E)))
        self.c.update(use_boundary='SPECULATIVE_UNSUPPORTED',allowed_use=[])
        self.assertEqual([],stretch_errors(self.c,set(E)))

    def test_B_adjacent_product_potential_needs_no_formal_PM_title(self):
        self.assertNotIn('official_title',self.c)
        self.assertEqual([],stretch_errors(self.c,set(E)))
        self.assertEqual('INFERRED',D['nodes']['C-pattern']['epistemic_status'])
        self.assertEqual('POTENTIAL',D['nodes']['C-stretch']['target_epistemic_status'])

    def test_C_metric_aggregate_cannot_become_percent_improvement(self):
        s=D['source_atoms']; atom={'source_id':'changes',**s['changes']}
        self.assertEqual([],fact_atom_errors([atom],s))
        for value in ['30% usability improvement','50% faster workflow','9 participants']:
            self.assertTrue(fact_atom_errors([{**atom,'value':value}],s))

    def test_D_independent_prototype_not_whole_project_leadership(self):
        s=D['source_atoms'];atom={'source_id':'ownership',**s['ownership']}
        self.assertEqual([],fact_atom_errors([atom],s))
        self.assertTrue(fact_atom_errors([{**atom,'value':'independently led entire project'}],s))
        self.assertTrue(fact_atom_errors([{**atom,'scope':'Entire project'}],s))

    def test_E_AI_workflow_does_not_supply_stack_usage(self):
        for stack in ['ML model development','RAG implementation','backend engineering']:
            self.assertTrue(fact_atom_errors([{'source_id':'unknown','type':'technical_stack','value':stack,'scope':'candidate implementation'}],D['source_atoms']))
        self.assertEqual([],stretch_errors(self.c,set(E)))

    def test_F_bridge_gives_PARTIAL_not_SUPPORTED_or_automatic_UNSUPPORTED(self):
        c=D['claims']['S-evaluation'];row=D['stage_sequence'][2]['requirements'][1]
        self.assertEqual([],stretch_match_errors(row,c,E))
        for level in ['SUPPORTED','UNSUPPORTED']:
            self.assertTrue(stretch_match_errors({**row,'match_level':level},c,E))
        no_bridge={**c,'use_boundary':'SPECULATIVE_UNSUPPORTED','allowed_use':[]}
        self.assertEqual([],stretch_match_errors({**row,'match_level':'UNSUPPORTED'},no_bridge,E))
        self.assertTrue(stretch_match_errors(row,no_bridge,E))

    def test_L1_L2_L3_are_internal_quality_gates(self):
        for level in ['L1','L2','L3']:
            c=copy.deepcopy(self.c);c['defensibility'][level]='UNKNOWN'
            self.assertTrue(stretch_errors(c,set(E)))
        self.c['defensibility']['reviewed']=False
        self.assertTrue(stretch_errors(self.c,set(E)))

    def test_contradiction_ownership_and_credentials_are_not_majority_votes(self):
        for k,v in [('direct_counterevidence',True),('ownership_reviewed',False),('invents_credential',True),('direct_counterevidence','UNKNOWN')]:
            self.assertTrue(stretch_errors({**self.c,k:v},set(E)))

    def test_all_hard_fact_types_reject_value_or_scope_expansion(self):
        for kind in HARD:
            sources={'x':{'type':kind,'value':'bounded original','scope':'original scope'}}
            a={'source_id':'x',**sources['x']}
            self.assertEqual([],fact_atom_errors([a],sources))
            for change in [{'value':'expanded'},{'scope':'broader'}]:
                self.assertTrue(fact_atom_errors([{**a,**change}],sources))

    def test_five_trace_chains_and_lost_edge_detection(self):
        for chain in D['trace_chains'].values():
            self.assertEqual([],trace_errors(D['nodes'],chain))
            nodes=copy.deepcopy(D['nodes']);nodes[chain[1]]['input_refs']=[]
            self.assertTrue(trace_errors(nodes,chain))
            nodes=copy.deepcopy(D['nodes']);nodes[chain[0]]['role_key']='another role'
            self.assertTrue(trace_errors(nodes,chain))
        for c in D['claims'].values():
            for cid in c.get('source_capability_refs',[]):self.assertEqual('position',D['nodes'][cid]['stage'])

    def test_documentary_fact_does_not_verify_candidate_achievement(self):
        c=D['claims']['F-documentary']
        self.assertEqual([],stretch_errors(c,set(E)))
        self.assertTrue(stretch_errors({**c,'proposition_verified':False},set(E)))
        self.assertTrue(stretch_errors({**self.c,'use_boundary':'VERIFIED_FACT'},set(E)))

    def test_historical_framing_review_never_unlocks_live_preparation(self):
        analysis=D['stage_sequence'][2];prep=D['stage_sequence'][3]
        self.assertEqual('PREPARATION_HOLD',preparation_gate(analysis)['gate'])
        self.assertEqual([],prep['claim_candidates']);self.assertIsNone(prep['packet'])
        self.assertEqual('NOT_FOR_ADOPTION',prep['framing_review']['disposition'])
        self.assertEqual(analysis['role_key'],prep['role_key'])

    def test_frozen_inputs_and_actual_handoff_identity(self):
        for path,digest in D['input_sha256'].items():
            self.assertEqual(digest,hashlib.sha256((ROOT/path).read_bytes()).hexdigest())
        for prev,nxt in zip(D['stage_sequence'],D['stage_sequence'][1:]):
            self.assertIn(prev['id'],nxt['input_refs'])
        self.assertEqual('Tencent:1283126456553382912:2027',D['selected_role_key'])

if __name__=='__main__':unittest.main()
