# /route-jobs — intake to Application Pool proposal

Read [execution rules](../rules/search-execution.md) and [contracts](../schemas/search-execution.md). Use the existing source, eligibility, global market, quality and calibration rules.

1. Accept a plain portable JobCandidateBatch and optional current pool. Preserve raw records; validate identity, provenance, market, exact authority scope/date, JD and critical unknowns. Use UNKNOWN/VERIFY instead of guessed metadata.
2. Deduplicate only exact, officially bound identities. Keep every discovery and authority observation; never overwrite official closure with newer platform content. Ambiguous identity/payload conflicts remain separate and IDENTITY_VERIFY.
3. Light screen each unique candidate across the existing ten independent dimensions plus Job Quality and work-right friction. Explain claims using duties/evidence, not title/brand/city or percentage. Keep defensible stretch and unsupported scope explicit. Do not do full company research for every result.
4. Propose TARGETED_PREPARE, FAST_APPLY, WATCH_VERIFY or SKIP with lane, reason and exactly one next Human action. UK unknown sponsor remains WATCH_VERIFY / VERIFY_SPONSORSHIP, not SKIP. Quality negatives materially downgrade; dated salary alone never decides. Unknown routine quality fields do not block every role; material missing facts do.
5. Check pool duplicates and company-specific slots. Apply adjustable Targeted WIP; a high-value excess role stays TARGETED_CANDIDATE / QUEUED. Pool entry ordering is a visible allocation input, not a ranking score.
6. Hand selected Targeted roles to /analyse-job → /prepare-application. Fast still needs qualification, an honest evidence match and Human Review, but keeps research/material effort bounded. FAST_APPLY is a lane label, not submission authorization. Intake lifecycle, route and application status remain separate.

Use intake_batch and route_pool in the [helper](../scripts/search_execution.py) for structured reviewed inputs. LIVE requires actual current source inspection; fixture mode must explicitly say synthetic simulation. Historical rows cannot bypass the existing Core preparation gate. No owner records are modified by this workflow.
