import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.career_scan import build_summary, resolve_scan_config, run_scan_review


class CareerScanEntrypointTests(unittest.TestCase):
    @staticmethod
    def _discovery_payload():
        return {
            "capabilityProfile": {"profile_ref": "SYNTHETIC-PROFILE"},
            "roleHypotheses": [{
                "id": "H1",
                "role_or_family": "Product / Digital Product",
                "taxonomy_ref": "schemas/capability-role-family-taxonomy.md#product",
                "capability_root_refs": ["cap-product"],
                "search_terms": {
                    "China": {"title": [{"term": "Product Manager", "why": "family variant"}]},
                    "UK": {"title": [{"term": "Product Manager", "why": "family variant"}]},
                    "Other": {"title": [{"term": "Product Manager", "why": "family variant"}]},
                },
            }],
            "marketScope": ["China", "UK"],
            "locationScope": ["Hangzhou", "London"],
            "companyTypes": ["technology", "research-led"],
            "candidateConstraints": {"no_external_action": True},
            "candidates": [{
                "company": "Synthetic Discovery Co",
                "external_job_id": "DISC-1",
                "role": "Product Manager",
                "location": ["Hangzhou"],
                "role_family": "Product / Digital Product",
                "ai_involvement": "NONE",
                "evidence_refs": ["SYN-E1"],
                "matched_role_hypothesis": "H1",
            }],
        }

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

    def test_market_discovery_uses_handoff_without_configured_sources(self):
        result = run_scan_review(
            None,
            {},
            use_configured_sources=True,
            use_current_career_context=False,
            mode="market_discovery",
            discovery=self._discovery_payload(),
        )
        self.assertEqual(result["mode"], "market_discovery")
        self.assertEqual(result["scan_config_source"], "DISCOVERY_INPUT")
        self.assertEqual(result["source_scope"]["sources"], [])
        self.assertEqual(result["discovery"]["handoff_schema_version"], "0.2.4")
        self.assertEqual(result["discovery"]["role_hypothesis_count"], 1)
        candidate = result["pool_view"]["candidates"][0]
        self.assertEqual(candidate["role_family"], "Product / Digital Product")
        self.assertEqual(candidate["ai_involvement"], "NONE")
        self.assertEqual(candidate["evidence_refs"], ["SYN-E1"])
        self.assertEqual(candidate["next_action"], "VERIFY_OFFICIAL_SOURCE")

    @patch("scripts.career_scan.build_review_packets")
    @patch("scripts.career_scan.run_batch")
    def test_hybrid_discovery_merges_and_dedupes_configured_candidates(
        self, run_batch_mock, review_mock
    ):
        run_batch_mock.return_value = {
            "scan_id": "configured",
            "captured_at": "2026-09-21T00:00:00+00:00",
            "candidate_pool": [{
                "company": "Synthetic Discovery Co",
                "external_job_id": "DISC-1",
                "role": "Product Manager",
                "location": ["Hangzhou"],
                "verification_status": "OPEN_VERIFIED",
                "screening": {"state": "REVIEW", "reasons": ["configured"]},
            }],
            "source_results": [{"adapter": "sap", "status": "OK"}],
            "raw_record_count": 1,
            "deduped_count": 1,
            "screening_counts": {"REVIEW": 1},
        }
        review_mock.return_value = {"review_packet_count": 0, "review_state_counts": {}}
        result = run_scan_review(
            None,
            {},
            use_configured_sources=True,
            use_current_career_context=False,
            mode="hybrid_discovery",
            discovery=self._discovery_payload(),
        )
        self.assertEqual(result["scan_config_source"], "CURRENT_CONFIGURED_SOURCES_PLUS_DISCOVERY_INPUT")
        self.assertEqual(result["scan"]["deduped_count"], 1)
        self.assertEqual(result["scan"]["candidate_pool"][0]["verification_status"], "OPEN_VERIFIED")
        self.assertEqual(result["discovery"]["candidate_count"], 1)
        self.assertEqual(result["pool_view"]["candidates"][0]["role_family"], "UNKNOWN")

    @patch("scripts.career_scan.build_review_packets")
    @patch("scripts.career_scan.run_batch")
    def test_configured_review_keeps_current_source_path(self, run_batch_mock, review_mock):
        run_batch_mock.return_value = {
            "scan_id": "configured",
            "captured_at": "2026-09-21T00:00:00+00:00",
            "candidate_pool": [],
            "source_results": [],
            "raw_record_count": 0,
            "deduped_count": 0,
            "screening_counts": {},
        }
        review_mock.return_value = {"review_packet_count": 0, "review_state_counts": {}}
        result = run_scan_review(
            None, {}, use_configured_sources=True, use_current_career_context=False,
            mode="configured_review",
        )
        self.assertEqual(result["mode"], "configured_review")
        self.assertEqual(result["scan_config_source"], "CURRENT_CONFIGURED_SOURCES")
        self.assertEqual(result["discovery"]["state"], "NOT_REQUESTED")

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
        custom = {
            "scan_id": "scan-1",
            "sources": [
                {
                    "adapter": "sap",
                    "mode": "discover",
                    "url": "https://jobs.sap.com/search/",
                }
            ],
        }
        result = run_scan_review(
            custom,
            {"candidate_context": {}},
            use_configured_sources=False,
            use_current_career_context=False,
        )
        self.assertEqual(result["operation"], "SCAN_AND_REVIEW")
        self.assertEqual(result["candidate_status"], "HUMAN_REVIEW_REQUIRED")
        self.assertEqual(result["schema_version"], "0.3")
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

    @patch("scripts.career_scan.build_review_packets")
    @patch("scripts.career_scan.run_batch")
    def test_broad_and_focused_never_change_source_scope(
        self, run_batch_mock, review_mock
    ):
        run_batch_mock.return_value = {
            "scan_id": "same-scan",
            "candidate_pool": [
                {
                    "company": "A",
                    "external_job_id": "1",
                    "screening": {"state": "REVIEW_PRIORITY"},
                },
                {
                    "company": "B",
                    "external_job_id": "2",
                    "screening": {"state": "DEPRIORITIZE"},
                },
            ],
            "source_results": [],
            "raw_record_count": 2,
            "deduped_count": 2,
            "screening_counts": {
                "REVIEW_PRIORITY": 1,
                "DEPRIORITIZE": 1,
            },
        }
        review_mock.return_value = {
            "review_packet_count": 1,
            "review_state_counts": {},
        }
        custom = {
            "scan_id": "custom",
            "sources": [
                {
                    "adapter": "sap",
                    "mode": "discover",
                    "url": "https://jobs.sap.com/search/?q=Product&locationsearch=China",
                    "limit": 10,
                }
            ],
        }
        broad = run_scan_review(
            custom, {}, use_configured_sources=False,
            use_current_career_context=False, pool_mode="BROAD"
        )
        focused = run_scan_review(
            custom, {}, use_configured_sources=False,
            use_current_career_context=False, pool_mode="FOCUSED"
        )
        self.assertEqual(
            broad["source_scope"]["fingerprint"],
            focused["source_scope"]["fingerprint"],
        )
        self.assertFalse(broad["pool_view"]["source_scope_changed"])
        self.assertFalse(focused["pool_view"]["source_scope_changed"])
        self.assertEqual(broad["pool_view"]["retained_candidate_count"], 2)
        self.assertEqual(focused["pool_view"]["retained_candidate_count"], 1)
        self.assertEqual(len(broad["pool_view"]["candidates"]), 2)
        self.assertEqual(
            broad["pool_view"]["candidates"][0]["screening_state"],
            "REVIEW_PRIORITY",
        )

    def test_configured_mode_rejects_caller_source_override(self):
        with self.assertRaisesRegex(
            ValueError, "pool mode never changes source scope"
        ):
            run_scan_review(
                {"sources": [{"adapter": "sap"}]},
                {},
                use_configured_sources=True,
                use_current_career_context=False,
            )

    def test_plugin_surface_points_to_one_shot_entrypoint(self):
        root = Path(__file__).resolve().parents[1]
        canonical = (root / "SKILL.md").read_text()
        plugin = (root / "skills/career-intelligence/SKILL.md").read_text()
        contract = (root / "mcp/job-scanner-contract.md").read_text()
        manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
        self.assertIn("scripts/career_scan.py", canonical)
        self.assertIn("one-shot scan entrypoint", plugin)
        self.assertIn("scan_and_review()", contract)
        self.assertEqual(manifest["version"], "0.2.8")

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
            result = run_scan_review(
                {
                    "sources": [
                        {
                            "adapter": "sap",
                            "mode": "discover",
                            "url": "https://jobs.sap.com/search/",
                        }
                    ]
                },
                {},
                use_configured_sources=False,
                use_current_career_context=False,
            )
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
