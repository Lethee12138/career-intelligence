import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from market_calibration_guard import load_salary, compare_base, freshness, benefits_context, import_errors

ROWS = load_salary()
DATE = '2026-09-13'


def inputs(index=0, base=12000):
    row = ROWS[index]
    job = {k: row[k] for k in ('market', 'city', 'route', 'role_family', 'currency_basis')}
    job.update(base=base, refs=['SYNTHETIC:official-role'], role_source_reviewed=True,
               role_key='SYNTHETIC:role', observed_as_of=DATE, eligibility='VERIFY')
    review = dict(as_of=DATE, captured_date=row['captured_date'], decision='USABLE_FOR_CYCLE',
                  reason='Synthetic reviewer decision for this recruiting-cycle example')
    return job, row, review


class CalibrationTests(unittest.TestCase):
    def test_A_partial_directional_no_action(self):
        j,r,v=inputs(base=7000); out=compare_base(j,r,DATE,v)
        self.assertEqual('BELOW_DIRECTIONAL_BAND',out['market_quality_band'])
        self.assertEqual('PARTIAL',out['traceability_status'])
        self.assertIsNone(out['automatic_action']); self.assertIsNone(out['percentile'])

    def test_B_full_still_not_automatic(self):
        j,r,v=inputs(42,35000); out=compare_base(j,r,DATE,v)
        self.assertEqual('FULL',out['traceability_status'])
        self.assertEqual('WITHIN_DIRECTIONAL_BAND',out['market_quality_band'])
        self.assertIsNone(out['automatic_action'])

    def test_C_visa_gate_independent(self):
        j,r,v=inputs(42,35000); r=copy.deepcopy(r)
        before=compare_base(j,r,DATE,v)
        r['visa_salary_gate']='SYNTHETIC threshold 50000';j['eligibility']='NOT ELIGIBLE under synthetic route only'
        after=compare_base(j,r,DATE,v)
        self.assertEqual(before['market_quality_band'],after['market_quality_band'])
        self.assertEqual(j['eligibility'],after['eligibility'])

    def test_D_high_salary_keeps_workload_and_failure(self):
        j,r,v=inputs(base=30000);j.update(quality_concerns=['sustained overtime','bad management'],eligibility='NOT ELIGIBLE')
        out=compare_base(j,r,DATE,v)
        self.assertEqual('ABOVE_DIRECTIONAL_BAND',out['market_quality_band'])
        self.assertEqual(j['quality_concerns'],out['quality_concerns']);self.assertEqual('NOT ELIGIBLE',out['eligibility'])

    def test_E_stale_recheck(self):
        j,r,v=inputs();v['decision']='STALE'
        out=compare_base(j,r,DATE,v)
        self.assertEqual('STALE_RECHECK_REQUIRED',out['freshness'])
        self.assertEqual('INSUFFICIENT_REFERENCE_DATA',out['market_quality_band'])
        self.assertEqual('HISTORICAL_ONLY',out['reference_use'])

    def test_F_actual_salary_preserved_over_estimate(self):
        j,r,v=inputs(base=22000);before=copy.deepcopy((j,r))
        out=compare_base(j,r,DATE,v)
        self.assertEqual(22000,out['actual_base']);self.assertEqual(j['refs'],out['actual_source_refs'])
        self.assertEqual(before,(j,r))

    def test_G_annual_leave_context_preserves_prevalence_verify(self):
        r=next(x for x in benefits_context() if x['market']=='China' and x['dimension']=='Annual leave')
        self.assertIn('5 days',r['baseline']);self.assertIn('10–15',r['competitive']);self.assertIn('VERIFY',r['competitive'])
        self.assertEqual('NOT_ASSESSED',r['traceability_status'])

    def test_H_sparse_family_no_adjacent_substitution(self):
        for i,r in enumerate(ROWS):
            if 'Prototyping' in r['role_family']:
                j,r,v=inputs(i,15000)
                self.assertEqual('INSUFFICIENT_REFERENCE_DATA',compare_base(j,r,DATE,v)['market_quality_band'])

    def test_import_integrity_and_traceability(self):
        self.assertEqual([],import_errors());self.assertEqual(60,len(ROWS))
        self.assertEqual(2,sum(r['traceability_status']=='FULL' for r in ROWS))
        self.assertEqual(58,sum(r['traceability_status']=='PARTIAL' for r in ROWS))
        self.assertTrue(all(r['source_refs'] and r['derivation_note'] and r['sample_count'] for r in ROWS))

    def test_no_implicit_freshness_or_universal_ttl(self):
        self.assertEqual('RECHECK_REQUIRED',freshness(DATE,DATE,'SALARY'))
        self.assertEqual('ROLE_LEVEL_FRESH_VERIFY',freshness(DATE,DATE,'VOLATILE'))
        self.assertEqual('RECHECK_REQUIRED',freshness('2030-01-01',DATE,'SALARY'))
        self.assertEqual('DURABLE_UNLESS_POLICY_CHANGE',freshness(DATE,DATE,'METHOD'))

    def test_basis_scope_and_source_fail_closed(self):
        for change in [{'city':'Other'},{'route':'UNKNOWN'},{'currency_basis':'net annual'}, {'refs':[]},{'observed_as_of':'2025-01-01'},{'base':float('nan')}]:
            j,r,v=inputs();j.update(change)
            self.assertEqual('INSUFFICIENT_REFERENCE_DATA',compare_base(j,r,DATE,v)['market_quality_band'])

    def test_benefits_preserve_two_markets_no_invented_confidence(self):
        rows=benefits_context();self.assertEqual(38,len(rows))
        self.assertEqual({'China','UK'},{r['market'] for r in rows})
        self.assertTrue(all(r['confidence']=='UNKNOWN_NOT_SUPPLIED' and r['last_verified'] is None for r in rows))

if __name__=='__main__':unittest.main()
