import json
from pathlib import Path
import unittest


class OfficialAdapterContractTest(unittest.TestCase):
    def test_official_source_has_high_authority(self):
        data = json.loads(
            Path('tests/fixtures/official-adapter-synthetic.json').read_text()
        )
        self.assertEqual(data['official_job']['source_type'], 'official')
        self.assertEqual(data['official_job']['authority_level'], 'HIGH')

    def test_unknown_open_state_needs_verification(self):
        data = json.loads(
            Path('tests/fixtures/official-adapter-synthetic.json').read_text()
        )
        self.assertEqual(data['missing_status']['expected_status'], 'NEEDS_VERIFY')


if __name__ == '__main__':
    unittest.main()
