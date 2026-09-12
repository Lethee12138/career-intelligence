# Career Intelligence v0.1 — Slice 1 accepted checkpoint

Status: `CAREER_INTELLIGENCE_V01_SLICE1_ACCEPTED`

Human Review completed with explicit `ACCEPT` on 2026-09-12. This accepts the bounded Slice 1 implementation and artifacts; it does not authorize material adoption, external application actions or Slice 2 work.



## Durable acceptance checkpoint — 2026-09-12

Direct user approval: `CAREER_INTELLIGENCE_V01_SLICE1_ACCEPTED`.

Accepted scope: Portable Core; `/analyse-job`; `/prepare-application`; shared contracts/rules; dependency-free validator; Reuse Matrix; regression fixtures; Tencent end-to-end Human Review artifact.

The user explicitly accepts these remaining limitations as boundaries, without requiring them to be solved or filled in Slice 1:

- Exact Master Evidence / frozen CV version access.
- Missing CMK authority snapshot.
- Incomplete DNEG per-event test → change trace.
- No real-time READY-path validation yet.
- No independent model benchmark.

Checkpoint scope is this directory only. It had no existing Git repository; the reviewed 29-file tree is the initial accepted baseline on `main`. The annotated tag `career-intelligence-v0.1-slice1-accepted-20260912` identifies the acceptance commit; resolve the tag through Git rather than embedding a self-referential commit hash in this file. No remote publication is part of this checkpoint.

No Slice 2 work starts here. `/position`, `/discover`, output/capability-first discovery, hidden capability, role hypotheses and market-validation regression belong to a separately authorized next phase. PAW integration remains outside Slice 2.

The final-patch and initial implementation sections below are retained as historical review records. Their pending-review language describes those earlier stages and is superseded by the explicit acceptance above.

## Final acceptance patch — 2026-09-12

Human Review input: `CONDITIONAL ACCEPT / MINOR FIX REQUIRED`. The accepted architecture, workflows, evidence boundaries, guard implementation, six fixtures and original 33 regression tests remain unchanged. This patch is ready for final Human acceptance; it does not record that acceptance on the user's behalf.

### Exact files changed in this patch

Modified (4):

- `SKILL.md` — document the local dependency-free canonical validation command.
- `reuse-matrix.md` — explicit upstream audit status, separate from reuse decisions.
- `tests/README.md` — canonical validation path, separate acceptance command and Tencent artifact link.
- `DELIVERY.md` — this final patch report and Human UX findings; initial delivery retained below as history.

Added (3):

- `scripts/validate.py` — standard-library CLI, usable from any working directory.
- `tests/acceptance_check.py` — seven validator acceptance checks plus execution of existing Tencent decision guards.
- `tests/outputs/tencent-final-human-review.md` — standalone readable execution of both workflows.

No deletions. Current directory contains 29 files. No third-party code/dependency was added. The global/bundled validator was only read, never modified.

### Validator change and actual result

Inspection showed that the old validator's only external need was general YAML loading. This Skill actually uses two single-line plain-string fields, `name` and `description`; nested metadata, quoted/block scalars, anchors, aliases and YAML collections are not needed. The new validator accepts this explicit subset and rejects unsupported syntax rather than attempting a partial general-YAML interpretation. It also checks name/description constraints, duplicate/missing/unknown fields, unfinished scaffold and local Markdown file links. Existing regression frontmatter/link checks are preserved.

Canonical command from the Core: `python3 -B scripts/validate.py`.

Clean-environment verification was actually run from outside the Core: `python3 -I -S -B /Users/luna/Luna/career-intelligence/scripts/validate.py`. **PASS** with Python isolation and site packages disabled. No PyYAML, package manager or installation is required. Enhanced full-YAML validation is optional and outside the default acceptance path. Remote URL health and Markdown anchor existence are not claimed by the local file-link check.

### Reuse audit status

- `ai-job-search`: **INSPIRE — NOT AUDITED IN THIS SLICE**.
- `resume-tailoring-skill`: **INSPIRE — NOT AUDITED IN THIS SLICE**.
- `career-ops`: **LATER**, unchanged.

Upstream identity, revision, features, implementation and license are not marked verified. Method-level ADAPT/DROP decisions remain as accepted; no new online audit or installation occurred.

### Tencent E2E result

Artifact: [Tencent final Human Review](tests/outputs/tencent-final-human-review.md).

The agent read the Skill, all six rules, both workflows and contracts, then used the unchanged privacy-safe Tencent fixture and evidence excerpts to execute `/analyse-job → /prepare-application`. The guard companion independently corroborates the structured boundaries; it is not an LLM or a substitute for semantic review.

Actual result: **historical ELIGIBLE retained; current qualification VERIFY; current source status VERIFY; two evidence matches structurally valid; Explore → PREPARATION_HOLD**. The historical fixture cannot exercise a truthful current READY path. No synthetic OPEN observation, upgraded qualification or company-slot default was inserted. The report supplies the specifically requested conditional CN-P/Product route, DNEG evidence routing, three likely concerns and four verification steps while retaining HOLD. It contains one strategy, zero adoptable CV claims and no Packet or full application package. Fixture input hashes are recorded in the artifact; fixture `expected` values are not decision inputs to the guard execution.

