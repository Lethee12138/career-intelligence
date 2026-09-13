# /find-jobs — bounded external search handoff

Read [execution rules](../rules/search-execution.md), [contracts](../schemas/search-execution.md) and [executor template](../templates/search-execution-handoff.md).

1. Existing First: read supplied discovery/hypotheses, capability/evidence references, preferences and optional pool snapshot. Any one useful discovery artifact can suffice; missing optional inputs stay UNKNOWN. Without useful hypotheses, reuse /discover before sending search instructions; do not invent candidate strengths.
2. Select responsibility/problem/output hypotheses; propose title variants with explicit reasons and title traps. Cover active China and UK; other markets opportunity-driven. Preserve selective Creative Tech/Game Systems when evidence justifies them; unfamiliar titles are not exclusions.
3. Make SearchExecutionHandoff with advisory target around 20–40 useful raw results (helper default 30), market/role coverage and stop conditions. Optional search window, exclusions and priority changes require explicit scoped Human context. Do not upload entire canonical/evidence records; include only minimal public search criteria.
4. Include portable pool identities/Applied/Closed exclusions and company constraints when supplied. Unknown pool coverage is disclosed. Targeted WIP defaults to an adjustable 3–5 range; helper uses 4, not an immutable rule.
5. Return the handoff for external executor review; do not execute search, create external tasks, log in, contact or submit. Any executor may return a JobCandidateBatch. Report missing coverage instead of filling quotas with weak matches.
6. On return run intake/normalization/dedupe under /route-jobs. Search screen is shallow; full analysis is reserved for selected roles.

The standard-library [helper](../scripts/search_execution.py) exposes make_handoff. It combines supplied, grounded terms and reasons, not an NLP discovery engine. A handoff is a search request, never proof of demand or vacancies.
