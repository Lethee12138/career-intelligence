# Public Discovery Adapter Design

## Purpose

Discover possible job opportunities from public sources.

Discovery results are leads, not verified openings.

## Source Types

- public search results
- public job aggregators
- public professional platforms

## Output

Creates:

Discovery Candidate

Fields:

- company
- role
- location
- source_url
- captured_at
- source_type

## Boundary

Discovery Adapter does not:

- confirm final availability
- assess personal fit
- rank companies
- submit applications

Flow:

Discovery Candidate

↓

Source Verification

↓

Job Source Record

↓

Job Scan Candidate
