import json
import unittest
from pathlib import Path


class JobScannerRuntimePrototypeTest(unittest.TestCase):
    def test_official_source_preserves_authority(self):
        data = json.loads(Path('tests/fixtures/runtime-source-synthetic.json').read_text())
        source = data['sources'][0]
        self.assertEqual(source['source_type'], 'official')
        self.assertEqual(source['authority_level'], 'HIGH')
        self.assertEqual(source['job_status'], 'OPEN_VERIFIED')

    def test_third_party_requires_verification(self):
        data = json.loads(Path('tests/fixtures/runtime-source-synthetic.json').read_text())
        source = data['sources'][1]
        self.assertEqual(source['source_type'], 'third_party')
        self.assertEqual(source['job_status'], 'NEEDS_VERIFY')


if __name__ == '__main__':
    unittest.main()
