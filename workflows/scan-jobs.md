# /scan-jobs

## Purpose

Discover currently available public job opportunities and create review candidates.

This workflow extends Career Intelligence from reactive job analysis to bounded market discovery.

It does not:

- apply for jobs
- log in to recruitment systems
- upload materials
- contact recruiters
- modify Career canonical records

## Inputs

Required:

- Capability Profile
- Evidence references
- Preference Profile
- Job Quality Profile

Optional:

- Market
- Location
- Industry
- Role family
- Time window

## Process

1. Discover a bounded set of public job sources; discovery-only leads remain `NEEDS_VERIFY`.
2. Normalize source facts through the [official source runtime](../mcp/official-source-runtime.md) when an official adapter is available.
3. Verify source and vacancy status. The standard-library [job source runtime](../scripts/job_source_runtime.py) is the executable source boundary for supported public sources.
4. Combine supported sources with the [multi-source scan batch](../scripts/job_scan_batch.py), deduplicate by stable source identity / official job ID, and preserve failed verification as `NEEDS_VERIFY` rather than inventing closure.
5. Apply transparent first-pass screening signals only:
   - location preference signal
   - role-family term signal
   - capability-language signal
   - explicit preference-risk terms
   - visible student / graduate / experience requirements
   - Job Quality remains UNKNOWN unless the vacancy itself supplies relevant evidence
6. Career Intelligence then assesses:
   - Eligibility Fit
   - Capability Fit
   - Preference Fit
   - Job Quality
   - Interview Process Risk
7. Build exact-role review packets with the [scan review bridge](../scripts/job_scan_review_bridge.py). Existing exact roles become continuity packets rather than duplicates; visible internship/experience/language/quant gates are surfaced before high-effort analysis.
8. Send only bounded new candidates into `/analyse-job`; roles already in the Application Pool reuse their existing state. Route only after Career Intelligence review.

## Output

Return a deduplicated Candidate Pool. The batch runtime may add non-final screening states:

- REVIEW_PRIORITY
- REVIEW
- VERIFY
- DEPRIORITIZE
- CLOSE

These are triage states, not final Fit or application decisions. The downstream review bridge emits `EXISTING_POOL_CONTINUITY`, `SOURCE_VERIFY_FIRST`, `QUALIFICATION_REVIEW_REQUIRED` or `READY_FOR_JOB_ANALYSIS`; none is an application authorization.

Allowed Career Intelligence routes:

- OPPORTUNITY_POOL
- FAST_LANE
- TARGETED_PREPARE
- WATCH
- CLOSE
