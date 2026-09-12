# Slice 2 regression and Human Review

Slice 1 [protocol](README.md), tests, fixtures and accepted outputs remain unchanged. New [fixture](fixtures/slice2-cases.json) contains minimal paraphrases of five completed project sections from OUTPUT, plus a real historical OPPO report case from SCAN. Resolve the existing source keys and hashes with [source manifest](fixtures/source-manifest.json). Fixture locators extend the original manifest's narrow OUTPUT/SCAN locators without changing its accepted history. Education/preferences come from CANONICAL; no new personal truth owner is created.

Run from the repository root, without dependencies:

```sh
python3 -I -S -B scripts/validate.py
python3 -B -m unittest discover -s tests -p test_core.py -v
python3 -B -m unittest discover -s tests -p test_discovery.py -v
python3 -B tests/acceptance_check.py
```

The new [discovery guard](../scripts/discovery_guard.py) checks manually grounded assertions. It does not generate a role pool, read or verify evidence, decide semantic entailment, search, rank jobs or recommend applications. `behavior_reviewed`, `problem_reviewed` and direct verification flags are explicit caller assertions, not automated proof. Existing [guard](../scripts/guard.py) remains owner of formal qualification and work-style checks.

| Case | Executable boundary coverage | Semantic review obligation |
|---|---|---|
| A | Secondary completed outputs cannot be promoted to DEMONSTRATED | Five project outputs can support Applied AI Product, Product Discovery, Prototyping, Workflow/Ops, HITL and Game Systems hypotheses; no automatic SWE/front-end/visual craft |
| B | Distinct owned behavior, copied-context rejection, single tool/course/AI implementation rejection | Name the actual repeated behavior; do not infer from project counts |
| C | Seed bridge requires counter and alternative | PM support AND commercial/technical counters, adjacent routes |
| D | Degree does not gate capability; shared qualification rejects explicit verified MUST failure | Media degree leaves product plausible, real JD degree gate remains role-specific |
| E | Problem-first route accepts non-media teams and requires repeated trace | Multiple plausible industries/team types for each hypothesis |
| F | Title cannot override revenue duties | Inspect all four traps: growth/revenue, presales, visual-heavy, engineering |
| G | Existing work-style negatives and neutral collaboration | Keep capability adjacency despite preference downgrade |
| H | MT conditions fail closed; equal direct function preferred | MT has no automatic priority |
| I | One weak signal can be POTENTIAL, not inferred | Do not turn the weak item into a new stable capability |
| J | Real reported OPPO mismatch appends scoped contradiction and preserves original hypothesis | Historical report is not a supplied current original JD; no family-wide rejection |

Additional controls cover explicit-self Route B, hidden Route C ownership, strong-single exception, missing trace, categorical confidence, taxonomy/future observation rejection and questioning stops. The current inspected-JD positive control is explicitly SYNTHETIC. No real-time READY-path or employer validation is claimed.

For behavioral review give a fresh agent only SKILL.md and the raw Slice 2 fixture, with linked contracts and source-manifest available; do not expose this checklist, tests, delivery or intended output. Run /position → /discover in an isolated temporary directory without network or real-owner writes. Inspect the result for the semantic obligations above before copying a reviewed artifact into this repository. One fresh-context agent run is not an independent-model benchmark or Human acceptance.