### Human UX check — author review, pending Human acceptance

| Check | Finding and minimal treatment |
|---|---|
| Obvious repetition | No duplicated analysis/brief blocks. HOLD appears in the conclusion and preparation section because it controls two different reading decisions; raw seven-item guard diagnostics are summarized once in ordinary language |
| Mechanical repetition of rules | The report does not reproduce the 15 principles or six rule files. It explains only case-specific ownership, metrics, source and preparation boundaries |
| Unnecessary questioning | No user questions were asked. Three recruiter concerns are explicitly hypothetical interview topics, not a new career interview. Missing documents/site facts become a short verification checklist |
| UNKNOWN clarity / overload | Related missing job fields are grouped; ten required dimensions remain visible. Each blocking unknown maps to a next action. No full metadata dump or fabricated replacement detail |
| Decision usefulness | Supports a concrete keep-and-verify decision for one Tencent direction. Explicitly insufficient to approve an application or adopt CV wording; that limitation follows the fixture's source coverage |
| Bounded preparation | One existing CN-P route, DNEG-based routing, three concerns and four checks. No BG-specific CV variants, cover letter, polished resume bullets, large interview bank or new portfolio work |
| Evidence inflation | None found in the reviewed artifact. Normalized MUST levels are not passed off as freshly verified official requirements; historical eligibility is not promoted to current eligibility; Agent/RAG expertise and commercial metrics are not asserted; 3 rounds/9+ changes remain aggregate reports |

No workflow or core architecture refactor was needed. UX refinement was confined to the standalone output: grouped unknowns, a single decision headline, concise gate reasons and a conditional preparation table.

### Final validation and source protection

- Dependency-free validator: **PASS**, including isolated `-I -S` execution.
- Existing regression: **33/33 PASS**, original `tests/test_core.py` and fixtures unchanged.
- Additional validator acceptance: **7/7 PASS**, reported separately; Tencent guard execution also completed successfully.
- Before/after SHA-256 comparison: **18/18 inspected protected files outside the Core unchanged** (seven registered source copies plus local CV/root DOCX files). This is the measured source-protection scope, not a claim to have hashed every unrelated repository or file on disk.
- All edits and temporary test files stayed within `career-intelligence`; temporary validator fixtures were removed. PAW, Career canonical, Master Evidence and CV sources received no writes. No global Skill/dependency install, network audit, login, submission, push or deployment.

### Remaining limitations and final readiness

The validator intentionally does not parse general YAML or prove semantic entailment. The E2E is an agent-executed historical-fixture HOLD-path run, not independent-model evaluation or a live READY-path job application. Original Master Evidence/CV versions, current employer facts, CMK primary snapshot and DNEG event-level trace retain the previously disclosed limitations. None was filled with invented evidence.

**Slice 1 is ready for final Human acceptance of this bounded implementation and patch.** Final acceptance itself remains Human-owned. `/position`, `/discover` and all Slice 2/integration work remain deferred.

---

## Initial implementation record (retained history)

## Existing First

No existing Career Portable Core was found in the current workspace. Existing method/spec, canonical, Tencent routing, Kuaishou/Baidu operational reports and DNEG records were found and read. The new directory is `/Users/luna/Luna/career-intelligence`; the registered project currently points at `/Users/luna/Luna`, which is not a Git repository. No parallel directory was added to PAW, Portfolio Studio or the global Skill installation path.

## Exact change manifest

The initial implementation added these 26 files relative to this directory. The final patch changes are listed above; this is the historical baseline manifest.

```text
SKILL.md
SOURCES.md
LICENSES.md
reuse-matrix.md
DELIVERY.md
rules/evidence.md
rules/source-and-inference.md
rules/eligibility.md
rules/opportunity-assessment.md
rules/cv-claims.md
rules/user-questioning.md
schemas/contracts.md
workflows/analyse-job.md
workflows/prepare-application.md
scripts/guard.py
tests/README.md
tests/test_core.py
tests/walkthroughs.md
tests/fixtures/source-manifest.json
tests/fixtures/evidence-excerpts.json
tests/fixtures/A-tencent.json
tests/fixtures/B-kuaishou-user.json
tests/fixtures/C-baidu.json
tests/fixtures/D-kuaishou-commerce.json
tests/fixtures/E-stale-source.json
tests/fixtures/F-dneg-packet.json
```

One shared contract replaces four overlapping schema files; it also serves as the report field specification, so separate duplicate templates were not created. Guard code is standard-library-only and read-only. Fixture excerpts are test-only, not another maintained Evidence Bank.

## Implemented

