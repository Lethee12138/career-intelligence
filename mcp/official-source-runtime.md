# Official Source Runtime Contract

## Purpose

Provide a shared runtime boundary for official career source adapters.

Adapters provide factual job source records only.

## Input

- company
- career_url
- optional external_job_id

## Output

- company
- role
- location
- department
- source_url
- external_job_id
- captured_at
- verification_status

## Status

- OPEN_VERIFIED
- NEEDS_VERIFY
- CLOSED

## Boundary

Runtime does not produce:

- fit assessment
- ranking
- application decision
