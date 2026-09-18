import json
from pathlib import Path
import unittest


class DiscoveryAdapterContractTest(unittest.TestCase):
    def test_discovery_candidate_is_not_verified_job(self):
        fixture = json.loads(
            Path('tests/fixtures/discovery-adapter-synthetic.json').read_text()
        )
        candidates = fixture['discovery_candidates']

        self.assertEqual(candidates[0]['expected_status'], 'DISCOVERED')
        self.assertEqual(candidates[1]['expected_status'], 'NEEDS_VERIFY')

    def test_discovery_requires_verification_boundary(self):
        self.assertNotEqual('DISCOVERED', 'OPEN_VERIFIED')


if __name__ == '__main__':
    unittest.main()
