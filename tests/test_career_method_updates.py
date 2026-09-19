import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CareerMethodUpdateTests(unittest.TestCase):
    def read(self, rel):
        return (ROOT / rel).read_text()

    def test_secondary_discovery_source_requires_official_verification(self):
        text = self.read("rules/career-tooling.md")
        self.assertIn("来个OC / givemeoc", text)
        self.assertIn("二级岗位发现资料源", text)
        self.assertIn("employer-official verification", text)

    def test_china_early_scan_window_is_recorded(self):
        text = self.read("rules/career-tooling.md")
        self.assertIn("July–August", text)
        self.assertIn("foreign enterprises", text)
        self.assertIn("consulting", text)

    def test_prefill_requires_human_check_and_sensitive_fields(self):
        text = self.read("rules/career-tooling.md")
        self.assertIn("automatic prefill → Human check → Human submit", text)
        for term in (
            "graduation date",
            "visa / work-right status",
            "salary",
            "work location",
        ):
            self.assertIn(term, text)

    def test_interview_dossier_and_ai_product_template_are_bounded(self):
        text = self.read("rules/interview-preparation.md")
        self.assertIn("Company interview research dossier", text)
        self.assertIn("Short-term AI Product / Agent preparation template", text)
        self.assertIn("RAG", text)
        self.assertIn("Bad Case", text)
        self.assertIn("not a promised timeline", text)

    def test_cv_quantification_forbids_invented_outcomes(self):
        text = self.read("rules/cv-claims.md")
        self.assertIn("Evidence-based quantification", text)
        for term in (
            "conversion rate",
            "ROI",
            "user growth",
            "efficiency-improvement percentages",
        ):
            self.assertIn(term, text)

    def test_external_skills_cannot_replace_career_pipeline(self):
        text = self.read("rules/career-tooling.md")
        self.assertIn("Do not rebuild a second Career pipeline", text)
        self.assertIn("Evidence First", text)


if __name__ == "__main__":
    unittest.main()
