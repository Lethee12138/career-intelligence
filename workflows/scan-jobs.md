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

1. Discover public job sources.
2. Normalize job information.
3. Verify source and vacancy status.
4. Assess:
   - Eligibility Fit
   - Capability Fit
   - Preference Fit
   - Job Quality
   - Interview Process Risk
5. Route candidate.

## Output

Return Job Scan Candidates.

Allowed routes:

- OPPORTUNITY_POOL
- FAST_LANE
- TARGETED_PREPARE
- WATCH
- CLOSE
