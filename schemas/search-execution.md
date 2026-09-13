# Portable Execution contracts v0.2

Extend [shared contracts](contracts.md); all substantive judgments use the existing sourced claim/uncertainty boundary. These are portable JSON/Markdown artifacts, not a database or new SSOT. Every ID binds to source scope, not semantic similarity.

## SearchExecutionHandoff

`schema_version, search_id, created_at, executor, input_refs, market_scope[], role_hypotheses[], location_scope[], query_sets[], source_priorities[], authority_verification_rules[], candidate_fields_required[], dedupe_rules[], target_batch_size, target_is_advisory, stop_conditions[], human_constraints[], existing_pool, existing_pool_coverage, handoff_state, external_action=false`.

Each hypothesis retains id, source capability/evidence refs, epistemic status, bridge/unsupported scope, family and per-market search_terms. Terms have axis title/responsibility/problem/output/negative, term and why. Query combinations do not imply equivalence. Core families: Product/AI/Digital; Agent/Human-AI Workflow; Research/Insights/CX; Ops/Systems/Workflow/Transformation; Strategy/Innovation/AI Adoption; AI Evaluation/HITL Product & Experience Ops; Product Prototyping/0→1 Builder. Creative Tech and Game/Interactive Systems are selective. Choose grounded subsets, report omissions; not every family needs equal quota.

## JobCandidateBatch / JobCandidate

Batch: `batch_id, search_id, executor, captured_at, coverage_by_market_and_hypothesis, stop_reason, candidates[]`. Candidate missing values are UNKNOWN; absent arrays may be empty only when coverage is explicit, never imply no requirements.

Identity: `candidate_id, role_key, company, role_title, employment_market, country, city, company_type, recruitment_route, business_unit, programme`; `identity={official_binding_reviewed, refs, official_job_id, namespace, official_url, complete_tuple_reviewed}`. ID is company/ATS-namespace scoped. Unknown business-unit/programme blocks tuple-only merge. Explicit NOT_APPLICABLE requires source rationale. Dedupe yields canonical candidate_id plus merged_from and raw_variants without destruction.

Sources: discovery_source URL, discovery_source_tier 1–4, authority_source, official_url, source_capture_date, official_published_date, last_verified; observations `{role_key, ref, authority_for_role, inspected_original, observed_at, status}`. Use exact URLs or refs resolving to retained snapshots. Flags are reviewed assertions, not source authentication. An executor's claim to have checked is insufficient until the intake reviewer grounds it. Status is OPEN/CLOSED/VERIFY; FILLED maps CLOSED, 404 alone VERIFY.

Job state: opening_status, deadline, jd_ref, responsibilities[], requirements[], source_status, intake_state, intake_issues. DISCOVERED → AUTHORITY_VERIFIED → QUALIFICATION_VERIFY or SCREEN_READY; current confirmed closed can exit to CLOSED (explicit expired closure may be displayed EXPIRED). Lifecycle is not application status. No inference of closure just from missing page.

Qualification: qualification_review `{role_key, as_of, reviewed, refs, checks[], coverage_complete}` reuses existing MUST/preference guards. work_right_review uses v0.1.2's independent candidate_authorization, employer_sponsorship, other_route and other qualification checks, bound to exact role/market/date. Overall qualification_status remains ELIGIBLE/VERIFY/NOT ELIGIBLE; work_right, sponsorship, unresolved_eligibility_items remain distinct.

Quality: base_salary, guaranteed_cash, variable, benefits, workload_signals, leave, hybrid, probation, stability_signals — all sourced or UNKNOWN. Dated calibration remains contextual and separate.

Intelligence: role_family, matched_role_hypothesis, strongest_capability_match, strongest_evidence_refs, main_gaps. Reviewed screen `{role_key, as_of, reviewed, refs, dimensions, evidence_refs, responsibility_match, career_value, application_cost, critical_unknowns, company_constraint, quality_observations, calibration_context}`. Dimensions retain all ten accepted fields with judgment/rationale/refs/unknowns, including Experience/Practical/Interest/Work-style/Interview/Stretch. Quality observations reuse v0.1.1 and add basis=ROLE_EVIDENCE for current-role concerns; calibration-only observations cannot generate a downgrade. Severe mismatch needs type, mismatch_reason and mismatch_refs; neither city nor salary band is a valid standalone type. Defensible stretch stays PARTIAL with bounded bridge, not fabricated direct experience.

## Application Pool proposal

Input snapshot: `pool_id, captured_at, entries[], company_constraints`. Entries carry exact identity binding, existing application_status (e.g. APPLIED/CLOSED), lane, queue_state and provenance. A missing pool is UNKNOWN coverage, not an empty verified pool. Existing pool matches receive HOLD/EXISTING_POOL, not reintroduced active entries. Company constraints are explicit scoped Human/authority facts, not inferred by brand.

Output: `candidate_status=HUMAN_REVIEW_REQUIRED, targeted_limit, allocation_order, routes[], external_action=false`. Each route: candidate_id, route TARGETED_PREPARE/FAST_APPLY/WATCH_VERIFY/SKIP, lane TARGETED/FAST/NONE, queue_state ACTIVE/QUEUED/REVIEW/WATCH/EXCLUDED/CLOSED/EXISTING_POOL, priority_rationale, next_human_action, independent dimensions, job_quality, work_right_friction, calibration_context if supplied, pool_coverage. No match percentage or weighted total. Routing never sets Applied or writes an application status. Each candidate retains one useful Human action, with no external effect.
