# Local Codex installation

Canonical source: `/Users/luna/Luna/career-intelligence`.
Accepted Career logic: commit `bd5b25c96299ed684c725bfcc6fd8191b187bc59`, annotated tag `career-intelligence-v0.2-job-search-execution-accepted-20260913`.

Installed directory symlink:

```text
/Users/luna/.codex/skills/career-intelligence
  -> /Users/luna/.codex/skill-runtimes/career-intelligence
```

Accepted packaging tag: `career-intelligence-v0.2-installable-skill-accepted-20260913`. Resolve its exact commit with `git rev-parse career-intelligence-v0.2-installable-skill-accepted-20260913^{commit}` in the canonical repo.

The runtime is a detached Git worktree at that exact accepted commit, derived from the canonical repository and sharing its Git history. The local skill-runtimes directory is a deliberately chosen private storage location outside the discoverable skills directory; it is not a Codex-required directory. Only the installed symlink is discovered. No manual package copy or independent history is maintained. Development edits do not update the runtime. Do not edit files in the runtime checkout.

## Mechanism verified on this host

Audited 2026-09-13 using `/Applications/ChatGPT.app/Contents/Resources/codex`, version `0.154.0-alpha.6.2`. CODEX_HOME was unset. Existing system skill-installer code resolves its default install root to the home .codex/skills directory. More decisively, `codex debug prompt-input` listed that exact root and existing installed skills. Career Intelligence was absent before registration and present afterwards at `r0/career-intelligence/SKILL.md`. Fresh invocation actually read that path through the directory symlink. This host observation, not a portable assumption about every client, establishes the installation path.

The bundled installer supports curated/GitHub downloads, unnecessary for an existing local repo. The app-server protocol exposes skills/list (forceReload), skills/config/write and experimental extra roots; persistent direct-repo registration was not established. A reversible directory symlink to a detached Git worktree avoids a manually synchronized copy and needs no manifest, API, plugin or public publish. The root directory is symlinked; SKILL.md itself remains a regular file in the canonical repo.

## Use / verification

Start a fresh Codex turn or conversation. Natural-language career requests can select this skill; explicit `$career-intelligence` is also available. Slash labels inside this skill are workflow vocabulary, not newly registered Codex terminal commands. Load only the relevant workflow and its needed rules/references. Tests and full market datasets are not normal invocation inputs.

Verify the live source and version:

```sh
readlink /Users/luna/.codex/skills/career-intelligence
git -C /Users/luna/Luna/career-intelligence rev-parse HEAD
git -C /Users/luna/.codex/skill-runtimes/career-intelligence rev-parse HEAD
git -C /Users/luna/.codex/skill-runtimes/career-intelligence status --porcelain=v1
python3 -I -S -B /Users/luna/.codex/skills/career-intelligence/scripts/validate.py
```

`codex debug prompt-input` from another directory provides an offline discovery check; inspect only the skills section. Its full output may include unrelated session configuration and need not be shared. Real minimal-context invocation evidence is retained in [results](tests/outputs/skill-invocation-results.json).

## Update / disable / remove

Required update lifecycle:

canonical development → tests → Human Review → accepted commit → annotated tag → explicitly update stable runtime worktree → fresh-session invocation check.

The last two steps happen only after Human acceptance. A working-tree edit must never automatically become installed Skill content. Tags are immutable; do not retarget existing accepted tags. Keep the canonical repo as the sole authoring and acceptance owner.

For an authorized update, verify the requested tag is annotated, resolve it to an exact commit in the canonical repo, and confirm the runtime has an empty `git status --porcelain=v1 --untracked-files=all` and detached HEAD. Stop if it is dirty; do not force, stash or discard changes. Then use `git -C /Users/luna/.codex/skill-runtimes/career-intelligence checkout --detach <resolved-accepted-commit>`. Check HEAD equality, shared Git common directory, clean state, installed symlink target, resource validation and fresh invocation before reporting the update complete. No watcher or automatic update hook is installed.

Rollback follows the same clean-state checks and detached checkout procedure using a previously Human-accepted annotated tag. It changes only the derived runtime checkout, not canonical branch history. If recreation is needed, remove only a verified clean runtime via Git worktree management, recreate with `git worktree add --detach <runtime-path> <resolved-accepted-commit>`, and verify the registration again. Never use a destructive reset to conceal dirty runtime state.

For portability to another host, verify that host's supported skill root and choose an explicit private runtime path before registration.

To disable/remove this local registration without touching source files:

```sh
python3 - <<'PY'
from pathlib import Path
p = Path('/Users/luna/.codex/skills/career-intelligence')
assert p.is_symlink() and p.resolve() == Path('/Users/luna/.codex/skill-runtimes/career-intelligence')
p.unlink()
PY
```

Uninstall leaves the canonical repo, Git history and derived runtime intact. Re-enable by verifying the runtime is clean at an accepted commit and creating the same directory symlink only if the destination is absent. Never recursively delete the canonical target. Already-running conversations may retain previously loaded instructions; use a new conversation after disable/re-enable.

## Boundaries and checks

Initial packaging verification (before stable-runtime repoint): six fresh ephemeral Codex exec sessions were launched from an otherwise empty `/tmp/career-skill-invocation`, with natural-language prompts, no skill-name hint, read-only sandbox, no approval requests and web disabled. Small synthetic context was supplied where needed. Evidence records workflow reads and final output, not just a static keyword matcher. The unrelated birthday request must not load Career Intelligence.

Installed resource access covers six workflows, four schemas, twelve rules, one template and five market-reference files. Salary/benefits loading and import hashing succeeded with all Downloads reads forbidden; legacy external paths are provenance, not installed-reference dependencies. Real personal evidence access remains separate from package usability.

Initial packaging validation: standard-library validator PASS (198 local links); six fresh invocation checks 6/6 PASS; retained v0.2 E2E trace replay PASS. Existing Career regression counts are 33/19/7/13/15/15/12/28, all PASS (135 regression tests plus 7 separate acceptance checks). Historical protected-source verification remains `PROTECTED_SOURCE_VERIFICATION_PARTIAL_DUE_TO_MISSING_HISTORICAL_PATHS` (14 matched, 4 missing), as accepted; no reconstruction and no 18/18 PASS claim. No Career decision logic, fixtures, guards or imported references were changed for installation.

Client limitations: testing used the current desktop-bundled CLI runtime; an already-open app task's cached skill list may need the next turn/new conversation. No GUI picker or marketplace registration is claimed. The local daemon control socket was absent, so no daemon restart or app reconfiguration was performed. Unrelated pre-existing plugin icon/MCP startup warnings did not prevent invocation. Trigger selection remains model behavior, not a guarantee for every paraphrase.

No real job search, external application, public publishing, account permission change, API-key purchase or new paid service was performed.
