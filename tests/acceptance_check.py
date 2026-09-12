"""Final patch checks, separate from the unchanged 33-test regression suite."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load_module("core_validator", ROOT / "scripts/validate.py")
g = load_module("core_guard", ROOT / "scripts/guard.py")
VALID = "---\nname: career-intelligence\ndescription: Analyse supplied jobs for review.\n---\nBody\n"


class ValidatorAcceptance(unittest.TestCase):
    def test_valid_frontmatter(self):
        self.assertEqual(v.frontmatter_errors(VALID), [])

    def test_duplicate_missing_and_unknown_keys_fail(self):
        for text in (VALID.replace("description:", "name: duplicate\ndescription:"),
                     VALID.replace("name: career-intelligence\n", ""),
                     VALID.replace("description:", "metadata: invalid\ndescription:")):
            self.assertTrue(v.frontmatter_errors(text))

    def test_unsupported_yaml_fails_explicitly(self):
        for scalar in ("true", "123", "|", ">", "&anchor text", "*anchor", "[a, b]",
                       "{a: b}", '"quoted"', "hello # comment", "hello: world", "null",
                       "2026-09-12", "1e3", ".nan", "trailing:"):
            with self.subTest(scalar=scalar):
                text = VALID.replace("Analyse supplied jobs for review.", scalar)
                self.assertTrue(v.frontmatter_errors(text))

    def test_length_name_and_scaffold_fail(self):
        for text in (VALID.replace("career-intelligence", "Career--Invalid"),
                     VALID.replace("Analyse supplied jobs for review.", "x" * 1025),
                     VALID + "[TODO: unfinished]\n"):
            self.assertTrue(v.frontmatter_errors(text))

    def test_fences_fail_closed(self):
        self.assertTrue(v.frontmatter_errors("name: career-intelligence"))
        self.assertTrue(v.frontmatter_errors(VALID.replace("---\nBody", "Body")))

    def test_local_link_resolution_and_no_network_dependency(self):
        # Ephemeral test workspace is inside this Core and is removed on exit.
        with tempfile.TemporaryDirectory(prefix=".validator-check-", dir=ROOT / "tests") as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text(VALID + "[missing](rules/evidence.md)\n[web](https://example.invalid/unread)\n")
            errors, count = v.validate(root)
            self.assertEqual(count, 1)
            self.assertTrue(errors)
            (root / "rules").mkdir()
            (root / "rules/evidence.md").write_text("Evidence rule\n")
            self.assertEqual(v.validate(root), ([], 1))

    def test_actual_core(self):
        self.assertEqual(v.validate(ROOT)[0], [])


def run_tencent_guards():
    """Execute guards on fixture inputs; no READY defaults or synthetic facts.

    The agent performs semantic workflow execution in the readable artifact.
    This function corroborates the structured match and preparation boundaries.
    """
    case_path = ROOT / "tests/fixtures/A-tencent.json"
    evidence_path = ROOT / "tests/fixtures/evidence-excerpts.json"
    case = json.loads(case_path.read_text())
    case.pop("expected", None)  # Expected outcomes are not decision inputs.
    evidence = json.loads(evidence_path.read_text())["evidence"]
    matches = [g.match_errors(row, evidence) for row in case["requirements"]]
    if any(matches):
        raise AssertionError(matches)
    # Historical user confirmation is retained, but no original current JD or
    # qualification checks are present in this privacy-safe fixture.
    current_qualification = g.qualification([], coverage_complete=False)
    source_status = g.resolve_status(case["role_key"], [], case["as_of"], case["mode"])
    analysis = {"role_key": case["role_key"], "qualification": current_qualification,
                "source_status": source_status, "evidence_justifies_preparation": True,
                "recommendation": "Explore", "one_active_application": "UNKNOWN",
                "critical_unknowns": ["current authority JD/status/qualifications", "original fact and CV Base references"]}
    gate = g.preparation_gate(analysis)
    result = {"mode": case["mode"], "as_of": case["as_of"], "role_key": case["role_key"],
              "historical_qualification": case["historical_qualification"],
              "current_qualification": current_qualification, "current_source_status": source_status,
              "matched_requirement_count": len(matches), "match_errors": matches,
              "recommendation": analysis["recommendation"], "preparation_result": gate,
              "cv_strategy_count": 1, "claim_candidates": [], "packet": None,
              "input_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (case_path, evidence_path)}}
    assert current_qualification == "VERIFY" and gate["gate"] == "PREPARATION_HOLD"
    print("TENCENT GUARD EXECUTION (agent-readable artifact is separate):")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ValidatorAcceptance)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    run_tencent_guards()
