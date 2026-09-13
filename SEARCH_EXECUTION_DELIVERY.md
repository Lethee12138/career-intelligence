# v0.2 Job Search Execution Layer — Accepted checkpoint

Current status: CAREER_INTELLIGENCE_V02_JOB_SEARCH_EXECUTION_ACCEPTED

Human Review: ACCEPT, direct Human instruction 2026-09-13. Local checkpoint commit message: `Accept Career Intelligence v0.2 Job Search Execution`; annotated tag: `career-intelligence-v0.2-job-search-execution-accepted-20260913`. Protected-source verification remains partial: 14 historical hashes matched, 4 missing historical paths unverifiable, no reconstruction. No push.

The following original delivery snapshot retains pre-acceptance descriptions as historical provenance.

## Original delivery snapshot

Status: CAREER_INTELLIGENCE_V02_JOB_SEARCH_EXECUTION_HUMAN_REVIEW_READY

Baseline remains main / `ab76921fcd5abd219ef7b854c523adfe5b6a36ba` / `career-intelligence-v0.1.3-market-calibration-accepted-20260913`. No commit, tag, history rewrite or push. Scope is portable workflow instructions, offline reviewed-input helpers and a synthetic demonstration; no live search was executed.

## Result

The chain now has explicit handoffs: /discover → /find-jobs → external executor → JobCandidateBatch → intake/dedupe → /route-jobs → Application Pool proposal → selected /analyse-job → /prepare-application. Search and external actions remain executor/Human-owned. No platform API or persistence layer is introduced.

[Human Review artifact](tests/outputs/search-execution-human-review.md) shows query strategy, raw batch, identity resolution, routing and complete Targeted/Fast chains. [Reproducible trace](tests/outputs/search-execution-trace.json) carries exact stage IDs, source observations, matches, independent dimensions, preparation gates and uncertainty. Run `python3 -B scripts/run_search_execution_fixture.py` to reproduce it from the [fixture](tests/fixtures/search-execution.json).

## Implementation

`/find-jobs` uses existing hypotheses and minimal relevant context. It emits SearchExecutionHandoff with active China/UK, opportunity-driven other markets, five query axes with reasons, tiered source routing, authority requirements, requested fields, dedupe rules, advisory target and stop conditions. Default target 30 is adjustable, not mandatory. Missing UK/China non-title coverage is surfaced before declaring the handoff ready. The catalogue supports all seven requested core families and selective Creative Tech/Game Systems; the synthetic example intentionally exercises only three grounded hypotheses.

The [executor template](templates/search-execution-handoff.md) works for ChatGPT Work, web research, manual import or another executor. It requests actual JD/URLs/status/qualification and public quality fields, preserves missing data, forbids unauthorized login/contact/submission and does not copy a full canonical/evidence file into a handoff. Pool is projected to identity/status/constraint context.

`intake_batch` retains every raw variant and observation. Official scoped ID precedes exact official URL, then complete official tuple. Similar names alone do not merge. Conflicting IDs sharing URL or city/BG/programme conflicts remain separate/IDENTITY_VERIFY. Canonical IDs are deterministic across source ordering. Discovery and authority remain separate. Official closure beats platform OPEN; 404/conflicting status or stale evidence remains VERIFY. Caller-supplied LIVE/reviewed flags require actual agent inspection; this helper does not authenticate sources.

Lifecycle is DISCOVERED, AUTHORITY_VERIFIED, QUALIFICATION_VERIFY, SCREEN_READY or CLOSED; explicit expired closures can be represented as closed/unavailable with reason. It never writes an application status. Malformed or weak results stay DISCOVERED/VERIFY. Existing qualification, status and global-work-right guards are reused; company type, jurisdiction, location, sponsorship and qualification stay separate.

`route_pool` emits explained TARGETED_PREPARE, FAST_APPLY, WATCH_VERIFY or SKIP with lane, queue state and one Human action. It carries independent assessment dimensions, quality and work-right friction. It does not calculate a total score or percentage. Duties and value can favor an unfamiliar Shenzhen role over a weaker Hangzhou role. Known Job Quality concerns materially downgrade; dated PARTIAL salary does not decide. Sponsor unknown keeps a UK hypothesis open. Targeted WIP defaults to 4, is adjustable, and queues excess. Exact pool matches do not become new active work; company FULL/VERIFY constraints hold further work. Allocation follows supplied order, visibly; Human can reorder without hidden scoring.

## Exact changed / added files

Modified — 3:

- `SKILL.md` — six-workflow entrypoint and explicit external execution boundary.
- `schemas/contracts.md` — link to portable execution contracts.
- `workflows/discover.md` — explicit next handoff to /find-jobs.

Added — 12:

