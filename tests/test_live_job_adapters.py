import json
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.job_source_runtime import (
    _kuaishou_open_json,
    discover_kuaishou,
    extract_tencent_payload,
    fetch_kuaishou_detail,
    kuaishou_sign,
)


FIXTURES = Path("tests/fixtures")


class LiveJobAdapterTests(unittest.TestCase):
    def test_tencent_official_payload_normalizes_to_verified_record(self):
        payload = json.loads(
            (FIXTURES / "tencent-live-api-synthetic.json").read_text()
        )
        url = (
            "https://join.qq.com/post_detail.html?"
            "postid=1283878533483275264"
        )
        record = extract_tencent_payload(
            payload, url, "2026-09-19T11:00:00+08:00"
        )
        self.assertEqual(record["role"], "用户研究")
        self.assertEqual(record["location"], ["深圳总部", "北京"])
        self.assertEqual(record["business_groups"], ["CSIG", "IEG", "PCG"])
        self.assertEqual(record["verification_status"], "OPEN_VERIFIED")
        self.assertNotIn("fit", record)
        self.assertNotIn("application_decision", record)

    def test_kuaishou_public_signature_matches_frontend_algorithm(self):
        params = {
            "name": "用户产品经理",
            "pageNum": 1,
            "pageSize": 100,
            "workLocationCode": "domestic",
        }
        self.assertEqual(
            kuaishou_sign(params, 1770000000000),
            "4b27b15da07ea3a1068f788b3c2734ce"
            "fded123ed1b7de919391a8953d3407c4",
        )

    def test_kuaishou_discovery_stays_unverified_until_detail(self):
        payload = json.loads(
            (FIXTURES / "kuaishou-live-search-synthetic.json").read_text()
        )
        with patch(
            "scripts.job_source_runtime._kuaishou_open_json",
            return_value=(payload, "https://zhaopin.kuaishou.cn/api"),
        ):
            result = discover_kuaishou("用户产品经理", "domestic", 10)
        self.assertEqual(result["count"], 2)
        self.assertEqual(result["candidates"][0]["external_job_id"], "31523")
        self.assertEqual(
            result["candidates"][0]["verification_status"], "NEEDS_VERIFY"
        )

    def test_kuaishou_detail_verifies_existing_official_record(self):
        payload = json.loads(
            (FIXTURES / "kuaishou-live-detail-synthetic.json").read_text()
        )
        url = (
            "https://zhaopin.kuaishou.cn/recruit/e/"
            "#/official/social/job-info/31523"
        )
        with patch(
            "scripts.job_source_runtime._kuaishou_open_json",
            return_value=(payload, "https://zhaopin.kuaishou.cn/api"),
        ):
            record = fetch_kuaishou_detail(
                url, "2026-09-19T11:00:00+08:00"
            )
        self.assertEqual(record["role"], "商城用户产品经理实习生（导购方向）-【电商】")
        self.assertEqual(record["location"], ["Hangzhou"])
        self.assertEqual(record["verification_status"], "OPEN_VERIFIED")

    def test_kuaishou_runtime_rejects_state_changing_endpoint(self):
        with self.assertRaises(ValueError):
            _kuaishou_open_json(
                "/recruit/e/api/v1/user/apply/position",
                {"positionId": 31523},
            )


if __name__ == "__main__":
    unittest.main()
