# EXCAVA — laws, guardrails and working rules

_Assembled from the EXCAVA repo for NotebookLM upload._



---

# ===== FILE: PROTOCOLS.md =====

# PROTOCOLS.md — Eitan's approach, codified as law (EXCAVA v2 M2.0)

_Every agent reads this before acting. The orchestrator self-audits against it every beat
(`_audit_spine`); drift trips SAFE mode. Changing a protocol here without the owner's say-so
is itself a violation._

## P1 — Free-only forever
No action may require payment or a card. A "free tier needing a card" = paid = skip. Design
tooling included: test free tools first; a specific/paid tool only if the result genuinely
can't be excellent without it.

## P2 — Depth before breadth
Make a small set genuinely real before adding scope.

## P3 — Task-relative value (hard rule)
No global "best/better." Never bury or prune an element for being low-rated — a "1" may be
perfect for one niche task; that is WHY holding many elements is worthwhile. Prune ONLY
dead/fake/empty elements. Comparison and effectiveness scoring are always per-task.

## P4 — Real, not display
Every feature must actually do / open / run. Visualization that does nothing useful is a bug.

## P5 — Autonomy with three pitch-gates
Agents may autonomously build and change almost anything (features, outlines/formats,
prompts, commands, designs, packages). Only three things need Eitan's OK, each delivered as
a PITCH conversation: (1) building a brand-new TOOL, (2) any OVERHAUL (a better working
method / full redesign / a change to how agents work), (3) DEEPER ACCESS to Eitan's computer.

## P6 — Trigger words
Default on activation = find or build the right PACKAGE and act. `NOSG` = skip options, do
the single best thing, one-line report. `HORSE` = 10 agents each FULLY EXECUTE the goal,
then merge the best of the RESULTS (not the plans), tuned to Eitan's taste. `PLAN` = show
the plan first instead of acting; absent PLAN = act silently in the background. `RESEARCH`
= deep multi-source brief. `WATCH` = ongoing tracking of a topic/source.

## P7 — Offline/online parity
Every EXCAVA action runs at the same speed and quality whether Eitan is present or not;
agents converse identically in his absence; all chats archived and scrollable by day.

## P8 — Elements & packages
"Elements" = every information item in the hub. "Packages" = bundles of elements for a task.
Every element ALSO stands alone with direct access — never hidden inside packages only.

## P9 — Provenance + independent test
Anything created enters the project labeled "Created by EXCAVA"; an independent test re-runs
before its first use. Publishing beyond the project stays behind the outward gate.

