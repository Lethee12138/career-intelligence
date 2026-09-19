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

### scan_and_review()

Purpose:

Provide the ChatGPT/agent-facing high-level operation for one bounded scan cycle.

Reference implementation:

- Core orchestration: `scripts/career_scan.py`
- Private MCP HTTP surface: `mcp/career-mcp-http-server.mjs`
- Secure Tunnel helper: `scripts/career-mcp-tunnel.sh`

The MCP server binds only to `127.0.0.1:8797` and is stateless. Personal Career context is request-scoped and is not persisted by the server. Tunnel ID and runtime credentials remain external to the repository; Career must not reuse PAW's tunnel ID, local MCP port, or credential file.

Input:

- `useConfiguredSources=true` by default
- omit `scanConfig` for the current configured source preset
- optional explicit, schema-validated custom `scanConfig` only for intentional source overrides
- ephemeral Career context referencing existing owners
- optional current exact-role records / constraints

The MCP surface must advertise concrete custom-source fields (`adapter`, `mode`, `url` / `urls`, optional query/location and bounded limits) plus a stable output schema. Invalid custom input returns a descriptive contract error; raw `KeyError` or other implementation exceptions are not part of the public contract.

Execution:

`public discovery → official verification → dedupe → transparent triage → exact-role review packets`

Output:

- compact summary
- Candidate Pool
- review packets
- exact-role continuity markers
- qualification/source gates
- Human Review boundary

This operation MUST NOT turn triage into final Fit, persist Career state, edit CV/Portfolio materials or perform an application. MCP implementations should wrap the same Core logic rather than reimplementing a parallel scanner.

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
