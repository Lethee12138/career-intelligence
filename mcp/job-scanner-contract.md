# Job Scanner MCP Contract

## Purpose

Provide read-only public job discovery support for Career Intelligence.

The MCP layer retrieves and normalizes external job information.
Career Intelligence remains responsible for assessment and routing.

## Boundary

The MCP layer MUST NOT:

- decide candidate suitability
- rank jobs by company brand
- submit applications
- login to recruitment systems
- upload candidate materials

Human review remains required before external action.

## Core operations


### search_public_jobs()

Purpose:

Discover publicly available job records.

Input examples:

- market
- location
- role family
- source preference
- time window

Output:

Unverified job leads only.

Required fields:

- company
- role
- location
- source_url
- source_type

### verify_job_source()

Purpose:

Check source authority and vacancy status.

Output:

- authority level
- captured time
- status

Allowed status:

- OPEN_VERIFIED
- NEEDS_VERIFY
- CLOSED
