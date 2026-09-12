# Slice 2 delivery — accepted

Status: `CAREER_INTELLIGENCE_V01_SLICE2_ACCEPTED`. Human Review explicitly returned ACCEPT on 2026-09-12 for the delivered Slice 2 scope and its documented limitations. Scope is /position, /discover, their semantic contracts, minimal structured guards, privacy-safe fixtures and bounded reuse integration. This record accompanies the authorized local durable checkpoint; no push is authorized.

Baseline verified before edits: main at `29a9c7930b4e1668879ab30689c47c38626fcb8d`; accepted annotated tag `career-intelligence-v0.1-slice1-accepted-20260912` peels to that commit; working tree was clean. Slice 1 acceptance is preserved.

## Existing owners reused unchanged

- `workflows/analyse-job.md`, `workflows/prepare-application.md`: actual-job qualification, ten-dimensional assessment, recommendations and preparation gates.
- `schemas/contracts.md`: common claim/reference, evidence, match and application contracts. No synonym evidence schema.
- `rules/evidence.md`, `rules/source-and-inference.md`: source trace, ownership and epistemic boundaries.
- `rules/eligibility.md`, `rules/opportunity-assessment.md`: degree vs role, mandatory vs preference, work-style, practical fit and no composite scores.
- `rules/user-questioning.md`, `rules/cv-claims.md`: existing-first material questions, Human Review and claim restrictions.
- `scripts/guard.py`: shared qualification/work-style boundaries; `scripts/validate.py`: dependency-free canonical validator.
- `tests/test_core.py`, `tests/acceptance_check.py`, `tests/README.md`, `tests/walkthroughs.md`, all eight original JSON fixtures including source-manifest, and `tests/outputs/tencent-final-human-review.md`: accepted Slice 1 checks/provenance retained.
- `DELIVERY.md`, `SOURCES.md`, `LICENSES.md`: historical acceptance and source/license boundaries retained.

## Exact changed and added files

Changed:

1. [SKILL.md](SKILL.md): route four commands; link Slice 2 rules and verification without altering Slice 1 workflow behavior.
2. [reuse-matrix.md](reuse-matrix.md): append Human-supplied bounded pattern decisions; preserve earlier audit history.

Added:

1. [rules/discovery.md](rules/discovery.md)
2. [schemas/capability-profile.md](schemas/capability-profile.md)
3. [schemas/role-hypothesis.md](schemas/role-hypothesis.md)
4. [workflows/position.md](workflows/position.md)
5. [workflows/discover.md](workflows/discover.md)
6. [scripts/discovery_guard.py](scripts/discovery_guard.py)
7. [tests/fixtures/slice2-cases.json](tests/fixtures/slice2-cases.json)
8. [tests/test_discovery.py](tests/test_discovery.py)
9. [tests/SLICE2.md](tests/SLICE2.md)
10. [tests/outputs/slice2-discovery-review.md](tests/outputs/slice2-discovery-review.md)
11. This `SLICE2_DELIVERY.md`.

Separate report templates were unnecessary: the semantic contracts specify readable report order and required fields. No database, scanner, ontology store, API, integration or new dependency was added.

## Implementation and reuse

/position reads existing evidence without a JD, inventories completed outputs with Human/AI/team contributions, deduplicates bounded capabilities, counter-checks seed roles and produces a small role hypothesis pool. It distinguishes SELF_IDENTIFIED, DEMONSTRATED, INFERRED and POTENTIAL as epistemic statuses with STRONG/MODERATE/TENTATIVE confidence. Hidden patterns require traceable owned behavior across distinct contexts or a justified unusually strong single record.

/discover supports seed-role, explicit-capability, hidden-capability and problem-first bridges. The Output-first lens applies across routes. Each hypothesis requires actual work, supports, counters, gaps, preference risks, multiple industries/teams and core/adjacent/responsibility/problem/output/negative search terms. It works offline without exact titles and does not automatically search. Supplied market evidence appends scoped validation observations, preserving the original family hypothesis. Current original JD validation is distinct from historical reported contradictions and never bypasses /analyse-job.

The capability and role contracts reuse the original claim/reference model. A profile is a review candidate, not durable evidence. An unvalidated hypothesis is not a role recommendation. Optional ESCO/O*NET vocabulary cannot establish skills, current hiring, China demand or eligibility.

Reuse Matrix adaptations: ai-job-search existing-first/dedup/source-trace/inference/Human review; resume-tailoring dynamic branching/cross-experience recall/low-information stop. Existing Slice 1 job evaluation concepts are reused without a duplicate scoring layer. Syllabus/toolchain inflation, public-profile scanning, web enrichment as personal truth, automatic profile growth, percentages, weighted scores, rigid location gating and trivial-story mining are dropped. ESCO/O*NET remain vocabulary only; career-ops remains LATER. All these are Human-supplied bounded findings, not independent upstream implementation/license verification.

## Verification

