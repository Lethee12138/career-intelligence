# Core Integration — accepted Core delivery

Status: `CAREER_INTELLIGENCE_V01_CORE_INTEGRATION_ACCEPTED`. Human Review returned ACCEPT for the delivered Core and its documented limitations. The authorized local durable checkpoint is `CAREER_INTELLIGENCE_V01_CORE_ACCEPTED`; no push or next-stage execution is authorized.

Accepted baselines verified: Slice 1 `29a9c7930b4e1668879ab30689c47c38626fcb8d`; Slice 2 / pre-checkpoint main HEAD `083ee7b37dad01debc9095f65cd53280811eb59a`. Both annotated tags retain their accepted targets. Worktree and index were clean before this increment. Historical DELIVERY records remain unchanged.

## Existing first and exact reuse

Existing rules already express Evidence gap vs Capability gap, scoped PARTIAL matches, Strategic Stretch recommendations, four capability epistemic states, questioning stops and strong fact/ownership boundaries. These are retained. The missing part was an independent claim/use boundary with an explainable transfer mechanism and interview defensibility, plus an explicitly bounded way to review strategic wording against a frozen role while live preparation remains on HOLD.

Reused unchanged:

- `rules/evidence.md`, `rules/eligibility.md`, `rules/opportunity-assessment.md`, `rules/source-and-inference.md`, `rules/user-questioning.md`, `rules/discovery.md`.
- `schemas/capability-profile.md`, `schemas/role-hypothesis.md` — no new capability or hypothesis system.
- `scripts/guard.py`, `scripts/discovery_guard.py`, `scripts/validate.py` — no new matching engine or changed live gate.
- `tests/test_core.py`, `tests/test_discovery.py`, `tests/acceptance_check.py` and all accepted fixtures. Direct case inputs: `tests/fixtures/A-tencent.json`, `B-kuaishou-user.json`, `evidence-excerpts.json`, `slice2-cases.json`, `source-manifest.json`. No expected-result fields were used as decision inputs.
- `tests/README.md`, `tests/SLICE2.md`, both accepted Human Review artifacts, `DELIVERY.md`, `SLICE2_DELIVERY.md`, `SOURCES.md`, `LICENSES.md`, `reuse-matrix.md` remain historical records/reference context; no new upstream audit.
- External read-only evidence: registered OUTPUT §2, BATCH product/usability rows, DNEG_IMPLEMENTATION note; other project patterns reuse the accepted minimal Slice 2 excerpts.

## Exact changed / added files

Changed (7):

1. [SKILL.md](SKILL.md) — shared policy entry point for all four workflows.
2. [rules/cv-claims.md](rules/cv-claims.md) — bridge to the new use boundary and strongest truthful framing.
3. [schemas/contracts.md](schemas/contracts.md) — minimal claim/use and historical framing_review extension; original schemas retained.
4. [workflows/position.md](workflows/position.md) — adjacent potential use guidance.
5. [workflows/discover.md](workflows/discover.md) — stretch expands hypotheses without promoting epistemic status.
6. [workflows/analyse-job.md](workflows/analyse-job.md) — PARTIAL + DEFENSIBLE_STRETCH remains distinct from SUPPORTED and gaps.
7. [workflows/prepare-application.md](workflows/prepare-application.md) — L1–L3 and explicitly requested internal historical wording review.

Added (6):

1. [rules/stretch.md](rules/stretch.md) — one cross-workflow increment, not a second evidence system.
2. [scripts/stretch_guard.py](scripts/stretch_guard.py) — pure checks for reviewed bridges, immutable hard-fact atoms and trace edges.
3. [tests/test_stretch.py](tests/test_stretch.py) — focused A–F and integration counterfactuals.
4. [tests/outputs/core-integration-human-review.md](tests/outputs/core-integration-human-review.md) — complete readable four-workflow execution.
5. [tests/outputs/core-integration-trace.json](tests/outputs/core-integration-trace.json) — task-local structured output/handoff record with source hashes, not a new evidence owner.
6. This `CORE_INTEGRATION_DELIVERY.md`.

## Policy representation and gate reconciliation

