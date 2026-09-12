# Global opportunity / market-specific calibration v0.1.2

Reuse [eligibility](eligibility.md), [sources](source-and-inference.md), [assessment](opportunity-assessment.md), [Job Quality](job-quality.md), [contracts](../schemas/contracts.md) and [Human market context](../references/global-market-context.md). No live research, global static database or new workflow is required.

Discovery order: Capability / Problem / Output → Role Hypothesis → Market possibilities → specific location, eligibility and quality checks. Do not delete capability or transferable potential because a visa is missing. China remains easy to execute as a high-activity market; UK remains active through normal discovery, qualification and preparation; other markets stay open until a concrete opportunity justifies calibration. Unknown work rights are not a verified legal impossibility.

## Separate identities and gates

Employment market is the actual labor/employment jurisdiction; company nationality/type is a separate attribute; work location records country/region/city. Resolve ambiguity (remote cross-border arrangements, multiple locations) explicitly, not from headquarters or brand. A foreign MNC Shanghai role can be China employment; a Chinese company's London role can be UK employment. Neither example proves pay, benefits, sponsorship or culture.

Record candidate current work authorization and its scope/conditions/expiry, employer sponsorship policy for the exact job/program, other possible routes, and separate qualification rows (graduation, degree, language, citizenship only where an applicable hard criterion is established, program, experience, location and other requirements). References must bind to the same role, employment market, version/as-of and candidate context. Sponsor registration or company-wide past sponsorship alone does not establish sponsorship for this job. An offer to sponsor is not visa issuance or candidate route eligibility.

Use a work-right resolution summary alongside the separate fields:

- ALREADY_AUTHORISED: sourced current authorization applicable to this job.
- SPONSORSHIP_REQUIRED: candidate needs sponsorship; this records need, not availability.
- SPONSORSHIP_AVAILABLE: credible job/program-specific confirmation, with route conditions separately checked.
- SPONSORSHIP_VERIFY: employer support/applicability unknown or only potentially available.
- SPONSORSHIP_UNAVAILABLE: credible explicit no-sponsorship plus no existing applicable work right or other established route.
- OTHER_ROUTE_VERIFY: plausible alternative lawful route has not been verified.

Preserve need and availability simultaneously (e.g. need=SPONSORSHIP_REQUIRED, resolution=SPONSORSHIP_AVAILABLE). An unverified alternative is not a bypass. Formal qualification remains ELIGIBLE / VERIFY / NOT ELIGIBLE using existing per-gate rules. All applicable gates must pass for overall ELIGIBLE. Explicit no sponsorship only makes the exact job NOT ELIGIBLE when the candidate needs it and has no other route; otherwise retain the appropriate VERIFY or authorized path. Never lower Capability Fit or close the entire market/family on that basis. Conflicting, stale or wrongly scoped observations require verification.

## Market Job Quality / optional benchmark

Personal Preference is not Market Benchmark. Calibrate salary/currency/gross-net convention, local costs/rent, pension/social insurance, health insurance, leave, probation, working-time norms, sponsorship, relocation and local benefits when a concrete opportunity warrants it. The optional benchmark in the shared contract is external evidence with context, source levels, dates and limitations; it is neither a personal floor nor an employer promise. Empty benchmark is valid, MARKET_VERIFY; no numbers are needed to initialize this framework.

Do not compare RMB/month and GBP/year nominally or conclude offer quality from FX conversion. Align periods and pay bases, then examine relevant taxes, living/rent costs, benefits, hours, pension/social insurance, relocation and visa constraints/costs. Unknown factors prevent an asserted financial winner, not all strategy discussion. Currency syntax validation is not an exchange-rate or market-quality validator. China housing fund and UK pension need local contribution/access/eligibility context; labels are not equivalent units of value. Do not propagate China-specific benefit priority or city order globally.

Overseas adds possible application friction, source checks, timing, employer constraints and relocation cost. Record those specific burdens, not an automatic Low Priority. Strong fit, job quality and career value with realistic sponsorship can support high priority after ordinary gates; a modest-value opportunity may not justify substantial verification/relocation effort. Neither conclusion follows from geography alone.

## Four workflow use

/position remains market-agnostic, attaching preference/feasibility context without changing identity or capability. /discover preserves one hypothesis with China, UK and international title/search variants as useful; vocabulary does not prove demand, openings or sponsorship.

/analyse-job includes market identity, company type, location, work-right/sponsorship, separate qualification rows and contextual Job Quality. High capability and excellent quality can coexist with job-specific NOT ELIGIBLE. Preserve the favorable evidence and record the precise failed gate.

/prepare-application: a worthwhile role with SPONSORSHIP_VERIFY may receive a bounded strategy while qualification/work-right verification remains open. Keep the existing readiness gate PREPARATION_HOLD; add strategy_scope=STRATEGY_ONLY, no approved CV claims or full material bundle, no claim of visa or employer sponsorship. This permits a preparation strategy before work-right resolution, not hidden readiness. Explicit SPONSORSHIP_UNAVAILABLE with no alternative stops full materials and retains only closure reason/verification next action. Existing unknown-quality allowances, claim-use permissions and Human Review remain; no login, submission or negotiation.
