"""Offline behavioral regression for pure guards, not a live LLM/ATS test."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("career_guard", ROOT / "scripts/guard.py")
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def read(name):
    return json.loads((ROOT / "tests/fixtures" / name).read_text())


EVIDENCE = read("evidence-excerpts.json")["evidence"]
CASES = {c: read(name) for c, name in [
    ("A", "A-tencent.json"), ("B", "B-kuaishou-user.json"),
    ("C", "C-baidu.json"), ("D", "D-kuaishou-commerce.json"),
    ("E", "E-stale-source.json"), ("F", "F-dneg-packet.json")]}


def eligible_checks():
    # Controlled structural inputs, not newly verified employer evidence.
    return [{"hierarchy": "MUST", "result": "PASS", "verified": True,
             "refs": ["test-only-verified-graduation-gate"]}]


def ready_input():
    # Synthetic gate-positive control. Never an assertion that a real job is open.
    return {"role_key": "test-only-role", "qualification": "ELIGIBLE",
            "source_status": {"role_key": "test-only-role", "status": "OPEN", "live_verified": True, "refs": ["test-only-authority"]},
            "evidence_justifies_preparation": True, "recommendation": "Apply",
            "critical_unknowns": [], "one_active_application": False}


def packet():
    def field(value, refs, kind="EXTERNAL_REPORT"):
        return {"value": value, "refs": refs, "kind": kind}
    unknown = {"value": "UNKNOWN", "refs": [], "kind": "UNKNOWN"}
    return {"trigger": "HUMAN_AI_JUDGEMENT", "truth_source": False,
            "user_problem": field("Creative intent drift in AI-assisted creative workflows", ["dneg-ownership"]),
            "why_selected": copy.deepcopy(unknown),
            "end_to_end_flow": field("Anchor → Compare → Feedback → Human Decision → History", ["dneg-workflow"]),
            "product_decisions": field("Humans keep final creative judgment", ["dneg-ownership"]),
            "technical_decisions": copy.deepcopy(unknown),
            "ai_contribution": field("Codex-assisted prototype implementation and modification", ["dneg-ownership"]),
            "human_contribution": field("Prototype, testing and iteration decisions", ["dneg-ownership"]),
            "team_contribution": field("Shared research and parts of problem definition", ["dneg-ownership"]),
            "testing_evaluation": field("3 formal rounds; not a participant count", ["dneg-testing"]),
            "discovered_problems": copy.deepcopy(unknown),
            "iteration": field("9+ documented changes at aggregate scope; event-level trace UNKNOWN", ["dneg-testing"]),
            "real_feedback": copy.deepcopy(unknown),
            "approved_artifact_refs": copy.deepcopy(unknown),
            "interviewer_objections": field("Which decisions were yours versus AI or team?", ["dneg-ownership"], "INFERENCE"),
            "answer_boundaries": field("AI-assisted prototype does not establish software engineering, live model execution or commercial efficiency", ["dneg-ownership", "dneg-runtime"], "INFERENCE"),
            "event_trace_status": "UNKNOWN", "change_events": []}


class CareerRegression(unittest.TestCase):
    def test_A_qualification_does_not_reject_preferred_major_gap(self):
        checks = eligible_checks() + [{"hierarchy": "STRONG PREFERENCE", "result": "FAIL"}]
        self.assertEqual(g.qualification(checks, True), CASES["A"]["expected"]["qualification_with_preferred_major_gap"])

    def test_A_all_positive_matches_have_inspected_bounded_evidence(self):
        for row in CASES["A"]["requirements"]:
            self.assertEqual(g.match_errors(row, EVIDENCE), [])
        row = copy.deepcopy(CASES["A"]["requirements"][0])
        row["evidence_refs"] = ["invented-evidence"]
        self.assertTrue(g.match_errors(row, EVIDENCE))

    def test_A_unknown_HC_does_not_become_fact_or_multiple_CVs(self):
        self.assertEqual(CASES["A"]["scenario"]["kind"], "INFERENCE")
        self.assertEqual(CASES["A"]["hc"], "UNKNOWN")
        self.assertEqual(CASES["A"]["cv_strategy_count"], 1)
        # Reviewed fixture assertions; semantic classification remains agent-reviewed.

    def test_B_and_C_graduation_intervals_inside_reported_windows(self):
        for key in ("B", "C"):
            c = CASES[key]
            self.assertEqual(g.window_match(*c["candidate_window"], *c["graduate_window"]),
                             c["expected"]["window_qualification"])

    def test_B_slot_occupied_unknown_clear_and_same_role(self):
        for slot, expected in [("other-role", "PREPARATION_HOLD"), ("UNKNOWN", "PREPARATION_HOLD"),
                               ("CLEAR", "READY_FOR_REVIEW"), ("test-only-role", "READY_FOR_REVIEW")]:
            with self.subTest(slot=slot):
                a = ready_input()
                a.update(one_active_application=True, company_slot=slot)
                self.assertEqual(g.preparation_gate(a)["gate"], expected)

    def test_B_completed_evidence_excludes_active_projects_but_not_AR_research(self):
        c = CASES["B"]
        row = copy.deepcopy(c["requirements"][0])
        row["evidence_refs"] = ["ar-research"]
        self.assertEqual(g.match_errors(row, EVIDENCE, c["excluded"], True), [])
        for ref in ("paw-active", "portfolio-active"):
            row["evidence_refs"] = [ref]
            self.assertTrue(g.match_errors(row, EVIDENCE, c["excluded"], True))
        # Even later completion cannot silently remove explicit batch exclusions.
        newer = copy.deepcopy(EVIDENCE)
        newer["paw-active"]["completion_at_cutoff"] = "COMPLETED"
        row["evidence_refs"] = ["paw-active"]
        self.assertTrue(g.match_errors(row, newer, c["excluded"], True))

    def test_B_product_data_partial_keeps_commercial_gap(self):
        row = copy.deepcopy(CASES["B"]["requirements"][1])
        self.assertEqual(row["match_level"], "PARTIAL")
        self.assertEqual(g.match_errors(row, EVIDENCE), [])
        row["unsupported_scope"] = "UNKNOWN"
        self.assertTrue(g.match_errors(row, EVIDENCE))

    def test_C_high_value_does_not_erase_practical_penalty(self):
        c = CASES["C"]
        self.assertEqual((c["career_value"], c["practical_fit"]), ("HIGH", "LOW"))
        self.assertIn("Direct functional", c["high_value_exception"])

    def test_D_city_cannot_override_required_domain_gap(self):
        a = {"dimensions": {d: {"rationale": "Test-only independent dimension"} for d in g.DIMENSIONS},
             "mandatory_domain_gap": True, "recommendation": "High Priority Apply"}
        self.assertTrue(g.assessment_errors(a))
        a["recommendation"] = CASES["D"]["expected"]["recommendation"]
        self.assertEqual(g.assessment_errors(a), [])

    def test_E_assistant_report_is_not_original_authority(self):
        c = CASES["E"]
        self.assertEqual(c["historical_report"]["reported_decision"], "CLOSED")
        result = g.resolve_status(c["role_key"], [], c["as_of"])
        self.assertEqual(result["status"], c["expected"]["current_status"])

    def test_E_inspected_authority_filled_beats_newer_discovery_open(self):
        # Fault injection derived from real reported conflict, NOT original snapshots.
        observations = [
            {"role_key": "test-role", "ref": "test-authority", "authority_for_role": True,
             "inspected_original": True, "observed_at": "2026-09-09", "status": "FILLED"},
            {"role_key": "test-role", "ref": "test-mirror", "authority_for_role": False,
             "inspected_original": True, "observed_at": "2026-09-10", "status": "OPEN"}]
        r = g.resolve_status("test-role", observations, "2026-09-10", "LIVE")
        self.assertEqual(r["status"], "CLOSED")
        a = ready_input()
        a["source_status"] = r
        self.assertEqual(g.preparation_gate(a)["gate"], "PREPARATION_HOLD")

    def test_source_identity_and_dates_cannot_be_stitched(self):
        obs = [{"role_key": "other-role", "ref": "authority", "authority_for_role": True,
                "inspected_original": True, "observed_at": "2026-09-10", "status": "OPEN"}]
        self.assertEqual(g.resolve_status("target", obs, "2026-09-10")["status"], "VERIFY")
        obs[0]["role_key"] = "target"
        self.assertEqual(g.resolve_status("target", obs, "2026-09-09")["status"], "VERIFY")

    def test_conflicting_authority_and_404_require_verify(self):
        o = {"role_key": "target", "ref": "test", "authority_for_role": True,
             "inspected_original": True, "observed_at": "2026-09-10", "status": "OPEN"}
        for other in ("CLOSED", "404", "UNKNOWN"):
            self.assertEqual(g.resolve_status("target", [o, {**o, "status": other}], "2026-09-10")["status"], "VERIFY")
        self.assertEqual(g.resolve_status("target", [{**o, "status": "404"}], "2026-09-10")["status"], "VERIFY")

    def test_later_authority_can_explicitly_reopen(self):
        o = {"role_key": "target", "ref": "test", "authority_for_role": True,
             "inspected_original": True, "observed_at": "2026-09-09", "status": "CLOSED"}
        r = g.resolve_status("target", [o, {**o, "observed_at": "2026-09-10", "status": "OPEN"}], "2026-09-10", "LIVE")
        self.assertEqual((r["status"], r["live_verified"]), ("OPEN", True))

    def test_historical_snapshot_never_authorizes_current_preparation(self):
        o = {"role_key": "target", "ref": "test", "authority_for_role": True,
             "inspected_original": True, "observed_at": "2026-09-10", "status": "OPEN"}
        a = ready_input()
        a["source_status"] = g.resolve_status("target", [o], "2026-09-10")
        self.assertEqual(g.preparation_gate(a)["gate"], "PREPARATION_HOLD")

    def test_F_packet_retains_human_AI_team_and_aggregate_boundary(self):
        p = packet()
        self.assertEqual(g.packet_errors(p, EVIDENCE), [])
        self.assertEqual(p["change_events"], CASES["F"]["expected"]["individual_change_events"])
        for field in ("ai_contribution", "human_contribution", "team_contribution"):
            self.assertTrue(p[field]["refs"])

    def test_F_no_invented_nine_events_or_new_truth_source(self):
        p = packet()
        p["change_events"] = ["invented event"] * 9
        self.assertTrue(g.packet_errors(p, EVIDENCE))
        p = packet()
        p["truth_source"] = True
        self.assertTrue(g.packet_errors(p, EVIDENCE))

    def test_F_packet_requires_trigger_completed_evidence_and_unknowns(self):
        p = packet()
        p["trigger"] = "EVERY_APPLICATION"
        self.assertTrue(g.packet_errors(p, EVIDENCE))
        p = packet()
        p["human_contribution"]["refs"] = ["paw-active"]
        self.assertTrue(g.packet_errors(p, EVIDENCE))
        p = packet()
        del p["real_feedback"]
        self.assertTrue(g.packet_errors(p, EVIDENCE))

    def test_F_engineering_and_commercial_claims_fail_verified_scope(self):
        e = {"e": {"resume_use_boundary": "ALLOWED"}}
        facts = {"f": {"evidence_id": "e", "verified": True, "source_location": "test-only-fact",
                       "supported_capabilities": ["AI-assisted prototype"]}}
        c = {"requirement_id": "r", "evidence_id": "e", "fact_id": "f", "text": "test-only claim",
             "scope_reviewed": True, "asserted_capabilities": ["AI-assisted prototype"]}
        self.assertEqual(g.claim_errors(c, {"r"}, e, facts), [])
        for unsupported in CASES["F"]["unsupported_claims"]:
            c["asserted_capabilities"] = [unsupported]
            self.assertTrue(g.claim_errors(c, {"r"}, e, facts))

    def test_missing_metadata_does_not_prevent_bounded_analysis(self):
        original = {"source_location": "inspected section"}
        result = g.normalized_evidence(original)
        self.assertEqual(result["metric_scope"], "UNKNOWN")
        self.assertEqual(original, {"source_location": "inspected section"})

    def test_positive_match_without_evidence_is_rejected(self):
        r = {"hierarchy": "MUST", "match_level": "SUPPORTED", "supported_scope": "prototype", "evidence_refs": []}
        self.assertTrue(g.match_errors(r, EVIDENCE))

    def test_unknown_and_unsupported_are_distinct_valid_results(self):
        for level in ("UNKNOWN", "UNSUPPORTED"):
            self.assertEqual(g.match_errors({"hierarchy": "MUST", "match_level": level}, {}), [])

    def test_qualification_no_checks_missing_refs_or_ambiguous_requirement(self):
        self.assertEqual(g.qualification([], True), "VERIFY")
        self.assertEqual(g.qualification(eligible_checks(), False), "VERIFY")
        self.assertEqual(g.qualification([{"hierarchy": "MUST", "result": "PASS"}], True), "VERIFY")
        self.assertEqual(g.qualification([{"hierarchy": "UNKNOWN / AMBIGUOUS"}], True), "VERIFY")

    def test_verified_mandatory_failure_wins_without_erasing_capability(self):
        checks = eligible_checks()
        checks[0]["result"] = "FAIL"
        self.assertEqual(g.qualification(checks, True), "NOT ELIGIBLE")
        self.assertEqual(g.match_errors(CASES["A"]["requirements"][0], EVIDENCE), [])

    def test_partial_window_overlap_unknown_and_disjoint(self):
        self.assertEqual(g.window_match("2026-12-01", "2027-01-31", "2027-01-01", "2027-12-31"), "VERIFY")
        self.assertEqual(g.window_match("UNKNOWN", "2027-01-31", "2027-01-01", "2027-12-31"), "VERIFY")
        self.assertEqual(g.window_match("2026-01-01", "2026-02-01", "2027-01-01", "2027-12-31"), "NOT ELIGIBLE")

    def test_work_style_sales_is_separate_from_interview_and_collaboration(self):
        neutral = [{"signal": x, "core_daily": True} for x in ("stakeholder_meeting", "user_interview", "cross_functional", "internal_presentation", "product_explanation")]
        self.assertEqual(g.work_style(neutral, ["group_assessment", "case_interview", "impromptu_presentation"])["work_style"], "NO_NEGATIVE_SIGNAL")
        for signal in g.SALES:
            self.assertEqual(g.work_style([{"signal": signal, "core_daily": True}], [])["work_style"], "LOW")
            self.assertEqual(g.work_style([{"signal": signal, "core_daily": False}], [])["work_style"], "NO_NEGATIVE_SIGNAL")
        self.assertEqual(g.work_style([], [])["work_style"], "UNKNOWN")

    def test_all_ten_dimensions_and_no_unexplained_percentage(self):
        a = {"dimensions": {d: {"rationale": "Fixture rationale"} for d in g.DIMENSIONS}, "recommendation": "Explore"}
        self.assertEqual(g.assessment_errors(a), [])
        a["match_percentage"] = 87
        self.assertTrue(g.assessment_errors(a))
        del a["match_percentage"]
        del a["dimensions"]["Eligibility Fit"]
        self.assertTrue(g.assessment_errors(a))

    def test_preparation_rejects_closed_unqualified_missing_identity_or_critical_unknown(self):
        for patch in [{"role_key": "UNKNOWN"}, {"qualification": "VERIFY"}, {"qualification": "NOT ELIGIBLE"},
                      {"evidence_justifies_preparation": False}, {"critical_unknowns": ["hard start-date condition"]},
                      {"recommendation": "Explore"}, {"source_status": {"status": "CLOSED", "live_verified": True}}]:
            a = {**ready_input(), **patch}
            self.assertEqual(g.preparation_gate(a)["gate"], "PREPARATION_HOLD")
        self.assertEqual(g.preparation_gate(ready_input())["gate"], "READY_FOR_REVIEW")

    def test_claim_requires_chain_and_separate_resume_public_permissions(self):
        c = {"requirement_id": "r", "evidence_id": "dneg-workflow", "fact_id": "missing", "text": "polished wording"}
        self.assertTrue(g.claim_errors(c, {"r"}, EVIDENCE, {}))
        e = {"e": {"resume_use_boundary": "ALLOWED", "public_use_boundary": "UNKNOWN"}}
        f = {"f": {"evidence_id": "e", "verified": True, "source_location": "test-only", "supported_capabilities": []}}
        c.update(evidence_id="e", fact_id="f", scope_reviewed=True)
        self.assertEqual(g.claim_errors(c, {"r"}, e, f), [])
        self.assertTrue(g.claim_errors(c, {"r"}, e, f, public=True))

    def test_preparation_cannot_borrow_other_job_authority_or_omit_constraint_checks(self):
        a = ready_input()
        a["source_status"]["role_key"] = "another-job"
        self.assertEqual(g.preparation_gate(a)["gate"], "PREPARATION_HOLD")
        for key in ("critical_unknowns", "one_active_application"):
            a = ready_input()
            del a[key]
            self.assertEqual(g.preparation_gate(a)["gate"], "PREPARATION_HOLD")

    def test_skill_frontmatter_is_valid_minimal_plain_scalar_subset(self):
        # Dependency-free check for this file's deliberately tiny YAML subset;
        # does not pretend to replace a general YAML parser or bundled validator.
        text = (ROOT / "SKILL.md").read_text()
        front = re.fullmatch(r"---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: ([^\n]+)\n---\n[\s\S]*", text)
        self.assertIsNotNone(front)
        name, description = front.groups()
        self.assertLessEqual(len(name), 64)
        self.assertTrue(0 < len(description) <= 1024)
        self.assertNotRegex(description, r"[:][ ]|[ ]#|[<>]|\[TODO:")

    def test_fixture_provenance_and_portable_document_links(self):
        for c in CASES.values():
            self.assertIs(c["test_only"], True)
            self.assertTrue(c["source_refs"])
        for path in ROOT.rglob("*.md"):
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if not link.startswith(("https:", "http:", "#", "/")):
                    self.assertTrue((path.parent / link.split("#")[0]).exists(), (path, link))

    def test_original_local_sources_unchanged_when_available(self):
        for item in read("source-manifest.json").values():
            path = Path(item["path"])
            if path.exists():
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item["sha256"], str(path))


if __name__ == "__main__":
    unittest.main(verbosity=2)
