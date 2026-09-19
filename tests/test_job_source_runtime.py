import unittest
from pathlib import Path

from scripts.job_source_runtime import (
    adapter_map,
    extract_sap_detail,
    extract_sap_search,
)


FIXTURES = Path("tests/fixtures")


class JobSourceRuntimeTests(unittest.TestCase):
    def test_sap_search_creates_unverified_discovery_candidate(self):
        page = (FIXTURES / "sap-runtime-search.html").read_text()
        rows = extract_sap_search(page, "https://jobs.sap.com/search/", limit=5)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["company"], "SAP")
        self.assertEqual(rows[0]["verification_status"], "NEEDS_VERIFY")
        self.assertTrue(rows[0]["source_url"].startswith("https://jobs.sap.com/job/"))
    def test_sap_detail_verifies_open_official_job(self):
        page = (FIXTURES / "sap-runtime-detail.html").read_text()
        url = "https://jobs.sap.com/job/example/1426364433/"
        row = extract_sap_detail(page, url, "2026-09-19T10:40:00+08:00")
        self.assertEqual(row["external_job_id"], "457795")
        self.assertEqual(row["role"], "iXP - SAP China AI Marketing Intern")
        self.assertEqual(row["location"], "Beijing, CN, 100016")
        self.assertEqual(row["department"], "Administration")
        self.assertEqual(row["verification_status"], "OPEN_VERIFIED")
        self.assertNotIn("fit", row)
        self.assertNotIn("application_decision", row)

    def test_adapter_mappings_are_explicit_about_live_readiness(self):
        self.assertEqual(adapter_map("sap")["runtime_status"], "ACTIVE")
        self.assertEqual(adapter_map("tencent")["verified_hosts"], ["join.qq.com"])
        self.assertEqual(adapter_map("tencent")["runtime_status"], "DETAIL_ACTIVE")
        self.assertEqual(
            adapter_map("kuaishou")["verified_hosts"],
            ["zhaopin.kuaishou.cn"],
        )
        self.assertEqual(adapter_map("kuaishou")["runtime_status"], "SOCIAL_ACTIVE")


if __name__ == "__main__":
    unittest.main()
