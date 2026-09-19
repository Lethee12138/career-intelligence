import unittest

from scripts.job_scan_review_bridge import build_review_packets, exact_role_key


class JobScanReviewBridgeTests(unittest.TestCase):
    def test_exact_role_key_prefers_company_scoped_external_id(self):
        row = {"company": "Tencent", "external_job_id": "128"}
        self.assertEqual(exact_role_key(row), "tencent:external:128")

    def test_existing_role_is_continuity_not_duplicate(self):
        scan = {
            "scan_id": "scan",
            "candidate_pool": [
                {
                    "company": "Tencent",
                    "external_job_id": "128",
                    "role": "用户研究",
                    "location": ["深圳总部"],
                    "source_url": "https://join.qq.com/post_detail.html?postid=128",
                    "verification_status": "OPEN_VERIFIED",
                    "screening": {"state": "REVIEW_PRIORITY"},
                    "requirements": "应届毕业生",
                }
            ],
        }
        context = {
            "candidate_context": {"as_of": "2026-09-19", "new_ssot": False},
            "existing_roles": [
                {
                    "company": "Tencent",
                    "external_job_id": "128",
                    "current_state": "FORM_READY",
                }
            ],
        }
        out = build_review_packets(scan, context)
        self.assertEqual(out["review_packet_count"], 1)
        packet = out["packets"][0]
        self.assertEqual(packet["review_state"], "EXISTING_POOL_CONTINUITY")
        self.assertEqual(packet["next_step"], "REUSE_EXISTING_ROLE_STATE")
        self.assertEqual(packet["existing_role"]["current_state"], "FORM_READY")

    def test_internship_and_sql_require_qualification_review(self):
        scan = {
            "candidate_pool": [
                {
                    "company": "Kuaishou",
                    "external_job_id": "31523",
                    "role": "产品经理实习生",
                    "verification_status": "OPEN_VERIFIED",
                    "screening": {"state": "REVIEW_PRIORITY"},
                    "requirements": "连续实习3个月，每周出勤5天；会使用SQL。",
                }
            ]
        }
        out = build_review_packets(scan, {"candidate_context": {}})
        packet = out["packets"][0]
        self.assertEqual(
            packet["review_state"], "QUALIFICATION_REVIEW_REQUIRED"
        )
        self.assertIn(
            "INTERNSHIP_DURATION_OR_ATTENDANCE",
            packet["qualification_gate"]["markers"],
        )
        self.assertIn(
            "TOOL_OR_QUANT_REQUIREMENT",
            packet["qualification_gate"]["markers"],
        )

    def test_internship_title_alone_requires_qualification_review(self):
        scan = {
            "candidate_pool": [
                {
                    "company": "Kuaishou",
                    "external_job_id": "31011",
                    "role": "用户产品经理实习生",
                    "verification_status": "OPEN_VERIFIED",
                    "screening": {"state": "REVIEW"},
                    "requirements": "本科及以上学历。",
                }
            ]
        }
        out = build_review_packets(scan, {"candidate_context": {}})
        packet = out["packets"][0]
        self.assertEqual(
            packet["review_state"], "QUALIFICATION_REVIEW_REQUIRED"
        )
        self.assertIn("INTERNSHIP_ROUTE", packet["qualification_gate"]["markers"])

    def test_unverified_candidate_never_enters_analysis_directly(self):
        scan = {
            "candidate_pool": [
                {
                    "company": "Example",
                    "external_job_id": "1",
                    "role": "产品经理",
                    "verification_status": "NEEDS_VERIFY",
                    "screening": {"state": "REVIEW"},
                }
            ]
        }
        out = build_review_packets(scan, {"candidate_context": {}})
        self.assertEqual(
            out["packets"][0]["review_state"], "SOURCE_VERIFY_FIRST"
        )

    def test_only_review_states_are_bridged(self):
        scan = {
            "candidate_pool": [
                {
                    "company": "A",
                    "external_job_id": "1",
                    "screening": {"state": "REVIEW_PRIORITY"},
                    "verification_status": "OPEN_VERIFIED",
                },
                {
                    "company": "B",
                    "external_job_id": "2",
                    "screening": {"state": "DEPRIORITIZE"},
                    "verification_status": "OPEN_VERIFIED",
                },
            ]
        }
        out = build_review_packets(scan, {"candidate_context": {}})
        self.assertEqual(out["review_packet_count"], 1)
        self.assertEqual(out["packets"][0]["job_identity"]["company"], "A")

    def test_bridge_preserves_no_action_boundaries(self):
        out = build_review_packets(
            {"candidate_pool": []},
            {"candidate_context": {"as_of": "2026-09-19"}},
        )
        self.assertFalse(out["boundary"]["canonical_write"])
        self.assertFalse(out["boundary"]["application"])
        self.assertFalse(out["boundary"]["cv_edit"])
        self.assertFalse(out["boundary"]["portfolio_edit"])


if __name__ == "__main__":
    unittest.main()
