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
