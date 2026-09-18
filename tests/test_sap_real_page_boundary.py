import json
import unittest
from pathlib import Path


class TestSAPRealPageBoundary(unittest.TestCase):
    def test_source_boundary_fixture(self):
        path = Path('tests/fixtures/sap-real-page-boundary.json')
        data = json.loads(path.read_text())
        self.assertEqual(data['source_type'], 'official')
        self.assertEqual(data['adapter'], 'sap')
        self.assertIn('OPEN_VERIFIED', data['verification'])


if __name__ == '__main__':
    unittest.main()