## P10 — Recall before change; log the WHY
Every tool (including EXCAVA's agents) recalls from the project memory master before
changing anything and logs a one-line WHY after (`PROJECT_MEMORY.md`).

## P11 — Consistency check every task
Against the goals + these protocols; flag + fix drift before moving on.

## P12 — Security first
Untrusted content is gated (`security_preflight`); keys/data never leak; the sandbox tests
before anything runs.

## P13 — Visible work
Agents work out loud in conversations; Eitan is the boss watching employees, with a
one-sentence "what they debated since you left" digest.

## P14 — Quality over quantity
300 verified beat 3,000 dead — reconciled with P3: keep niche elements, cut only dead ones.
The STRICT quality bar applies to things EXCAVA CREATES (small prompts/commands may be
light); existing elements are kept unless dead/fake/empty.

## Pace addendum (owner, 2026-07-04)
Fully parallel, non-blocking, no concurrency cap (organization = agent/department/room).
Creations: quality first, never > ~1 hour, target < 30 minutes. Anything Eitan-facing
(console, his tasks, approvals) responds FAST. Visible timing on the floor.



---

# ===== FILE: GUARDRAILS.md =====

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

## The guardrails (17, `python -m src.guardrails`)
_Table below covers G-A…G-L + the two newest; G-M…G-P (movement/disk/local-drain/beat-heartbeat)
are documented in their own docstrings in `src/guardrails.py` — this table has fallen behind that
file more than once and the code is always the source of truth for the live count._
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
| G-Q | Core-spoton heartbeat freshness | the hourly M1.C pipeline (discovery/deep-retrieve/verify) silently stalling — cron disabled, a step now raising before Commit, or a bad rebase — with nothing watching for it (added fire 26, 2026-07-27, after fire 25 found the sibling octal-arithmetic bug) |

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



---

# ===== FILE: CLAUDE.md =====

# CLAUDE.md — how Claude works with Eitan

_General, cross-project guidance. Deliberately **not** project-specific: Eitan will use Claude on
other projects, and this file is meant to travel with him. Anything specific to the
YouTube→hub tracker lives in **`ANALYZE_SPEC.md`** (the analysis-stage spec) and the EXCAVA
plan files (`EXCAVA_END_PLAN.md`, `EXCAVA_V2_STEPS.md`, `PROTOCOLS.md`)._

_Split out of the old project-specific CLAUDE.md on 2026-07-30 at Eitan's request._

---

## 1. How Eitan wants to be worked with

- **Do the work, don't narrate the plan.** Deliver the thing. A plan is only worth writing when
  the decision genuinely belongs to Eitan.
- **Harsh, honest criticism — of your own work, every time.** Say what is weak, half-done,
  or merely decorative. Never present plumbing as product. "Progress" means *Eitan can do
  something new*, never "a commit happened."
- **Never claim something works without checking.** Run it, read the output, then say so. If a
  check failed or was skipped, say that plainly.
- **Push back when he is wrong**, and change position when he is right. He challenged the M2
  timeline on 2026-07-30 and was correct — the plan was stale. That exchange is the standard.
- **Full sentences in reports to him; terse prompts for agents.** His reports are for a human.
- **Teach as you go.** Explain the reasoning, not just the result — he is learning the stack.
- **Questions are his.** Propose a verdict, let him decide. Ask clickable questions one or two
  at a time; large batches do not get answered. Never impose a generated set of decisions.

## 2. Working rules that apply on every project

- **Reuse before building.** Find the existing tool, library, or file first. Minimal diffs.
- **Free-only unless he says otherwise.** No paid services, no new heavy dependency without
  raising it first.
- **One increment at a time, ending wired + visible.** Nothing orphaned, nothing half-built.
- **Verify the read side.** Whatever you changed, look at what a user would actually see.
- **Log WHY, not just what.** A change nobody can explain later is a liability.
- **Small, safe, reversible** beats clever. When unsure, do the reversible thing and flag it.

## 3. Safety rules — these exist because something broke

- **Quarantine, never delete.** Never `rm -rf` or `git clean -fd` to unblock something. Move it
  aside and keep it. Nothing may permanently destroy uncommitted content.
- **Never force-push.** Never rewrite shared history.
- **Never print or commit secrets.** Keys live in environment variables / CI secrets only.
- **Verify a push actually landed** rather than trusting the command returned.
- **Look before overwriting.** Read the file first; a blind write loses work.

## 4. Environment quirks worth remembering

- **On Eitan's local PC loop, never run `git` directly in a Bash command.** The app gates
  `cd`+`git` as a hook-execution risk and an unattended session **freezes** on it. Route git
  through Python. This does not apply to cloud sessions, where git runs normally.
- **Unattended sessions must not use browser tools** — they can prompt for permission and are
  flaky headless. Verify via CLI and data assertions instead.
- **Recurring session jobs are session-only**: they die when the app closes and expire after
  7 days. Long-running automation belongs in CI or a cloud scheduled task, not a session cron.

## 5. This repo specifically

Two products in one repository:

- **EXCAVATORTRON** — the hub: ~11k mined AI elements (skills, tools, prompts, commands,
  connectors, designs, formats, models, creations).
- **EXCAVA** — the agent orchestra that generates tools and projects by orchestrating free OSS
  tools, free models, and the hub. Purpose is to assist Eitan's work; "sellable" is a quality
  bar, not a plan to sell.

| If you are doing this | Read this |
|---|---|
| Analyzing videos into the hub | **`ANALYZE_SPEC.md`** (authoritative) |
| Building EXCAVA | `EXCAVA_END_PLAN.md`, `EXCAVA_V2_STEPS.md` |
| Anything at all | `PROTOCOLS.md` (P1–P14, the laws) |
| Running the autonomous loop | `data/excava/away_mode.json` + `AWAY_MODE.md` |
| Git / recovery | `GUARDRAILS.md` — always ship via `python -m src.git_safe ship` |
| What happened recently | `PULSE.md`, `AWAY_LOG.md`, `SESSION_HANDOFF.md` |
| Open decisions | `QUESTIONS.md`, `data/excava/overhaul_decisions.json` |
| Eitan's own backlog asks | `data/excava/owner_requests.json` — never auto-pruned |

**Start any autonomous fire with:**

```
python -m src.standing_checks        # remote/upstream/guardrails + loop-contract status
python -m src.loop_contract status   # carry-over increment + meta-fire cap
```



---

# ===== FILE: AWAY_MODE.md =====

# GO AWAY MODE — what the routine actually performs

> **UPDATED 2026-07-30 (same day).** Eitan made the mode **PERMANENT** and added phone push.
> The §7 recommendations below are no longer recommendations — three of them are BUILT:
> `src/loop_contract.py` (contract acknowledgement, carry-over increment, meta-fire cap), wired
> into `src/standing_checks.py`. Cadence is now **2h unattended / hourly when Eitan is present**.
> The old exit condition is gone: the mode never ends, it only switches cadence.
> Sections 0-6 describe the run that ENDED 2026-07-30 and are kept as the evidence base.

_Report prepared 2026-07-30 for Eitan, after away mode ran 2026-07-21 → 2026-07-30 (81 fires).
This documents the routine as it REALLY behaves, verified against the repo — not as it was
imagined. The contract itself lives in `data/excava/away_mode.json`._

---

## 0. The headline finding — it is a PROMPT contract, not a program

`away_mode.json` is read by **nothing**. A grep for `away_mode` across every `.py`, `.yml`,
`.js` and `.json` in the repo returns the file itself and no consumer.

**Implication:** away mode is a set of instructions a Claude session *chooses* to read and obey.
No code enforces a single rule in it. If a session never opens the file, every rule below is
silently inactive — and nothing anywhere would report that. The 81 fires complied because each
one read the contract, not because anything made them.

This is the routine's deepest structural weakness and it is worth fixing before the next away
period (see §7).

---

## 1. What "go away mode" actually switches on

Three independent layers run while you are away. **Only the first is away mode.** The other two
run identically whether you are here or not — a fact worth knowing, because it means the program
does not stop when the loop dies.

| Layer | What runs it | Survives your PC being off? | Survives the Claude app closing? |
|---|---|---|---|
| **1. The session loop** (away mode proper) | `CronCreate` hourly job, **session-only** | yes (cloud sessions) | **NO — dies silently** |
| **2. The GitHub Actions beat** | 19 scheduled workflows | yes | yes |
| **3. The local drain** | Windows scheduled task on EITAN-PC + Ollama | **NO** | yes |

Layer 2 is the real 24/7 floor. Layer 3 died during this away period — it has been stale
**107 hours** (guardrail G-O has been flagging it), because your PC was off. Nothing about away
mode can prevent that.

### The 19 scheduled CI lanes (layer 2)

```
excava_beat        */10 * * * *     core_spoton     5 * * * *      links          15 * * * *
bulk_analyze       30 */2 * * *     analyze         0 */3 * * *    news           0 */6 * * *
connectors_verify  10 */6 * * *     transcribe      0 4 * * *      visual         30 2 * * *
gemini_video       0 5 * * *        mine_social     20 6 * * *     sources        0 6 * * *
fetch              0 6 */2 * *      creators        45 7 * * *     mine           0 10 * * *
discover           0 1 * * 0,2,4    review          0 23 * * 3,6   improve        0 20 * * 6
codeql             0 22 * * 6
```

---

## 2. The per-fire routine (what one fire performs, in order)

Every fire executes this sequence. It is defined in `away_mode.json.rules[0]`.

1. **Standing checks** — `python -m src.standing_checks`: snapshots `origin/main` before and
   after a real fetch (to answer "is a stale local ref hiding lost work?" deterministically
   rather than by eyeball), calls `git_safe.ensure_upstream()`, then folds in
   `guardrails.run()`. Writes `data/standing_checks.json`.
2. **ONE increment** that ends **wired + visible**, on a **non-brain front**. One only — the
   small-increment rule exists so an interrupted fire never leaves a half-built system.
3. **Verify the READ side via CLI/data assertions — explicitly NOT the browser.** Browser tools
   can prompt for permission and are flaky headless; an unattended fire that triggers a prompt
   **freezes**.
4. **Log WHY** — to `AWAY_LOG.md` and `python -m src.project_memory log`.
5. **Ship** via `python -m src.git_safe ship` (commit through a UTF-8 message file → backup →
   sync → push → assert `origin == HEAD`).
6. **Harsh criticism of both** the increment and the process.

Cadence: **hourly** ("conserve resources; no one is watching for fast feedback").
Every **10th** fire additionally writes a consolidated heartbeat summary — 17 of these fired.

---

## 3. The hard prohibitions

These are the rules that exist because something already went wrong once.

- **NEVER call `AskUserQuestion`.** Any question — spontaneous or part of the plan — is appended
  to `QUESTIONS.md` with a chosen default, and the fire proceeds on that default. Nothing ever
  blocks on you.
- **NEVER run `git` directly in a Bash command.** This is the non-obvious one. The app gates
  `cd`+`git` as a hook-execution risk and **the unattended loop freezes on it** — a screenshot
  proved a fire stalled mid-standing-check. All git is routed through Python
  (`python -m src.git_safe …`), which the gate cannot see inside. `cd`-before-`python` is fine;
  only `cd`-before-`git` is gated.
- **Never** `git push --force`, `git clean`, or `rm -rf`. Quarantine, never delete — anything in
  the way moves to `_ATTIC/quarantine/<timestamp>/` and is kept forever.
- **Non-brain fronts only** — M1 polish, M3 shell/design, the Hub, self-improvement dept,
  per-department executors, deterministic enrichment, audit-backlog machinery, cleanup.
  Explicitly **not** the engine/brains subsystem.

---

## 4. Entry and exit

- **Entry:** you say you are going away; `away_mode.json` is written with `away: true`, the
  date, your instruction verbatim, and the rules.
- **Exit:** **only** an explicit message from you indicating you are back. There is **no expiry**.
  Fire 47 hit the stated "~1 week" mark, flagged that the calendar alone is not a stop signal,
  and correctly kept running. Away mode ran 9 days on a "~1 week" instruction.
- On exit the routine must present every batched question from `QUESTIONS.md` and resume
  interactive cadence. (Done 2026-07-30.)

---

## 5. What the 81 fires actually produced

**Real infrastructure wins:**
- `src/pulse.py` → `PULSE.md` — the one-glance "is it actually working?" answer. Its first run
  immediately exposed a hidden regression the green dashboard was concealing.
- `src/standing_checks.py` — the one-command session-start check (queued twice before it was built).
- `src/github_meta_enrich.py` — deterministic, keyless stub-filling from GitHub's REST metadata,
  wired hourly so enrichment no longer depends on your PC being on.
- **Silent-commit-loss fix** — found via live Actions logs: a job reported success on every step
  while a full day's mining was discarded (rebase conflict → detached HEAD → `git push || echo`
  swallowed the failure). Fixed and verified against a real bare remote; rolled out to the
  highest-cadence lanes.
