# Job Scan Candidate Schema

## Identity

- company
- role
- location
- department

## Source

- source_url
- source_type
  - official
  - campus
  - third_party
  - unknown

- captured_at

## Verification

job_status:

- OPEN_VERIFIED
- NEEDS_VERIFY
- CLOSED

## Assessment

Keep separate:

- eligibility_fit
- capability_fit
- preference_fit
- job_quality
- interview_process_risk

## Routing

Allowed routes:

- OPPORTUNITY_POOL
- FAST_LANE
- TARGETED_PREPARE
- WATCH
- CLOSE

## Human Review

Required before external action or persistent adoption.
