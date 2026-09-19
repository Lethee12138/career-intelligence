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

## Multi-source screening

Optional runtime fields:

- dedupe_identity
- duplicate_count
- screening.state
  - REVIEW_PRIORITY
  - REVIEW
  - VERIFY
  - DEPRIORITIZE
  - CLOSE
- screening.reasons
- screening.location
- screening.role_term_hits
- screening.capability_term_hits
- screening.preference_risk_hits
- screening.student_or_early_career_hits
- screening.experience_requirement
- screening.job_quality
  - default UNKNOWN unless supported by vacancy evidence
- screening.final_fit_decision = false

## Routing

Allowed routes:

- OPPORTUNITY_POOL
- FAST_LANE
- TARGETED_PREPARE
- WATCH
- CLOSE

## Human Review

Required before external action or persistent adoption.
