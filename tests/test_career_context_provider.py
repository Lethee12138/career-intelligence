import json
import tempfile
import unittest
from pathlib import Path

from scripts.career_context_provider import (
    CareerContextError,
    context_status,
    load_current_career_context,
)


class CareerContextProviderTests(unittest.TestCase):
    def write_context(self, root: Path):
        path = root / "context.json"
        path.write_text(
            json.dumps(
                {
                    "context_version": "CTX-1",
                    "as_of": "2026-09-19",
                    "existing_roles": [
                        {
                            "company": "Tencent",
                            "external_job_id": "100",
                            "role": "AI 产品经理",
                            "current_state": "TARGETED_PREPARE",
                        },
                        {
                            "company": "Kuaishou",
                            "external_job_id": "13299",
                            "role": "用户产品经理",
                            "current_state": "REMAIN_VERIFY",
                        },
                    ],
                    "preference_context": {
                        "beijing_default": "DEPRIORITIZED"
                    },
                    "company_constraints": {
                        "Kuaishou": [{"constraint": "ONE_ACTIVE"}]
                    },
                }
            )
        )
        return path

    def test_provider_loads_read_only_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_context(Path(tmp))
            value = load_current_career_context(path=path)
        provider = value["_context_provider"]
        self.assertEqual(provider["source"], "CURRENT_LOCAL_CONTEXT")
        self.assertEqual(provider["version"], "CTX-1")
        self.assertEqual(provider["existing_role_count"], 2)
        self.assertTrue(provider["read_only"])
        self.assertFalse(provider["canonical_write"])

    def test_overlay_updates_matching_role_but_cannot_delete_other_roles(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_context(Path(tmp))
            value = load_current_career_context(
                {
                    "existing_roles": [
                        {
                            "company": "Tencent",
                            "external_job_id": "100",
                            "application_status": "NOT_SUBMITTED",
                        },
                        {
                            "company": "ByteDance",
                            "external_job_id": "A1",
                            "role": "用户研究",
                        },
                    ]
                },
                path=path,
            )
        roles = value["existing_roles"]
        self.assertEqual(len(roles), 3)
        tencent = next(
            row for row in roles
            if row["company"] == "Tencent"
            and row["external_job_id"] == "100"
        )
        self.assertEqual(tencent["current_state"], "TARGETED_PREPARE")
        self.assertEqual(tencent["application_status"], "NOT_SUBMITTED")
        self.assertTrue(
            any(row["external_job_id"] == "13299" for row in roles)
        )

    def test_missing_provider_fails_instead_of_reconstructing_from_memory(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing.json"
            with self.assertRaisesRegex(
                CareerContextError,
                "refresh the local Career context snapshot",
            ):
                load_current_career_context(path=path)

    def test_status_exposes_version_not_private_role_details(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_context(Path(tmp))
            status = context_status(path=path)
        self.assertEqual(status["version"], "CTX-1")
        self.assertEqual(status["existing_role_count"], 2)
        self.assertNotIn("existing_roles", status)


if __name__ == "__main__":
    unittest.main()