- New guardrails **G-Q** (core_spoton heartbeat), **G-R** (push-safety in every shipping lane),
  **G-S** (no conflict markers in logs), **G-T** (workflow lane heartbeat).
- Branch sweep — recovered real work stranded on an orphaned branch that never reached `main`.
- Anti-boilerplate gate moved to point-of-creation.

**The honest weakness, by the fires' own repeated admission:** a large share was **meta-plumbing
about the loop itself** rather than the program. Fires 6, 7, 8, 9 and 10 were consecutively git
hygiene and observability; each one's self-criticism says so explicitly ("the FOURTH fire in a
row that is meta/plumbing... the actual program — Hub content, enrichment, departments, M1–M5
milestones — untouched again"). The routine is good at noticing this and bad at stopping it,
because "one small safe increment, unattended" structurally selects for plumbing over product.

---

## 6. What it left open

- **25 of 31** numbered questions unanswered; **118 of 122** audit items undecided.
- ~13 stray `claude/kind-shannon-*` branches of unknown content, never swept.
- 12 of 19 workflow files still carry the silent-commit-loss pattern (the sub-6h lanes are done).
- The branch-vs-main ship convention — flagged by three separate fires, still unconfirmed.
- Enrichment: 2,019 stubs remain; the local drain that was meant to grind them down is dead.

