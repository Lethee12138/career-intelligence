# Reuse Matrix — Slice 1

Method-level reuse only; no external code, assets, installs or execution. Decisions below derive from the supplied request and inspected Career canonical §15.3 / method note's 2026-09-12 increment. No external repository identity, license or latest implementation is claimed verified.

| Existing source / sample | Decision | Scope / disposition |
|---|---|---|
| Current Career canonical / evidence / CV owners | REUSE | Read-only rules and exact references; no new fact owner or application tracker |
| ai-job-search | INSPIRE — NOT AUDITED IN THIS SLICE | Comparison sample only; upstream identity, revision, implementation, features and license not verified here. Not a verified reusable implementation or dependency |
| resume-tailoring-skill | INSPIRE — NOT AUDITED IN THIS SLICE | Comparison sample only; upstream identity, revision, implementation, features and license not verified here. Tailoring follows the accepted Career claim chain, not audited upstream code |
| career-ops | LATER | Tool/operations layer reference only; tracker/automation/dashboard outside Slice 1 |
| resume-evidence-workflow | ADAPT | Selective deep dive, information gain/stop rules, metric correction vs snapshot vs scope clarification, reference indexing; implemented in evidence/questioning rules |
| resume-evidence-workflow | DROP | Second Evidence Bank, second Base Resume lifecycle, automatic evidence writeback without current Human Review |
| tailor-job-application-skill | ADAPT | Requirement → evidence → gap, structured interview follow-up/risk, untrusted external-input boundary |
| tailor-job-application-skill | DROP | Second HTML dashboard, browser-local tracker as SSOT, replacement CV templates, mandatory full application package per role |
| Portable rules/workflows/guard | BUILD | Original minimal implementation of the user-approved requirements; guard enforces explicit structured boundaries, not semantic matching |

Allowed vocabulary: REUSE / ADAPT / INSPIRE / BUILD / DROP / LATER. INSPIRE for the first two names is a conservative implementation decision, not a claim that an earlier audit adopted specific upstream code. Upstream audit can be separately requested later; it is not needed to execute this standalone Core.

Audit status is separate from the reuse decision. The explicit suffix above means no upstream implementation audit in this Slice, including the final acceptance patch. ADAPT/DROP rows preserve accepted method-level decisions from Career sources; they do not imply a fresh upstream code or license audit. `career-ops = LATER` is unchanged. No online audit or installation was performed in this patch.

## Slice 2 — supplied bounded pattern findings

Provenance: Human-supplied completed Pattern Scan in the Slice 2 request, 2026-09-12. The Slice 1 NOT AUDITED entries above are historical. The following is method-level adaptation from that bounded input, not independent upstream implementation, identity, revision or license verification. No web audit, code copying, installation or external execution occurred.

| Sample | Decision | Bounded pattern / implementation location |
|---|---|---|
| ai-job-search /expand | ADAPT | Existing-profile-first, deduplicate, source-trace inference, direct vs inferred, Human review; discovery rules and position workflow |
| ai-job-search /expand | DROP | Syllabus/toolchain capability inflation, automatic profile growth, full public-profile scanning and web enrichment as personal truth |
| ai-job-search Job Evaluation | REUSE | Eligibility before fit, duties over title, career alignment already owned by Slice 1 eligibility/assessment; no duplicate assessment schema |
| ai-job-search Job Evaluation | DROP | Numeric fit dimensions, weighted overall/match percentage, rigid location gate |
| resume-tailoring-skill | ADAPT | Dynamic broad-to-selective branching, cross-experience recall and low-information stop; discovery questioning extends existing rules |
| resume-tailoring-skill | DROP | Percentage confidence, job-count-based leverage as truth, trivial-story mining to fill gaps |
| ESCO / O*NET | INSPIRE | Optional REFERENCE VOCABULARY for occupation/title variants and skills/occupation sanity checking only |
| ESCO / O*NET | DROP | Runtime APIs/datasets/dependency, candidate capability authority, current hiring/China demand/eligibility authority |
| career-ops | LATER | Unchanged; no tracker, operations layer or integration |

Current audit status for ai-job-search and resume-tailoring-skill: BOUNDED PATTERNS SUPPLIED BY HUMAN — UPSTREAM IMPLEMENTATION NOT INDEPENDENTLY AUDITED. Adaptation does not imply reusable verified code.