- All 15 requested principles are mandatory Skill rules, linked from the entrypoint and used by both workflows.
- Evidence metadata supports all requested fields, UNKNOWN defaults, ownership/metric/use boundaries and original-owner references.
- Claim/source epistemic levels, China Tier 1–4, exact job identity, source freshness/conflict and historical-vs-live distinction.
- Scoped qualifications and MUST/preference distinction; all ten assessment dimensions and eight gap categories; no match score.
- Sales-specific work-style negatives; neutral normal collaboration; separate interview process risks; direct functional role preference over otherwise-equal MT.
- `/analyse-job` generates a complete bounded candidate analysis; `/prepare-application` has a same-job/current-source/qualification/evidence/company-slot gate and stops at review strategy.
- Requirement→evidence→verified fact→claim chain, existing CV Base/project router, optional VibeCoded packet with human/AI/team boundaries.
- Pure guards plus real-source historical fixtures, negative/fault-injection tests and authored workflow walkthroughs.

## Reuse decisions

REUSE current Career owners. INSPIRE for `ai-job-search` and `resume-tailoring-skill` at comparison-name level only (upstream identity/features unverified). LATER for `career-ops`. ADAPT the approved deep-dive, stop-rule, metric-scope, evidence-indexing, requirement/evidence/gap and interview/untrusted-input methods from the two named comparison samples. DROP their second evidence/Base lifecycles, automatic writeback, dashboard, browser-local SSOT, replacement templates and mandatory full packages. BUILD the original portable instructions and guards. Details: [reuse matrix](reuse-matrix.md).

## Validation and acceptance evidence

**33/33 offline regression tests PASS.** The same suite passed with writes, subprocess execution and socket actions denied by an audit hook. Original source-file hashes match the inspected baseline. All local Markdown references resolve. New-file whitespace checks pass using Git no-index; staged/branch checks are not applicable because this workspace is not a repository.

Initial-run bundled skill-creator validator: **UNAVAILABLE**, missing PyYAML, no dependency installed. The final patch above replaces that default acceptance dependency with the successful local standard-library validator. The bundled script remains optional and was not modified.

| Requested acceptance | Evidence / limit |
|---|---|
| 1–5: no duplicate owners/tracker, external Skill execution, PAW or protected-source edits | Writes limited to the new 26-file directory; source hashes unchanged; no external skill installed or imported |
| 6–8: fact/report/inference/unknown, capability vs eligibility, visible negatives | Shared contracts/rules; A–F walkthroughs; gate/match/qualification regression tests. Semantic entailment still requires agent/Human source review |
| 9–11: work-style, city, MT | Mandatory rules and walkthrough assessment matrix; sales/interview and domain-priority guard tests. MT tie-break is an agent instruction, not an automated ranking engine |
| 12: Vibe-Coded boundaries | F source-derived packet and negative claim/packet tests; individual test→change ledger unavailable |
| 13: real regression without inflation | A–F all based on located real reports/messages. E original authority and F event-level trace incomplete; controlled additions are explicitly synthetic. No independent model forward-test was performed |
| 14–15: UNKNOWN and analysis/preparation-only | Missing metadata/identity/source/slot tests, HOLD gates, nonmutating source checks and deny-side-effect run |

This is a scoped implementation/guard PASS. It does not establish full autonomous semantic reliability or complete primary-evidence trace for every real case; those remain review limitations, not silently passing evidence.

## SSOT conflicts handled without edits

- Older method lists three workflows; latest canonical and request specify four overall, two in Slice 1. Follow the latter.
- Old Tencent scan VERIFY is superseded historically by explicit user ELIGIBLE confirmation and newer routing; it does not become freshly reverified today.
- General Product router may include PAW; the Kuaishou/Baidu completed-only batch excludes active PAW/Portfolio production. Completed AR research remains permitted. Later AR accepted high-fi does not rewrite the batch.
- DNEG's prototype deployment/integration note is not proof of commercial production adoption or current live AI execution.

## Information that cannot safely be promoted

- Master Evidence originals and frozen CV Base exact versions were not available; no substitute bank/Base was created and no new adoptable CV claim was produced.
- P&G CMK closure is traceable to an exact historical assistant report; original authority URL/snapshot and exact requisition are UNKNOWN. Real-case current result remains VERIFY/HOLD; CLOSED precedence is additionally tested with labelled synthetic authority observations.
- DNEG 3 formal rounds / 9+ changes are traceable at aggregate report level. Individual event records, participant count, raw feedback and some decision authorship remain UNKNOWN.
- Current live job status/deadlines, public/resume-use approvals and exact team/HC cannot be inferred from these historical fixtures.

## Deferred / stop boundary

`/position`, `/discover`, Codex Adapter/global installation, PAW integration, automation/scanning/monitoring, dashboard/tracker, paid APIs, external Skill audit/import, recruiting-site login, submission, uploads and recruiter contact are not implemented. No CV/canonical writeback, portfolio production reopening, commit, push or deployment occurred.

To use the portable implementation explicitly, ask an agent to read this directory's SKILL.md and run `/analyse-job` on a supplied real job with existing evidence references. It will produce bounded analysis when inputs are missing and hold preparation where required. Human review of this delivery remains the current stop.
