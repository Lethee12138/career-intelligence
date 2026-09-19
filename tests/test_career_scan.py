import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.career_scan import build_summary, run_scan_review


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

    def test_direct_cli_smoke_with_empty_sources(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            scan = tmp / "scan.json"
            context = tmp / "context.json"
            output = tmp / "output.json"
            scan.write_text(json.dumps({"scan_id": "cli-smoke", "sources": []}))
            context.write_text(
                json.dumps(
                    {
                        "candidate_context": {
                            "new_ssot": False,
                            "as_of": "2026-09-19",
                        }
                    }
                )
            )
            completed = subprocess.run(
                [
                    "python3",
                    "scripts/career_scan.py",
                    "--scan-config",
                    str(scan),
                    "--career-context",
                    str(context),
                    "--output",
                    str(output),
                    "--summary-only",
                ],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            )
            visible = json.loads(completed.stdout)
            full = json.loads(output.read_text())
        self.assertEqual(visible["scan_id"], "cli-smoke")
        self.assertEqual(full["operation"], "SCAN_AND_REVIEW")
        self.assertFalse(full["boundary"]["application"])

    def test_plugin_surface_points_to_one_shot_entrypoint(self):
        root = Path(__file__).resolve().parents[1]
        canonical = (root / "SKILL.md").read_text()
        plugin = (root / "skills/career-intelligence/SKILL.md").read_text()
        contract = (root / "mcp/job-scanner-contract.md").read_text()
        manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
        self.assertIn("scripts/career_scan.py", canonical)
        self.assertIn("one-shot scan entrypoint", plugin)
        self.assertIn("scan_and_review()", contract)
        self.assertEqual(manifest["version"], "0.2.4")

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
