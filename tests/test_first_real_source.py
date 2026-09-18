import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'tests/fixtures/first-real-source-synthetic.json').read_text())


class FirstRealSourceTests(unittest.TestCase):
    def test_official_source_has_high_authority(self):
        self.assertEqual('official', DATA['source']['source_type'])
        self.assertEqual('HIGH', DATA['source']['authority_level'])

    def test_source_does_not_make_career_decision(self):
        self.assertIsNone(DATA['expected']['fit_decision'])
        self.assertIsNone(DATA['expected']['application_decision'])


if __name__ == '__main__':
    unittest.main()
