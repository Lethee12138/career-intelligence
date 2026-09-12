# Portable output contracts v0.1

These are required semantic schemas for agent output, not database tables. Markdown reports may use the field labels directly; JSON may use snake_case equivalents. Missing metadata uses literal `UNKNOWN`, not an empty string, inferred default or invented date. `NOT_APPLICABLE` requires rationale. Each substantive statement is a claim object: `{value, kind, source_level, refs, scope, uncertainty}`. Inference must cite premises; UNKNOWN has no positive assertion. References contain `{id, source, location, revision_or_hash, author, observed_at}`. Never treat a reference ID alone as verification.

## Evidence item / match

Evidence item: `id, project_id, source, source_location, ownership_scope, context, action_or_decision, method_or_tool, result_or_output, limitation_or_boundary, metric_scope, confidence_or_uncertainty, public_use_boundary, resume_use_boundary, last_verified_at, provenance, completion_at_cutoff`.

Match row: `requirement_id, requirement_text, requirement_source_location, hierarchy, match_level, evidence_refs, supported_scope, unsupported_scope, gap_types, uncertainty`. Enums are the exact terms in the shared rules. PARTIAL must name the missing part. Each requirement appears exactly once; no hiding weak rows.

## JobAnalysis

- `schema_version`, `candidate_status=HUMAN_REVIEW_REQUIRED`, `job_identity` (company, requisition ID/exact URL, batch, locations), `existing_job_record_ref`, `analysis_date`, `as_of`, `verification_mode`, `evidence_cutoff`, `source_coverage`, `excluded_evidence`.
- Job facts: company, role, recruitment type, location, official source, discovery source, published date, deadline, last/current verification date (UNKNOWN unless verified), status and conflicting observations.
- Qualification: overall ELIGIBLE / VERIFY / NOT ELIGIBLE, scoped gate rows, mandatory/preference distinction, sources and unresolved checks.
- Requirement hierarchy and complete Requirement → Evidence Match rows.
- Actual role interpretation: what it produces, problems owned, title accuracy, premises and inference labels.
- Assessment: all ten named dimensions, each `{judgment, rationale, refs, unknowns}`; no composite score.
- Gaps: typed rows with evidence boundary and decision impact. Risks include work-style, interview, timing/source and company-slot constraints separately.
- Recommendation: allowed category, rationale, decisive positives/negatives, alternatives, what would change it, preparation gate and next action.

## ApplicationBrief

- Exact job/analysis identity and revision, `candidate_status=HUMAN_REVIEW_REQUIRED`, gate `READY_FOR_REVIEW` or `PREPARATION_HOLD` (not authorization).
- Why this role; strongest evidence; likely recruiter concerns; gap/honest response.
- Recommended existing CV Base (name, exact source/version or UNKNOWN); project router (evidence refs, selection reasons, exclusions); portfolio use/permissions or NOT_APPLICABLE with reason.
- Interview evidence stories and follow-up/risk/answer-boundary chains.
- Claim candidates: requirement ID → evidence reference → verified fact reference → bounded proposed text, metric/ownership scope and resume/public-use permission. Broken chains go to gaps.
- Preparation checklist, all remaining VERIFY items, and minimum material questions if justified.
- Optional VibeCodedProjectEvidencePacket: trigger reason, completed project refs, all fields enumerated in claim rules, per-field sources/UNKNOWN, aggregate/event trace distinction, objections and answer boundaries. It never becomes an evidence owner.

Blocked preparation still identifies job, gate reasons and next verification actions, but has no tailored claims, project packet or speculative CV variants. Human approval is not derivable from any report field.
