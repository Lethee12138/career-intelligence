# Regression protocol

The canonical default validation path is now the local standard-library validator. Run from the Portable Core with Python 3.9+ and no external packages:

```sh
python3 -B scripts/validate.py
```

It supports exactly the frontmatter this Skill uses: unquoted, single-line `name` and `description` strings. Duplicate/unknown keys, YAML type/collection/alias/block constructs, unfinished scaffold and broken local file links fail explicitly. General YAML parsing is unnecessary for this format. An external full-YAML validator is optional only, is not part of acceptance, and must not trigger dependency installation. The bundled `quick_validate.py` was not changed.

Run the original regression suite separately:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

No network, external skills, accounts, writes to evidence owners or generated trackers. Fixtures A–F are minimal redacted historical case derivatives; source-manifest records inspected source identities. The tests exercise pure guard decisions and adversarial mutations. The three small assertions on Tencent scenario/HC/strategy count and Baidu practicality preserve reviewed fixture conclusions; they do not prove a model will derive them independently.

Recorded final-patch result on 2026-09-12: **dependency-free validator PASS; original regression 33/33 PASS**. The original tests and their fixtures are unchanged. Their existing frontmatter/link checks remain as regression coverage, with the canonical validation entrypoint adding explicit format rejection. In the original implementation run the bundled skill-creator validator was unavailable because PyYAML was absent; that historical limitation no longer blocks the default path. No dependency was installed.

Additional acceptance checks are separate from the 33-test count:

```sh
python3 -B tests/acceptance_check.py
```

This runs seven validator checks (including malformed/unsupported input and broken-link controls), then exercises the existing guards on the Tencent input, excluding its expected-result field from decision inputs. The agent executes both Markdown workflows and supplies the readable [Tencent Human Review artifact](outputs/tencent-final-human-review.md). The honest end-to-end result for this historical input is PREPARATION_HOLD, with one conditional strategy and no CV claim/packet. It is not a live READY-path application test or an independent-model evaluation.

| Case | Real source | Guard coverage |
|---|---|---|
| A Tencent | Direct user ELIGIBLE confirmation + 2026-09-11 local routing report | Preferred-major vs hard gate; real evidence references; scenario remains inference; HC unknown; one strategy |
| B Kuaishou user product | 2026-09-11 accepted operational report | Date interval; slot constraint; completed batch/exclusions; product-data gap |
| C Baidu J100665 | Same report §3 | Date interval, preferred major, Beijing penalty retained alongside high value |
| D Kuaishou commerce | Same report's HOLD section | Unsupported domain gate prevents top tier despite Hangzhou |
| E P&G CMK | Exact historical Career assistant message | Original authority not available → VERIFY/HOLD; explicitly synthetic fault injection proves inspected authority FILLED beats later discovery OPEN |
| F DNEG | Canonical + batch + output report + implementation note | Human/AI/team separation; aggregate test/iteration trace; no invented nine events, engineering or commercial claims |

Read [walkthroughs](walkthroughs.md) for this author's manual execution of the Skill on the six bounded inputs. They distinguish historical analysis/strategy from live eligibility and do not produce adoptable CV claims. A positive preparation-gate control uses clearly synthetic verified facts; it is not a claim of live authority verification for these jobs.

## What these tests do not prove

- No independent model forward-test or live employer revalidation was performed.
- Python cannot establish whether a cited sentence really entails a match or claim; `scope_reviewed` is an input assertion, not Human approval. Agent/source review remains mandatory.
- Master Evidence originals, frozen CV Base revisions, CMK original authority snapshot and DNEG individual change-event ledger were unavailable. Report-level trace is verified; deeper trace stays UNKNOWN.
- Source hash comparison runs for available local sources; portability does not require the author's Downloads folder. It must not be reported as original-source verification on another machine.

For future behavior regression, load SKILL.md and give an evaluator only each fixture's source-derived inputs (hide `expected` and walkthroughs), request both workflows, then compare evidence labels, unsupported rows, dimensions, gate and claim boundaries. Use an isolated output directory; do not touch real owners. Only request deeper missing evidence when it could change the decision. Keep technical PASS separate from Human acceptance.

## v0.2.1 broad discovery and funnel correction

Run the nine focused Pilot regressions separately or as part of full discovery:

```sh
python3 -B -m unittest tests.test_broad_discovery -v
```

They cover AI-neutral full-root discovery, media/communication cross-domain recovery, result-set concentration, Discovery/Fast/Targeted separation, candidate-context gating, technical MUST gates, non-AI priority and existing-pool continuity. The fixtures are synthetic structured controls. They verify guard behavior and contracts, not live market breadth or independent semantic generation.

## v0.2.2 UK work-right routing fix

Run the six focused synthetic routing checks:

```sh
python3 -B -m unittest tests.test_uk_work_right_routing -v
```

## v0.2.3 UK residence/work-territory regressions

```bash
python3 -B -m unittest tests.test_uk_residence_work_territory -v
```

The focused controls cover Home Based versus explicit UK-only authority, outside-UK residence with unknown or impossible relocation, explicit no sponsorship with future need, explicit global remote permission, current-right versus territory separation, Capability/Evidence preservation and the `/prepare-application` material-uncertainty gate. Inputs are synthetic and do not encode or verify a real employer.

They confirm current-right PASS plus future-sponsorship UNKNOWN can remain Fast-ready, sponsor capability does not become exact-role sponsorship, permanent-right and explicit no-sponsorship gates still apply, unknown current right stays Watch, and confirmed role sponsorship cannot override another qualification failure. They are routing controls, not immigration or employer-policy verification.