---

## 7. Assessment — what I would change before the next away period

1. **Enforce the contract in code.** Add an `away` check to `standing_checks` so a fire that has
   not read `away_mode.json` says so loudly. Today compliance is voluntary and unverifiable.
2. **Alarm on loop death.** The session cron is session-only and "the app must stay open." If it
   closes, the loop stops and *nothing reports it* — you would find out by noticing silence.
   A guardrail comparing away-fire cadence against wall-clock would catch it.
3. **Give the fence an expiry.** "Non-brain fronts only" was correct on day 1 and stale by day 9 —
   it is what left the M2 class collapse unstarted. Scope fences should carry a review date.
4. **Cap consecutive meta-fires.** If N fires in a row touch only the loop's own machinery, force
   the next one onto product. The fires diagnosed this pattern five times and never broke it.
5. **Make "proceed on default" visible.** 25 accumulated defaults is a lot of unreviewed decision
   surface. A running count in `PULSE.md` would keep the debt honest.

---

_Sources: `data/excava/away_mode.json`, `AWAY_LOG.md` (304 fire references), `PULSE.md`,
`QUESTIONS.md`, `GUARDRAILS.md`, `.github/workflows/*.yml`, `data/excava/local_worker.json`._


---

## 8. What changed on 2026-07-30 (Eitan's decision)

