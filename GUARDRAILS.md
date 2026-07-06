# GUARDRAILS — the project must never topple, and must never lose information

_Owner law, added 2026-07-06 after two mechanical failures nearly cost committed work.
Enforced by `src/guardrails.py` (checks) + `src/git_safe.py` (safe git). The guardrail run
happens every EXCAVA beat; its status shows on the cockpit's 🛡 Guardrails card._

## The one principle
**QUARANTINE, NEVER DELETE.** No operation may permanently destroy uncommitted content.
Anything in the way is moved to `_ATTIC/` (git-ignored, kept forever), never `rm`/`git clean -fd`-ed.

## The two mechanical failures this fixes
1. **Untracked trees blocked every rebase.** CI tracks `skills/` and `other-skills/` (real content).
   Local agent drafts of the same paths are untracked → they collide with incoming commits and abort
   the rebase; `git stash pop` can even OOM on them. The old "fix" was `git clean -fd`, which **deletes**
   them — permanent loss. **Now:** `git_safe.sync()` moves only the colliding untracked files into
   `_ATTIC/quarantine/<timestamp>/` (preserved, reviewable), then rebases. Nothing is destroyed.
2. **PowerShell mangled commit messages.** A message with embedded `"` made PowerShell split it, so git
   read trailing words as pathspecs and the commit failed. **Now:** every commit goes through a UTF-8
   file (`git commit -F _ATTIC/COMMIT_MSG.txt`) via `git_safe.commit()` — the shell never touches the text.

## The 12 guardrails (`python -m src.guardrails`)
| ID | Name | Protects against |
|----|------|------------------|
| G-A | Quarantine over delete | losing uncommitted files to blind `git clean` |
| G-B | Message-file commits | commit-message mangling / failed commits |
| G-C | History backup fresh | total loss — a `git bundle` of all history sits in `_ATTIC/backups/` |
| G-D | No mojibake (UTF-8 intact) | the emoji double-encoding that corrupted v67 |
| G-E | Build alignment | a stale service-worker shell serving old code (`APP_BUILD` == `SHELL_CACHE`) |
| G-F | JSON integrity | shipping a broken data file that blanks the dashboard ("useless") |
| G-G | Remote sync verified | believing a push saved when it didn't (`HEAD` == `origin/main`) |
| G-H | No rebase-blocking collisions | the failure-1 class, caught before it bites |
| G-I | Handoff mentions live build | context loss between sessions (SESSION_HANDOFF.md stale) |
| G-J | Project-memory contract | the WHY log going empty |
| G-K | Append-only audit log | no trail of what happened (`data/guardrails_log.jsonl`, never rewritten) |
| G-L | Uncommitted-work watchdog | stray source files silently never committed |

## How to use the safe git helper (always, from now on)
```
python -m src.git_safe backup                  # bundle all history (do before anything risky)
python -m src.git_safe ship -m "msg" -a f1 f2  # commit (message-file) THEN push+verify, one call
python -m src.git_safe sync                     # revert CI churn + quarantine collisions + rebase
python -m src.git_safe push                     # backup -> sync -> push -> assert origin==HEAD
```
`ship`/`push` refuse to report success unless `origin/main` actually equals `HEAD`.

## Recovery
- **Undo/lost work:** look in `_ATTIC/quarantine/<timestamp>/` — the exact files, in their paths.
- **Wrecked repo:** `git clone _ATTIC/backups/repo-<newest>.bundle recovered` restores full history.
- **Orphaned commits** (from a stash drop): `git fsck --no-progress` lists dangling commits; `git log <sha>`
  inspects them, `git cherry-pick <sha>` brings one back. Dangling ≠ corruption.

## Never again
- Never `git clean -fd` or `rm -rf` untracked content to "unblock" — use `git_safe sync` (it quarantines).
- Never pass a multi-word/quoted commit message inline to PowerShell — use `git_safe commit/ship -m`.
- Never trust a push you didn't verify — `git_safe push` verifies `origin==HEAD` for you.
