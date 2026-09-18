import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'tests/fixtures/sap-adapter-synthetic.json').read_text())


class SAPAdapterPrototypeTests(unittest.TestCase):
    def test_official_source_identity(self):
        self.assertEqual('official', DATA['source']['source_type'])
        self.assertEqual('HIGH', DATA['source']['authority_level'])

    def test_adapter_output_keeps_assessment_separate(self):
        self.assertNotIn('fit', DATA['job'])
        self.assertNotIn('application_decision', DATA['job'])

    def test_job_status_is_verification_state(self):
        self.assertEqual('OPEN_VERIFIED', DATA['job']['status'])


if __name__ == '__main__':
    unittest.main()
