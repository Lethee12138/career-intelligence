import json
import unittest
from pathlib import Path


class TestSAPRealFetchPrototype(unittest.TestCase):
    def test_public_source_boundary(self):
        path = Path('tests/fixtures/sap-real-fetch-prototype.json')
        data = json.loads(path.read_text())
        self.assertEqual(data['source_type'], 'official')
        self.assertEqual(data['adapter'], 'sap')
        self.assertEqual(data['fetch_status'], 'SUCCESS')
        self.assertIn('job_id', data['fields'])


if __name__ == '__main__':
    unittest.main()
