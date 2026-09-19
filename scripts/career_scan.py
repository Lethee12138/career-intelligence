"""Single user-facing entrypoint for bounded Career Intelligence job scanning.

One invocation runs public-source scanning, deduplication/triage and the
Career review bridge. It produces review artifacts only. No application,
canonical mutation, login, upload, recruiter contact or material editing.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from scripts.job_scan_batch import run_batch
    from scripts.job_scan_review_bridge import build_review_packets
except ModuleNotFoundError:  # direct execution from repository root
    from job_scan_batch import run_batch
    from job_scan_review_bridge import build_review_packets


def _load_json(path: str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text())
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return payload


def build_summary(
    scan: dict[str, Any],
    review: dict[str, Any],
) -> dict[str, Any]:
    priority = []
    for candidate in scan.get("candidate_pool") or []:
        screening = candidate.get("screening") or {}
        if screening.get("state") == "REVIEW_PRIORITY":
            priority.append(
                {
                    "company": candidate.get("company"),
                    "external_job_id": candidate.get("external_job_id"),
                    "role": candidate.get("role"),
                    "location": candidate.get("location"),
                    "verification_status": candidate.get("verification_status"),
                }
            )

    return {
        "scan_id": scan.get("scan_id"),
        "captured_at": scan.get("captured_at"),
        "source_results": scan.get("source_results"),
        "raw_record_count": scan.get("raw_record_count"),
        "deduped_count": scan.get("deduped_count"),
        "screening_counts": scan.get("screening_counts"),
        "review_packet_count": review.get("review_packet_count"),
        "review_state_counts": review.get("review_state_counts"),
        "review_priority_candidates": priority,
        "external_action": False,
        "human_review_required": True,
    }


def run_scan_review(
    scan_config: dict[str, Any],
    career_context: dict[str, Any],
) -> dict[str, Any]:
    scan = run_batch(scan_config)
    review = build_review_packets(scan, career_context)
    return {
        "schema_version": "0.1",
        "operation": "SCAN_AND_REVIEW",
        "candidate_status": "HUMAN_REVIEW_REQUIRED",
        "summary": build_summary(scan, review),
        "scan": scan,
        "review": review,
        "boundary": {
            "read_only_public_sources": True,
            "canonical_write": False,
            "application": False,
            "login": False,
            "upload": False,
            "external_contact": False,
            "cv_edit": False,
            "portfolio_edit": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-config", required=True)
    parser.add_argument("--career-context", required=True)
    parser.add_argument("--output")
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Print only the compact summary; full output is still written with --output.",
    )
    args = parser.parse_args()

    scan_config = _load_json(args.scan_config)
    career_context = _load_json(args.career_context)
    result = run_scan_review(scan_config, career_context)

    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(payload)

    visible = result["summary"] if args.summary_only else result
    print(json.dumps(visible, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