The original four epistemic statuses are unchanged. `use_boundary` independently expresses VERIFIED_FACT / DEFENSIBLE_STRETCH / SPECULATIVE_UNSUPPORTED. Each stretch records source capabilities/evidence, bridge, unproven scope, allowed use, prohibited overclaim, ownership and L1 What / L2 Transfer / L3 Boundary. Categorical language only; no confidence numbers or majority scoring. Hard facts, material ownership contradictions and invented credentials cannot be voted away by other positive signals.

VERIFIED_FACT is scoped to the actual proposition verified. A directly read report's contents are a documentary fact, not verification of the reported candidate achievement. The current case therefore does not invent a DEMONSTRATED capability to populate a section. Report-derived INFERRED behaviors can still support honest conditional potential framing.

The earlier default HOLD contract excluded tailored claims. The Human's explicit historical integration request now permits a separate `framing_review`, NOT_FOR_ADOPTION, with wording comparisons and L1–L3 notes. This is a narrow semantic extension, recorded explicitly rather than silently bypassing the old rule. Live preparation checks stay unchanged; under HOLD, claim_candidates remains empty and packet remains null. No permission or formal qualification is supplied by a stretch bridge.

## Complete chain result

Kuaishou was inspected first but lacks exact job ID/URL. Tencent fallback preserves `Tencent:1283126456553382912:2027` through analysis and preparation. Role snapshot is historical/frozen at 2026-09-11; no employer freshness check or online activity.

- C-CORE-01 /position: repeated product/workflow and test-iteration patterns remain INFERRED; AI product/evaluation targets remain POTENTIAL with DEFENSIBLE_STRETCH. No prior PM title required. Directly verified personal capability list remains empty with explanation.
- D-CORE-01 /discover: Research-led Product Discovery, Workflow/Product Ops, Applied AI Product/HITL and Game Systems hypotheses; source-capability bridges, multiple industries, search terms and counterevidence. PM is neither sole nor automatically first. Route B explicitly lacks qualified inputs.
- A-TENCENT-CORE-01 /analyse-job: scoped prototype workflow SUPPORTED; product-data PARTIAL + DEFENSIBLE_STRETCH for evaluation questions/validation plans. SQL/A-B/commercial analytics are still unsupported subclaims. Historical ELIGIBLE is preserved; current qualification VERIFY and exact team/HC remain UNKNOWN. The data gap weakens the full-scope PM version, not the underlying capabilities. No fabricated Tencent hard-JD contradiction.
- P-TENCENT-CORE-01 /prepare-application: Explore / PREPARATION_HOLD from the existing guard. One targeted strategy, DNEG-first and a small alternate project route, strongest truthful wording and honest recruiter bridges. Internal framing review only; no CV, packet, adopted claims or submissions.

Five reverse traces in the artifact and JSON:

1. Documentary simulated-default fact → technical boundary → application-layer hypothesis → profile source context → dneg-runtime / implementation note.
2. DNEG-first framing → bounded workflow assessment → AI/workflow hypothesis → INFERRED pattern → dneg-ownership / OUTPUT, plus cross-context refs.
3. Evaluation bridge answer → product-data PARTIAL → evaluation hypothesis → test-iteration pattern → dneg-testing / BATCH.
4. Excluded SQL/A-B/commercial claims → explicit gap → narrower hypothesis → evidence-coverage gap → dneg-testing.
5. NOT_FOR_ADOPTION / CV VERIFY → readiness/evidence assessment → no hypothesis grants permission → profile source/permission context → dneg-workflow UNKNOWN permission. Exact CV source/version is an explicitly unresolved external link, not a fabricated completed chain.

All five internal chains resolve; direct Master Evidence, exact frozen CV and current authority links remain limited or broken as named. A trace to a report does not certify the reported achievement.

## Verification and scope of proof

Run from this repository with standard-library Python:

```sh
python3 -I -S -B scripts/validate.py
python3 -B -m unittest discover -s tests -p test_core.py -v
python3 -B -m unittest discover -s tests -p test_discovery.py -v
python3 -B -m unittest discover -s tests -p test_stretch.py -v
python3 -B tests/acceptance_check.py
```