**Always-on.** The mode no longer has an exit condition. It runs permanently and switches cadence
based on whether Eitan is in the session — hourly when he is, every 2 hours when he is not.
Rationale: he is rarely at the computer, so a loop that waits for him to appear wastes most of the
day.

**Phone push, tiered.** `PushNotification` reaches his phone when Remote Control is connected.
The tiering is the important part, and it is a deliberate departure from "notify me about even the
smallest detail":

| Tier | What | Why |
|---|---|---|
| **Push now** | blocks the increment with no safe default · a P5 pitch-gate · anything irreversible · loop/repo at risk · an owner request blocked | genuinely worth an interruption |
| **Batch, no push** | anything with a sensible default · style/naming/cosmetics · routine progress | recorded in `QUESTIONS.md`, visible, not interrupting |
| **Daily digest** | one line, once a day | keeps "the smallest detail" reachable without one push per detail |

Cap: 3 non-blocking pushes/day; blockers unlimited. **An owner who learns to ignore pushes is
worse than no pushes at all** — that is the failure this tiering prevents.

**Known gap:** `PushNotification` is a Claude Code *session* tool. The GitHub Actions beat cannot
call it, so a lane failing overnight in CI still cannot reach his phone. That needs a separate
transport (feature-inventory item 65, Telegram push) and is **unbuilt**.

**The three §7 fixes, now real** (`src/loop_contract.py`):
- `ack` — a fire records that it read the contract; `standing_checks` flags one that did not.
- `start`/`note`/`finish` — a carry-over increment can span several fires, so real work no longer
  has to fit inside one fire's window.
- meta-fire cap — after 3 consecutive fires touching only the loop's own machinery, the next fire
  must advance the product. This is the counter that the previous run lacked while diagnosing its
  own meta-bias five times.

**Retired:** the "non-brain fronts only" fence. Correct on day 1, stale by day 9, and the reason
M2's class collapse sat unstarted. Any future fence must carry a `review_by` date.
