# v0.1.1 Job Quality & Offer Preference Integration — accepted

Status: `CAREER_INTELLIGENCE_V011_JOB_QUALITY_ACCEPTED`. Human Review returned ACCEPT for this increment, its preference semantics and its documented UNKNOWN / MARKET_VERIFY fields. The pre-checkpoint main HEAD and immutable Core accepted tag target are `79e624f82125d4f296663e6bba0b692536a52462`. Worktree/index were clean before implementation. This record accompanies the authorized local durable checkpoint; no push is authorized.

## Existing first / schema decision

The accepted ten assessment dimensions already cover preference, practical fit, work style, career value and uncertainty. Their names and guard contract remain unchanged. An additive `job_quality` detail in the existing shared contract was sufficient; no separate schema file, capability system, offer database or workflow was needed. It can later support Offer Quality Assessment through grouped views, without a /compare-offers command or weighted score.

The Human-confirmed profile is a scoped reference transcription of this request, with DIRECT_USER provenance, version/date, attachment identity/hash and topic IDs. It records preferences, not market/company truths; it does not replace or modify Career canonical. It is not automatically a default for other candidates.

## Exact existing files reused unchanged

- `rules/evidence.md`, `rules/source-and-inference.md`, `rules/eligibility.md`, `rules/user-questioning.md`, `rules/cv-claims.md`, `rules/discovery.md`, `rules/stretch.md`.
- `schemas/capability-profile.md`, `schemas/role-hypothesis.md`.
- `scripts/guard.py`, `scripts/discovery_guard.py`, `scripts/stretch_guard.py`, `scripts/validate.py`.
- `tests/test_core.py`, `tests/test_discovery.py`, `tests/test_stretch.py`, `tests/acceptance_check.py` and every previously accepted fixture/output.
- `tests/README.md`, `tests/SLICE2.md`, `SOURCES.md`, `LICENSES.md`, `reuse-matrix.md`, `DELIVERY.md`, `SLICE2_DELIVERY.md`, `CORE_INTEGRATION_DELIVERY.md` remain existing records/reference context.
- Read-only external source hashes use the existing seven-source manifest plus eleven candidate/CV documents from the pre-edit snapshot; those files were not changed.

## Exact modified / added files

Modified (7):

1. [SKILL.md](SKILL.md) — load Job Quality rule/profile within the four existing commands.
2. [rules/opportunity-assessment.md](rules/opportunity-assessment.md) — Job Quality detail and recommendation effects, without replacing ten dimensions.
3. [schemas/contracts.md](schemas/contracts.md) — preference strengths, contextual pay basis, Job Quality details, tradeoffs and later Offer Quality grouping.
4. [workflows/position.md](workflows/position.md) — environment/value context alongside capability evidence.
5. [workflows/discover.md](workflows/discover.md) — sourced quality risks affect pursuit, not capability truth.
6. [workflows/analyse-job.md](workflows/analyse-job.md) — primary assessment integration and explicit recommendation effects.
7. [workflows/prepare-application.md](workflows/prepare-application.md) — retain known serious risks; do not gate on ordinary missing quality fields.

Added (7):

1. [references/job-quality-profile.md](references/job-quality-profile.md) — scoped Human-confirmed baseline.
2. [rules/job-quality.md](rules/job-quality.md) — cross-workflow interpretation and tradeoffs.
3. [scripts/job_quality_guard.py](scripts/job_quality_guard.py) — pure structured-signal checks, bounded hardship and stable-pay basis checks.
4. [tests/fixtures/job-quality-synthetic.json](tests/fixtures/job-quality-synthetic.json) — twelve privacy-safe hypothetical offers, no real market salary claims.
5. [tests/test_job_quality.py](tests/test_job_quality.py) — focused regression.
6. [tests/outputs/job-quality-human-review.md](tests/outputs/job-quality-human-review.md) — six readable hypothetical comparisons.
7. This `JOB_QUALITY_DELIVERY.md`.

## Preference model and workflow integration

Strengths: HARD_FLOOR, STRONG_NEGATIVE, STRONG_PREFERENCE, POSITIVE_BONUS, TRADEABLE, UNKNOWN. ACCEPTABLE is a stance, STRONG_CONCERN maps to a material negative, and PERFORMANCE_ENVIRONMENT_RISK is a distinct risk annotation. Housing fund's low priority is qualitative, not a hidden numeric weight. No current numerical Human HARD_FLOOR is invented.

Salary references remain subjective/contextual: approximately 4–6k low attraction, below approximately 5–6k requiring exceptional concrete return, 8–9k normal-graduate status MARKET_VERIFY. No upper cap. City × Role Family × Graduate Market/year/company type is the calibration scope, alongside costs, workload and benefits. Effective Compensation distinguishes dependable cash, realistically obtainable benefits/subsidies and material living/location costs without an automatic financial calculator. Uncertain bonus is not guaranteed pay; housing/talent support matters more away from home but needs eligibility/obtainability evidence.

Work/rest distinguishes structural overtime from exceptional compensated peaks; usable leave is material. Team pressure is surfaced as performance-environment risk, not merely taste or a diagnosis. Startup/brand/stability never substitute for actual payroll, business, role and manager evidence. Risk can be exchanged for specific credible return; hardship needs bounded cost/duration, mitigation and review/exit conditions. Probation 80% alone is acceptable in the personal baseline; long duration plus meaningful risk changes the assessment without invented rates. Social insurance is a baseline expectation, not a legal compliance verdict. Work arrangement, commute/travel, annual leave and other benefits retain their different strengths.

