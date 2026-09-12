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
