import json
import unittest
from pathlib import Path


class TestSAPRuntime(unittest.TestCase):
    def test_sap_official_source_boundary(self):
        data = json.loads(Path('tests/fixtures/sap-runtime-synthetic.json').read_text())
        self.assertEqual(data['company'], 'SAP')
        self.assertEqual(data['source_type'], 'official')
        self.assertEqual(data['authority_level'], 'HIGH')
        self.assertEqual(data['verification_status'], 'OPEN_VERIFIED')


if __name__ == '__main__':
    unittest.main()
