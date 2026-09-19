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

## Review packet bridge

Optional downstream review-packet fields:

- role_key
- review_state
  - EXISTING_POOL_CONTINUITY
  - SOURCE_VERIFY_FIRST
  - QUALIFICATION_REVIEW_REQUIRED
  - READY_FOR_JOB_ANALYSIS
- next_step
- job_identity
- source
- job_text
- scan_screening
- qualification_gate
- candidate_context
- preference_context
- company_constraints
- existing_role
- analysis_contract

The bridge is non-semantic: it may expose visible gate markers, but it does not decide final Capability Fit, Qualification, Job Quality or application route. Existing exact roles reuse current Career state.

## Routing

Allowed routes:

- OPPORTUNITY_POOL
- FAST_LANE
- TARGETED_PREPARE
- WATCH
- CLOSE

## Human Review

Required before external action or persistent adoption.