Results: dependency-free validator PASS; Slice 1 **33/33 PASS**; Slice 2 **19/19 PASS**; focused Core/Stretch **13/13 PASS**; existing acceptance checks **7/7 PASS**, Tencent default remains HOLD. Existing tests/fixtures were not altered to pass. Git diff/whitespace checks PASS. Protected-source hash comparison: 18/18 unchanged against this turn's pre-edit snapshot; no assertion of having hashed all PAW or unavailable Master Evidence files.

Focused coverage: tool-only engineering inflation, positive adjacent potential without prior title, exact metric/scope preservation, prototype vs entire-project ownership, technical-stack overclaim rejection, PARTIAL stretch vs unsupported bridge, L1–L3, vetoing direct counterevidence/credential inventions, all hard-fact categories, broken trace/identity edges, documentary fact scope, frozen input hashes and no live gate bypass.

This agent executed the four Markdown workflows, authored the corresponding semantic report and manually grounded the structured handoffs. Actual Python calls verified match rows, preparation gate, use-boundary structure and five trace chains. Tests exercise reviewed assertions/atoms, not natural-language entailment or automatic source extraction; source review is still necessary. No independent-model benchmark or live READY-path is claimed.

## Human UX and evidence inflation review

The opening recommends a concrete product/workflow strategy, not an audit task list. Professional phrasing strengthens tool-centric language into product decisions and prototype iteration, with a defensible ownership verb. Potential gets visible positive treatment and no formal PM title gate. The preparation section groups the shared non-adoption boundary once, then uses concise wording comparisons and L1–L3 internally instead of placing a caveat after every sentence.

Gaps stay decision-specific: commercial analytics is not supplied by qualitative testing; technical identity is not supplied by AI-assisted build. The report gives one Base route and bounded project selection, not an application bundle. No questions or default exercises were needed. Source/trace sections are denser than the strategy opening and remain available for review; Human Review subsequently accepted this delivered result.

Inflation checks rejected the deliberate negative examples (percent gains, whole-project leadership and engineering credentials). No such claim entered the final candidate strategy. During review, the potentially ambiguous “VERIFIED_FACT” example was scoped explicitly to documentary contents, and “improved usability significantly” was marked an unsupported wording counterexample, not a historical achievement. The strong ownership sentence remains conditional on the inspected report's attribution and future original/permission verification. No factual expansion was used to make the output competitive.

## Remaining limits and disposition

Current JD freshness, full raw JD coverage, exact Master Evidence/frozen CV, CMK authority and DNEG per-event trace remain unfilled. This case has only two normalized requirements; it cannot establish complete current employer fit. The verified fact is a narrow document fact, not direct proof of personal skill. Current market validation/READY path and independent-model benchmark remain untested. Upstream implementations remain independently unaudited.

Human ACCEPT supersedes the earlier review-ready handoff. Core acceptance does not certify current submission readiness or independently verify real-world candidate facts. No source CV, Career record, PAW, adapter, external account or historical accepted tag was changed.

Checkpoint changes only record acceptance and clarify the Human-confirmed VERIFIED_FACT definition: current input Evidence directly supports the proposition; independent real-world verification is not implied. DEFENSIBLE_STRETCH cannot become a hard fact, genuine gaps remain gaps and UNKNOWN remains UNKNOWN. Tests and the accepted workflow implementation are otherwise preserved.

Local checkpoint: branch `main`, commit message `Accept Career Intelligence v0.1 Core`, annotated tag `career-intelligence-v0.1-core-accepted-20260912`. Resolve its exact target from the tag; commit identity and post-commit cleanliness are reported after creation.

Checkpoint verification: dependency-free validator PASS; Slice 1 33/33; Slice 2 19/19; existing acceptance 7/7; Core/Stretch 13/13; protected source hashes 18/18 unchanged; whitespace and temporary-file/scope checks PASS.

No push, Codex Adapter, PAW integration, scanner, monitoring, dashboard or application submission. Job Quality & Offer Preference Profile remains a separately requested future stage, not started here.

`CAREER_INTELLIGENCE_V01_CORE_ACCEPTED`
