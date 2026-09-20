from pathlib import Path
import unittest


class CapabilityRoleTaxonomyTests(unittest.TestCase):
    def test_required_families_and_boundaries_are_present(self):
        text = (Path(__file__).parents[1] / 'schemas' / 'capability-role-family-taxonomy.md').read_text()
        for family in (
            'PRODUCT', 'AI_PRODUCT_HUMAN_AI_WORKFLOW', 'USER_PRODUCT_RESEARCH',
            'PRODUCT_OPERATIONS', 'DIGITAL_TRANSFORMATION', 'INNOVATION',
            'EXPERIENCE_SERVICE_DESIGN',
        ):
            self.assertIn(f'`{family}`', text)
        for title in ('Product Manager', 'AI Product Manager', 'User Researcher',
                      'Product Operations Manager', 'Digital Transformation Analyst',
                      'Innovation Strategist', 'Service Designer'):
            self.assertIn(title, text)
        self.assertIn('AI-CORE', text)
        self.assertIn('AI-ENABLED', text)
        self.assertIn('NONE', text)
        self.assertIn('negative_title_traps', text)


if __name__ == '__main__':
    unittest.main()