/position preserves capabilities; /discover keeps capability adjacency while adjusting pursuit based on sourced signals; /analyse-job explains independent Job Quality Fit and resulting recommendation change; /prepare-application carries serious concerns before further effort. Ordinary quality UNKNOWN does not enter critical_unknowns automatically. Existing live source/qualification/claim-use gates continue to apply, and favorable quality cannot promote a closed, ineligible or unresolved-source role.

Known severe concerns normally lower an otherwise active recommendation to Low Priority. An explicit contextual HARD_FLOOR breach normally yields Not Viable Currently. These are scoped recommendation effects, not automatic offer acceptance/rejection or numeric ranking. A well-supported risk-return exception remains a Human trade-off, never automatic rank restoration. Capability Fit is unchanged by this overlay.

## Execution, tests and limits of automation

The agent read the accepted rules/contracts, applied the increment and manually interpreted the six synthetic comparisons. Actual `quality_review` runs cover all twelve offers; focused tests exercise observed priority effects, basis validation and adversarial inputs. The guard accepts manually grounded signal classifications. It does not infer raw prose, verify salary/culture, classify legal compliance, estimate personal budgets, calculate market pay or rank all offers. A mostly unknown positive case remains MIXED/UNKNOWN rather than becoming a complete quality endorsement.

Focused regression: **15/15 PASS**:

- A high fit + structural workload/management → materially lower recommendation, capability stays HIGH.
- B higher salary cannot alone cancel structural pressure; no fixed premium threshold.
- C excellent environment/hybrid cannot cure an explicitly contextual synthetic floor; unconfirmed floor becomes VERIFY.
- D changing company type does not itself reject startup.
- E stability alone does not dominate interesting, well-compensated, moderate-risk ownership.
- F usable 5 vs 15 leave yields meaningful preference; unusable nominal leave is negative.
- G uncertain bonus cannot enter guaranteed comparison.
- H 80% normal probation acceptable; long meaningful elimination-risk probation concerns remain.
- I hybrid remains positive but cannot cancel severe negatives.
- J absent manager/team evidence remains UNKNOWN regardless of brand.
- Additional: no universal salary floor/cap; missing refs/unreviewed observations require verification; hardship conditions; unknown quality alone does not block otherwise valid synthetic preparation; quality cannot promote an existing Not Viable / Explore result.

Existing results: dependency-free validator **PASS**; Slice 1 **33/33 PASS**; Slice 2 **19/19 PASS**; existing acceptance **7/7 PASS**; Core/Stretch **13/13 PASS**. Old tests and fixtures remain unchanged. Protected source hashes **18/18 unchanged** against the pre-increment snapshot. Whitespace/diff checks PASS. No dependencies installed.

Reproduce from repository root:

```sh
python3 -I -S -B scripts/validate.py
python3 -B -m unittest discover -s tests -p test_core.py
python3 -B -m unittest discover -s tests -p test_discovery.py
python3 -B tests/acceptance_check.py
python3 -B -m unittest discover -s tests -p test_stretch.py
python3 -B -m unittest discover -s tests -p test_job_quality.py
```

## Human Review / conflicts / unresolved fields

The [artifact](tests/outputs/job-quality-human-review.md) covers pay vs sustainable hours, good environment below a contextual living floor, stable low-value vs moderate-risk startup, actual annual leave, contingent bonus vs stable base, and probation risk. It distinguishes psychological/performance environment from personal dislike. Money is material, benefits are not equally weighted, and risk is neither glorified nor categorically rejected. Recommendation categories do not force fine-grained rankings: e.g. both leave options can remain Apply while usable 15-day leave carries a strong relative preference.

No conflict with accepted Core was found. This adds the job-worth-doing side without altering evidence, use_boundary or capability status. UNKNOWN quality does not loosen mandatory source/qualification gates, and strategic packaging cannot invent employer quality facts. Human-confirmed personal expectations are separate from legal/market assertions.

No supplied preference required unsafe fabrication or a second schema. Not yet safely representable as fixed facts: exact personal living floor and salary gross/net basis; 8–9k graduate market status; actual city/role/year compensation distributions and living costs; concrete subsidy eligibility/timing; real manager/culture, leave usability, payroll/viability and probation elimination rates. Long-term/frequent assignment preference remains UNKNOWN. Some outcomes require contextual Human judgment, not an invented threshold.

No actual offer, company, salary market, legal status or current vacancy was verified. Existing Master Evidence/frozen CV/event-trace limitations and lack of independent model benchmark remain. No sources, CVs, canonical records or accepted tags changed. The accepted implementation, tests and preferences are unchanged during checkpoint creation; only this delivery acceptance record is updated. No Codex Adapter, PAW integration, scanner, monitoring, dashboard, application submission or negotiation automation was started.

## Durable checkpoint

Human ACCEPT supersedes the earlier review-ready handoff. The unresolved personal living-cost floor, gross/net comparison convention, city/role market benchmarks, subsidy eligibility, actual team/manager conditions and long-term relocation/assignment tolerance remain accepted calibration needs, not implementation defects.

Checkpoint branch: `main`. Commit message: `Accept Career Intelligence v0.1.1 Job Quality`. Annotated tag: `career-intelligence-v0.1.1-job-quality-accepted-20260913`. Resolve the exact final commit through that tag; the commit identity, tag target and post-commit cleanliness are verified and reported after creation.

Checkpoint checks: dependency-free validator PASS; Slice 1 33/33; Slice 2 19/19; acceptance 7/7; Core/Stretch 13/13; Job Quality 15/15; protected hashes 18/18 unchanged; final diff/whitespace/temporary-file checks PASS.

Job Quality Market Calibration is a separate future task and has not started. Personal Preference remains distinct from Market Benchmark. No push or other external action is part of this checkpoint.

`CAREER_INTELLIGENCE_V011_JOB_QUALITY_ACCEPTED`