- `workflows/find-jobs.md`
- `workflows/route-jobs.md`
- `rules/search-execution.md`
- `schemas/search-execution.md`
- `templates/search-execution-handoff.md`
- `scripts/search_execution.py`
- `scripts/run_search_execution_fixture.py`
- `tests/fixtures/search-execution.json`
- `tests/test_search_execution.py`
- `tests/outputs/search-execution-trace.json`
- `tests/outputs/search-execution-human-review.md`
- `SEARCH_EXECUTION_DELIVERY.md`

## Exact existing files reused unchanged

Core helpers: `scripts/guard.py`, `scripts/discovery_guard.py`, `scripts/stretch_guard.py`, `scripts/job_quality_guard.py`, `scripts/global_market_guard.py`, `scripts/market_calibration_guard.py`, `scripts/validate.py`.

Existing workflows: `workflows/position.md`, `workflows/analyse-job.md`, `workflows/prepare-application.md`. Rules/contracts: `rules/evidence.md`, `rules/source-and-inference.md`, `rules/eligibility.md`, `rules/opportunity-assessment.md`, `rules/discovery.md`, `rules/stretch.md`, `rules/job-quality.md`, `rules/global-market.md`, `rules/market-calibration.md`, `rules/cv-claims.md`, `rules/user-questioning.md`, `schemas/capability-profile.md`, `schemas/role-hypothesis.md`.

Preference/market references: `references/job-quality-profile.md`, `references/global-market-context.md`, and all five files under `references/market-calibration-v01/` (four imported research artifacts plus manifest). Historical tests, fixtures and outputs remain byte-identical; no prior fixture was edited to pass new tests.

## Tests / E2E

| Check | Result |
|---|---|
| Dependency-free validator | PASS, standard library only |
| Slice 1 | 33/33 PASS |
| Slice 2 | 19/19 PASS |
| Existing acceptance | 7/7 PASS |
| Core / Stretch | 13/13 PASS |
| Job Quality | 15/15 PASS |
| Global Market | 15/15 PASS |
| Market Calibration | 12/12 PASS |
| v0.2 Execution | 28/28 PASS |
| E2E | 12 raw → 11 candidates; 2 selected complete chains |
| Baseline files | Only the 3 listed baseline files modified; old tests/fixtures/guards/references unchanged |

Commands: `python3 -I -S -B scripts/validate.py`; `python3 -B -m unittest discover -s tests -p test_<suite>.py` for core, discovery, stretch, job_quality, global_market, market_calibration, search_execution; `python3 -B tests/acceptance_check.py`. E2E trace replay compares generated output with retained JSON.

Tests A–L cover all requested routing cases. Additional tests cover query axes, active market coverage, minimal inputs, privacy projection, nonmutation, stale authority, conflicting IDs/payloads, malformed results, wrong-role source/qualification binding, defensible stretch, company constraints, calibration-only observations, two existing-Core chains, order-independent identity and normalized pool reuse and latest-authority payload selection at the same URL.

E2E routes: 3 Targeted, 2 Fast, 4 Watch (including existing Applied pool record), 2 Skip. Only one Targeted and one Fast receive complete analysis/preparation. Both run existing match, assessment, stretch, claim and preparation guards; preferred production-model gap remains PARTIAL. The synthetic positive-control gate is READY_FOR_REVIEW, explicitly not real readiness or adoption. Removing current-source assertion returns PREPARATION_HOLD. Real CV base/version and permissions remain UNKNOWN/outside simulation; no CV source or real candidate claim was created.

## SSOT and limitations

No new canonical owner, evidence bank, CV lifecycle or persistent tracker. AOS is reused as the existing Fast/Targeted preparation distinction plus this Human instruction; no missing external AOS implementation was reconstructed. SKILL runtime wording now permits handoff/intake/routing review artifacts while retaining the ban on automatic search and actions. No conflict with accepted evidence/stretch/Job Quality/calibration boundaries was found.

`PROTECTED_SOURCE_VERIFICATION_PARTIAL_DUE_TO_MISSING_HISTORICAL_PATHS` remains: 14 historical source/CV files available and hash-matched; 4 historical Downloads paths unavailable, no reconstruction. Personal Preference and imported market-reference files remain unchanged. This is not 18/18 PASS.

Ready to drive a real Work search **at the portable handoff/intake protocol level**, after Human selects real discovery context and authorizes the executor. This is not proof of live executor recall, market coverage, current openings or source authentication. Query vocabulary may need market-local refinement; the China-heavy synthetic batch is branch coverage, not a search quota. Search quality and independent model benchmarks remain untested.

Intentionally deferred: actual search, crawler/scraper, browser automation, monitoring, provider adapter, PAW, dashboard, automatic outreach/application, negotiation and any owner mutation. Structured helpers rely on inspected, reviewed assertions; they do not infer semantic matches or truth from raw prose. No next-stage task is started.

`CAREER_INTELLIGENCE_V02_JOB_SEARCH_EXECUTION_HUMAN_REVIEW_READY`
