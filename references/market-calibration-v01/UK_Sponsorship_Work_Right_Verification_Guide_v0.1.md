# UK Sponsorship / Work-right Verification Guide v0.1

**Captured:** 2026-09-13  
**Candidate current work-right state:** `VERIFY`  
**Purpose:** Future role Qualification Gate; not immigration advice and not an application action.

## 1. Four facts that must never be merged

| Fact | What it proves | What it does not prove |
|---|---|---|
| Candidate has current UK work right | Can work under the stated route until its expiry/conditions | That the route covers the role start and full programme |
| Company is on Sponsor Register | Employer holds a relevant sponsor licence | That this role/programme sponsors |
| Company says it “may sponsor” | General willingness may exist | That this role, location, occupation code and salary qualify |
| Role sponsorship confirmed | Official role/programme says support exists | Final visa approval or candidate-specific eligibility |

## 2. Current 2026 rule anchors

### Skilled Worker

A Skilled Worker role normally needs all of the following:

1. eligible occupation code;
2. approved sponsor;
3. Certificate of Sponsorship for this role;
4. salary meeting the applicable threshold and occupation going rate;
5. candidate meeting the remaining visa conditions.

The general salary rule is the higher of **£41,700/year** and the occupation going rate. Some candidates can be paid less under specific rules.

Official sources:

- [GOV.UK — Skilled Worker: your job](https://www.gov.uk/skilled-worker-visa/your-job)
- [GOV.UK — when you can be paid less](https://www.gov.uk/skilled-worker-visa/when-you-can-be-paid-less)

### New entrant

A qualifying new entrant may use 70% of the going rate, but normally still needs at least **£33,400/year**. Possible routes include being under 26, recently on a Student/Graduate route, or working toward a recognised professional qualification. The discounted period is time-limited: total stay under the relevant new-entrant treatment can normally be no more than 4 years, including time already spent on the Graduate route.

Never infer new-entrant eligibility from “graduate” in the job title.

### Graduate visa

Potential eligibility requires, among other things:

- being in the UK when applying;
- holding a current Student/Tier 4 visa;
- successfully completing an eligible UK course;
- the education provider notifying the Home Office;
- applying before the Student visa expires.

Length:

- apply on or before **2026-12-31**: normally 2 years;
- apply on or after **2027-01-01**: normally 18 months;
- PhD/doctoral qualification: 3 years.

It cannot be extended, though switching to another route may be possible.

Official source: [GOV.UK — Graduate visa](https://www.gov.uk/graduate-visa).

## 3. Candidate-specific issue for Dec 2026–Jan 2027 award window

The award window alone does not resolve eligibility. Future Qualification Gate must obtain:

| Field | Current state |
|---|---|
| Course completion date | `VERIFY` |
| University notification date to Home Office | `VERIFY` |
| Student visa expiry | `VERIFY` |
| Earliest lawful Graduate visa application date | `VERIFY` |
| Likely application side of 2027-01-01 | `VERIFY` |
| Role start date and whether current route covers it | `VERIFY` |

This timing can change the Graduate visa duration from 2 years to 18 months.

## 4. Role-level verification workflow

### Gate 1 — Current right to work

Record:

- route/type;
- expiry date;
- hours/employment restrictions;
- whether it covers the proposed start date and programme length.

Output: `WORK_RIGHT CONFIRMED` or `WORK_RIGHT VERIFY`.

### Gate 2 — Sponsor licence

Check the latest [official Sponsor Register](https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers), using legal entity name and location where relevant.

Output: `SPONSOR LICENCE EXISTS`, `NOT FOUND`, or `ENTITY VERIFY`.

This is only a company-level fact.

### Gate 3 — Specific role/programme policy

Use official job page, programme FAQ and employer immigration page. Search for:

- “Skilled Worker sponsorship available/not available”;
- “must have unrestricted/permanent right to work”;
- selected programmes/locations only;
- Graduate visa accepted but no later Skilled Worker support;
- start-date visa validity requirements.

Output: `ROLE SPONSORSHIP CONFIRMED`, `SPONSORSHIP UNKNOWN`, or `SPONSORSHIP UNAVAILABLE`.

Current employer examples show why this gate matters:

- [NatWest](https://jobs.natwestgroup.com/pages/early-talent-application-support): not all graduate programmes sponsor; only where business need and visa criteria are met.
- [Deloitte](https://www.deloitte.com/uk/en/careers/early-careers/work-permits-and-sponsorship.html): support differs by opportunity and visa route.
- [KPMG](https://www.kpmgcareers.co.uk/graduates/how-to-apply/international-students): sponsorship can be restricted to selected programmes/locations.

### Gate 4 — Occupation code and duties

- Identify the code the employer intends to use; do not choose one solely from title.
- Match duties, level and required skills.
- Check whether it is eligible and retrieve the current going rate.

Output: `OCCUPATION CONFIRMED` or `OCCUPATION VERIFY`.

### Gate 5 — Salary

Compare the role's guaranteed base against:

1. general threshold;
2. applicable going rate;
3. any valid new-entrant rule;
4. permitted working hours/salary calculation rules.

Do not use target bonus, equity, relocation or uncertain overtime to cure a salary shortfall unless official guidance explicitly permits that component.

Output: `SALARY GATE PASS`, `SALARY GATE FAIL`, or `SALARY GATE VERIFY`.

### Gate 6 — Timing and employer action

Record:

- role start date;
- time remaining on current visa;
- when employer would issue CoS;
- whether graduate programme length exceeds current work right;
- whether the employer expects a switch before starting.

Output: `TIMING PASS`, `TIMING FAIL`, or `TIMING VERIFY`.

## 5. Final status logic

| Situation | Eligibility output |
|---|---|
| Existing work right fully covers role | Evaluate other qualification gates; sponsorship may be not required now |
| Graduate route plausible but dates missing | `VERIFY` |
| Licence exists but role policy unknown | `VERIFY`; never Eligible by licence alone |
| Role explicitly sponsors and all occupation/salary/timing gates pass | Sponsorship feasibility `PASS`; visa decision still external |
| Role explicitly does not sponsor but current work right fully covers role | May remain eligible for that period; assess programme duration and future dependency |
| Role explicitly does not sponsor and no covering work right | `NOT ELIGIBLE` for that role, not for the Role Family |
| Salary below applicable threshold | `NOT ELIGIBLE` under that Skilled Worker path; other lawful routes remain a separate question |

## 6. Volatile fields — revalidate every role

- salary thresholds and occupation going rates;
- eligible occupation lists;
- sponsor register and legal entity;
- new-entrant criteria and time limits;
- Graduate visa duration/rules;
- employer/program sponsorship policy;
- start dates and salary shown on the current opening.

Recommended verified-date rule: verify at discovery, Qualification Gate, pre-submission Human Review, and offer/visa stage.

## 7. Minimal future Job Record fields

```yaml
uk_eligibility:
  candidate_work_right: VERIFY
  route_type: VERIFY
  route_expiry: VERIFY
  graduate_route_possible: VERIFY
  employer_legal_entity: VERIFY
  sponsor_licence: VERIFY
  role_sponsorship: VERIFY
  occupation_code: VERIFY
  applicable_going_rate: VERIFY
  new_entrant: VERIFY
  salary_gate: VERIFY
  role_start_date: VERIFY
  last_verified: 2026-09-13
```

`UK_SPONSORSHIP_GUIDE_AWAITING_HUMAN_REVIEW`
