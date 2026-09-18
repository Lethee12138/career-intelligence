import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'tests/fixtures/source-adapter-synthetic.json').read_text())


class SourceAdapterTests(unittest.TestCase):
    def test_official_source_has_high_authority(self):
        source = DATA['sources']['official']
        self.assertEqual('official', source['source_type'])
        self.assertEqual('HIGH', source['authority_level'])
        self.assertEqual('OPEN_VERIFIED', source['expected_status'])

    def test_third_party_source_requires_verification(self):
        source = DATA['sources']['public_listing']
        self.assertEqual('third_party', source['source_type'])
        self.assertEqual('MEDIUM', source['authority_level'])
        self.assertEqual('NEEDS_VERIFY', source['expected_status'])

    def test_source_record_is_not_final_decision(self):
        self.assertNotIn('fit', DATA['sources']['official'])
        self.assertNotIn('application_decision', DATA['sources']['official'])
