import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'tests/fixtures/job-scan-synthetic.json').read_text())


class JobScanTests(unittest.TestCase):
    def test_ai_product_role_routes_to_prepare_path(self):
        job = DATA['jobs']['ai-product-hangzhou']
        self.assertEqual('AI Product Manager', job['role'])
        self.assertEqual('Hangzhou', job['location'])
        self.assertEqual('FAST_LANE', job['expected_route'])
        self.assertIn('workflow design', job['signals'])

    def test_digital_solution_sales_signal_requires_caution(self):
        job = DATA['jobs']['digital-sales-risk']
        self.assertEqual('Digital Solution Consultant', job['role'])
        self.assertEqual('WATCH', job['expected_route'])
        self.assertIn('sales target', job['signals'])


if __name__ == '__main__':
    unittest.main()
