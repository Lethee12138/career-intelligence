import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.career_scan import build_summary, resolve_scan_config, run_scan_review


class CareerScanEntrypointTests(unittest.TestCase):
    def test_summary_preserves_counts_and_priority_candidates(self):
        scan = {
            "scan_id": "scan-1",
            "captured_at": "2026-09-19T12:00:00+00:00",
            "source_results": [{"adapter": "sap", "status": "OK"}],
            "raw_record_count": 2,
            "deduped_count": 2,
            "screening_counts": {"REVIEW_PRIORITY": 1, "VERIFY": 1},
            "candidate_pool": [
                {
                    "company": "Example",
                    "external_job_id": "1",
                    "role": "产品经理",
                    "location": ["Hangzhou"],
                    "verification_status": "OPEN_VERIFIED",
                    "screening": {"state": "REVIEW_PRIORITY"},
                },
                {
                    "company": "Other",
                    "external_job_id": "2",
                    "role": "Research",
                    "screening": {"state": "VERIFY"},
                },
            ],
        }
        review = {
            "review_packet_count": 1,
            "review_state_counts": {"QUALIFICATION_REVIEW_REQUIRED": 1},
        }
        summary = build_summary(scan, review)
        self.assertEqual(summary["raw_record_count"], 2)
        self.assertEqual(len(summary["review_priority_candidates"]), 1)
        self.assertFalse(summary["external_action"])
        self.assertTrue(summary["human_review_required"])

    @patch("scripts.career_scan.build_review_packets")
    @patch("scripts.career_scan.run_batch")
    def test_single_entrypoint_composes_scan_and_review(
        self, run_batch_mock, review_mock
    ):
        run_batch_mock.return_value = {
            "scan_id": "scan-1",
            "candidate_pool": [],
            "source_results": [],
            "raw_record_count": 0,
            "deduped_count": 0,
            "screening_counts": {},
        }
        review_mock.return_value = {
            "review_packet_count": 0,
            "review_state_counts": {},
        }
        result = run_scan_review({"scan_id": "scan-1"}, {"candidate_context": {}})
        self.assertEqual(result["operation"], "SCAN_AND_REVIEW")
        self.assertEqual(result["candidate_status"], "HUMAN_REVIEW_REQUIRED")
        self.assertFalse(result["boundary"]["application"])
        self.assertFalse(result["boundary"]["canonical_write"])
        run_batch_mock.assert_called_once()
        review_mock.assert_called_once()

    def test_configured_sources_are_resolved_without_caller_scan_schema(self):
        context = {
            "existing_roles": [
                {
                    "company": "Tencent",
                    "external_job_id": "1283878533483275264",
                }
            ]
        }
        config = resolve_scan_config(None, context)
        adapters = [source["adapter"] for source in config["sources"]]
        self.assertIn("sap", adapters)
        self.assertIn("kuaishou", adapters)
        self.assertIn("tencent", adapters)
        tencent = next(source for source in config["sources"] if source["adapter"] == "tencent")
        self.assertIn("1283878533483275264", tencent["urls"][0])

    def test_custom_scan_config_is_preserved_for_intentional_override(self):
        custom = {
            "scan_id": "custom",
            "sources": [
                {
                    "adapter": "sap",
                    "mode": "discover",
                    "url": "https://jobs.sap.com/search/",
                }
            ],
        }
        self.assertEqual(resolve_scan_config(custom, {}), custom)

    def test_plugin_surface_points_to_one_shot_entrypoint(self):
        root = Path(__file__).resolve().parents[1]
        canonical = (root / "SKILL.md").read_text()
        plugin = (root / "skills/career-intelligence/SKILL.md").read_text()
        contract = (root / "mcp/job-scanner-contract.md").read_text()
        manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
        self.assertIn("scripts/career_scan.py", canonical)
        self.assertIn("one-shot scan entrypoint", plugin)
        self.assertIn("scan_and_review()", contract)
        self.assertEqual(manifest["version"], "0.2.6")

    def test_boundary_explicitly_blocks_material_actions(self):
        with patch("scripts.career_scan.run_batch") as scan_mock, patch(
            "scripts.career_scan.build_review_packets"
        ) as review_mock:
            scan_mock.return_value = {
                "candidate_pool": [],
                "source_results": [],
                "raw_record_count": 0,
                "deduped_count": 0,
                "screening_counts": {},
            }
            review_mock.return_value = {
                "review_packet_count": 0,
                "review_state_counts": {},
            }
            result = run_scan_review({}, {})
        for key in (
            "canonical_write",
            "application",
            "login",
            "upload",
            "external_contact",
            "cv_edit",
            "portfolio_edit",
        ):
            self.assertFalse(result["boundary"][key])


if __name__ == "__main__":
    unittest.main()
