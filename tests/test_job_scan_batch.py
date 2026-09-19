import unittest
from unittest.mock import patch

from scripts.job_scan_batch import (
    candidate_identity,
    dedupe_candidates,
    run_batch,
    screen_record,
)


PROFILE = {
    "preferred_locations": ["杭州", "Hangzhou", "深圳", "Shenzhen", "深圳总部"],
    "deprioritized_locations": ["北京", "Beijing"],
    "role_terms": ["产品", "Product", "用户研究"],
    "capability_terms": ["用户研究", "AI", "工作流", "原型", "访谈"],
    "risk_terms": ["销售", "客户拓展", "sales target"],
    "max_experience_years": 1,
}


class JobScanBatchTests(unittest.TestCase):
    def test_identity_prefers_company_and_external_job_id(self):
        row = {"company": "Kuaishou", "external_job_id": "31523"}
        self.assertEqual(
            candidate_identity(row), "kuaishou:external:31523"
        )

    def test_dedupe_keeps_more_verified_record(self):
        lead = {
            "company": "Kuaishou",
            "external_job_id": "31523",
            "verification_status": "NEEDS_VERIFY",
            "role": "用户产品经理",
        }
        detail = {
            "company": "Kuaishou",
            "external_job_id": "31523",
            "verification_status": "OPEN_VERIFIED",
            "role": "用户产品经理",
            "requirements": "本科及以上",
        }
        rows = dedupe_candidates([lead, detail])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["verification_status"], "OPEN_VERIFIED")
        self.assertEqual(rows[0]["duplicate_count"], 2)

    def test_short_ascii_signal_does_not_match_inside_unrelated_word(self):
        row = {
            "company": "SAP",
            "role": "China Open Source Software Developer",
            "location": ["Shanghai"],
            "verification_status": "OPEN_VERIFIED",
        }
        screened = screen_record(row, PROFILE)
        self.assertNotIn("AI", screened["screening"]["role_term_hits"])
        self.assertNotIn("AI", screened["screening"]["capability_term_hits"])

    def test_screening_prioritizes_preferred_location_and_capability(self):
        row = {
            "company": "Example",
            "role": "AI 产品经理",
            "location": ["Hangzhou"],
            "responsibilities": "负责AI工作流和用户研究。",
            "requirements": "应届毕业生可申请。",
            "verification_status": "OPEN_VERIFIED",
        }
        screened = screen_record(row, PROFILE)
        self.assertEqual(screened["screening"]["state"], "REVIEW_PRIORITY")
        self.assertIn("AI", screened["screening"]["capability_term_hits"])
        self.assertFalse(screened["screening"]["final_fit_decision"])

    def test_screening_flags_experience_gap_without_calling_it_final_fit(self):
        row = {
            "company": "Example",
            "role": "产品经理",
            "location": ["Hangzhou"],
            "requirements": "本科及以上学历，3年以上产品经验。",
            "verification_status": "OPEN_VERIFIED",
        }
        screened = screen_record(row, PROFILE)
        self.assertEqual(screened["screening"]["state"], "DEPRIORITIZE")
        self.assertTrue(screened["screening"]["experience_gap_signal"])
        self.assertEqual(
            screened["screening"]["experience_requirement"]["minimum_years"], 3
        )
        self.assertFalse(screened["screening"]["final_fit_decision"])

    def test_verified_but_irrelevant_record_is_reversibly_deprioritized(self):
        row = {
            "company": "SAP",
            "role": "Open Source Software Developer",
            "location": ["Shanghai"],
            "verification_status": "OPEN_VERIFIED",
        }
        screened = screen_record(row, PROFILE)
        self.assertEqual(screened["screening"]["state"], "DEPRIORITIZE")
        self.assertIn(
            "no configured role-family or capability signal found",
            screened["screening"]["reasons"],
        )

    def test_unverified_source_routes_to_verify_first(self):
        row = {
            "company": "Example",
            "role": "产品经理",
            "location": ["Hangzhou"],
            "verification_status": "NEEDS_VERIFY",
        }
        screened = screen_record(row, PROFILE)
        self.assertEqual(screened["screening"]["state"], "VERIFY")

    @patch("scripts.job_scan_batch._detail_source")
    @patch("scripts.job_scan_batch._discover_source")
    def test_batch_combines_sources_dedupes_and_preserves_boundaries(
        self, discover_mock, detail_mock
    ):
        discover_mock.return_value = [
            {
                "company": "Kuaishou",
                "external_job_id": "31523",
                "role": "AI 产品经理",
                "location": ["Hangzhou"],
                "responsibilities": "AI 工作流与用户研究",
                "requirements": "应届可申请",
                "verification_status": "OPEN_VERIFIED",
            }
        ]
        detail_mock.return_value = [
            {
                "company": "Tencent",
                "external_job_id": "128",
                "role": "用户研究",
                "location": ["深圳总部"],
                "responsibilities": "用户访谈与AI研究",
                "requirements": "应届毕业生",
                "verification_status": "OPEN_VERIFIED",
            }
        ]
        config = {
            "scan_id": "synthetic",
            "profile": PROFILE,
            "sources": [
                {"adapter": "kuaishou", "mode": "discover", "url": "https://example"},
                {"adapter": "tencent", "mode": "detail", "url": "https://example"},
            ],
        }
        result = run_batch(config)
        self.assertEqual(result["deduped_count"], 2)
        self.assertEqual(result["screening_counts"]["REVIEW_PRIORITY"], 2)
        self.assertFalse(result["boundary"]["application"])
        self.assertFalse(result["boundary"]["final_fit_decision"])


if __name__ == "__main__":
    unittest.main()