- Canonical validator: `python3 -I -S -B scripts/validate.py` — PASS using only Python standard library; validator unchanged; 73 local file links checked.
- Original Slice 1 regression: 33/33 PASS, original tests and fixtures unchanged.
- Slice 2 structured boundary regression: 19/19 PASS (52/52 total with the original 33). A–J mapping and the distinction between automated checks and semantic obligations are in [test protocol](tests/SLICE2.md).
- Existing validator acceptance: 7/7 PASS; Tencent guard remains PREPARATION_HOLD with one strategy and no claims/packet.
- Protected local sources: SHA-256 comparison of 18 registered reports, Career/candidate documents and CV files against this turn's pre-edit snapshot — 18 unchanged. The original seven-source manifest check also passes. This is bounded file verification, not a claim to have hashed every file in PAW or every inaccessible Master Evidence owner.
- Accepted Slice 1 workflows, contracts, rules, guard, validator, tests, fixtures and historical records: Git comparison against the accepted commit shows no changes.

## Evidence and intentional limits

No conflict with the inspected Career SSOT was found. The historical AR research contribution remains usable under completed-only evidence, without rewriting later AR production or attributing team visual work to the candidate. Active PAW/Portfolio work is excluded from the fixture.

The five project cases are historical report-derived excerpts, not new direct Master Evidence verification. Stable product/workflow/HITL capabilities can be represented safely as bounded INFERRED hypotheses; no DEMONSTRATED capability is invented from these reports. Single tool/course signals remain POTENTIAL. Candidate motivation for choosing PM remains UNKNOWN where not explicitly supplied. Software engineering, high-craft design, clinical expertise, commercial results and Agent/RAG expertise cannot be safely inferred from these inputs.

The real OPPO case supplies a historical report of an exact JD with a technical-major mismatch, so its CONTRADICTED state is scoped to that historical/reported job. The original current JD was not reread. A clearly SYNTHETIC positive current-JD control tests the authority branch; it does not satisfy real-time validation. A fresh-context execution can test instruction behavior but is not an independent-model benchmark or proof of semantic entailment.

Exact Master Evidence/frozen CV access, missing CMK authority snapshot and incomplete DNEG per-event test-to-change trace remain unchanged limitations. No real-time READY-path validation, independent-model benchmark, Codex Adapter, PAW integration, scanner, monitoring, auto-apply, dashboard, external search, login, outreach, CV edit or external submission was performed. No capability or hypothesis was durably adopted.

## Behavioral execution and UX findings

A fresh-context agent was given only the Skill, raw fixture and linked contracts/source metadata, with no tests, expected answer or prior conclusions. It ran /position → /discover and wrote `/tmp/career-slice2-trial/report.md`. The reviewed repository copy is [Slice 2 discovery review](tests/outputs/slice2-discovery-review.md). It explicitly records the subsequent editorial changes; it is not presented as an untouched benchmark output.

Observed behavior: completed output inventory, four traceable INFERRED capabilities, PM support/counters, cross-industry responsibility hypotheses and per-hypothesis search strategies. Route B correctly remained unavailable rather than inventing a direct user claim or DEMONSTRATED capability. A–J semantic review also checks title traps, normal collaboration vs revenue, MT and historical job-scoped contradiction. The primary review added compact Workflow Ops, Game Systems and Applied AI Product/HITL evaluation variants so those responsibility possibilities and their gaps are visible without inventing additional verified capabilities.

One evidence inflation risk was observed: the draft labelled personal high-fidelity visual craft POTENTIAL even though the cited output was primarily another team member's. The minimal correction removes that positive signal, clarifies in discovery rules that even POTENTIAL needs candidate-attributable evidence, and adds an adversarial regression. The added regression passes in the final **19/19 Slice 2 tests**. No other evidence inflation was found in the reviewed artifact; this is a scoped semantic review, not proof that future model executions cannot inflate claims.

UX: the report leads with a bounded conclusion and puts counters beside each hypothesis. Source metadata is relatively dense but grouped once; some boundary reminders recur around market validation and next steps, with no obvious contradictory or mechanically repeated rules block. UNKNOWN is concentrated on inaccessible originals, ownership and current JD coverage, rather than filling every conclusion with an undifferentiated unknown. No user questions were asked; the existing evidence sufficed for a bounded result. The Human can select a responsibility direction and supply one relevant current JD; there is no premature application recommendation, CV bundle or new project assignment. Preparation remains outside this discovery output and under the existing Slice 1 gates.

Final diff/whitespace checks PASS.

Final disposition: Human ACCEPT supersedes the prior `CAREER_INTELLIGENCE_V01_SLICE2_HUMAN_REVIEW_READY` handoff. The accepted implementation and tests are unchanged during checkpoint creation; only this delivery status is updated.

Checkpoint: branch `main`; annotated tag `career-intelligence-v0.1-slice2-accepted-20260912` targets the final acceptance commit containing this record. Resolve the exact commit from that tag; its hash is reported after commit creation. The Slice 1 accepted tag is preserved.

Checkpoint verification: dependency-free validator PASS; Slice 1 33/33 PASS; Slice 2 19/19 PASS; acceptance checks 7/7 PASS. Post-commit worktree/index cleanliness and tag identity are verified and reported separately.

Known limitations remain accepted without invented evidence: incomplete direct Master Evidence/frozen CV access, historical OPPO contradiction only, synthetic current-JD control, no independent model benchmark, and upstream implementations not independently audited.

No push, Codex Adapter, PAW integration or Core Integration Acceptance execution is part of this checkpoint. The latter is a separate future task.

`CAREER_INTELLIGENCE_V01_SLICE2_ACCEPTED`
