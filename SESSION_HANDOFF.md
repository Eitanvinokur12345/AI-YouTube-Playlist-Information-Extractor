# SESSION HANDOFF — start here (new-session continuation format)

_Everything a fresh session needs to continue Excavatortron/EXCAVA with zero context loss.
Last updated: 2026-07-02. Keep this current at the end of every working session._

## 0. FIRST ACTIONS (do before anything)
1. **PROJECT MEMORY MASTER (Phase 0.7, owner law):** before touching ANYTHING run
   `python -m src.project_memory recall "<topic>"` and start from it; after meaningful changes
   `python -m src.project_memory log --what ... --why ...`. Full contract: `PROJECT_MEMORY.md`.
2. **Load memory** (re-read specifically): `project_excavatortron`, `project-excava-makeit-work`, `project-excava-roadmap`, `project-excava-direction-loop` (⚠ missed once before), `feedback-fable-workflow`, `feedback-nosg`, `feedback-ship-visible-progress`, `feedback-consistency-check`.
3. **Read the plan**: `EXCAVA_PROGRAM.md` (now phases 0–9 incl. 0.7 memory-master + 9 omni-source), `PLAN.md` (P/F history), `QUESTIONS.md` (open, non-blocking).
4. **Run the consistency check** (§6) and keep running it after every task.
5. **Decisions:** D1 ✅ cron heartbeat · D2 ✅ direction-loop + change-tutorials, DAEMON-GRADE integration (see QUESTIONS #18/#25) · D3–D5 on defaults · D6 (locked social feeds) default no.

## 0b. SHIPPED 2026-07-03 (second arc): 0.7 + 5 + 9-tier-1, dashboard v64
- **Phase 0.7 memory master**: `src/project_memory.py` + `data/project_memory/` + root
  `PROJECT_MEMORY.md`; auto-ingests commits+bus traces every beat; `recall`/`log` CLI; rollup at 90d.
- **Phase 5 living OS (v64)**: fleet-health card (11 depts, real counters, cooldowns), live bus
  queue with per-task TRACE VIEWER (real "chose X over Y" routing), 📡 OS-events daemon feed,
  floor bots = real registered agents carrying their actual bus task, maintenance overlay on
  safe/kill. Special visitors + job menus still open (P5 leftovers).
- **Daemon step 1 (D2)**: every beat converts pipeline-lane runs into bus events — the OS sees
  all 16 lanes, not just its own ticks.
- **Phase 9 tier-1**: `src/mine_social.py` + `data/social_sources.json` + daily
  `mine_social.yml` → `data/social_intake.json` (intake QUEUE, gated before hub). Reddit=RSS
  (json is 403-blocked), DDG needs the Chrome UA, Jina Reader verified as universal fallback;
  agent-reach (MIT, keyless parts) endorsed by owner — deeper integration next arc.

## 0c. SHIPPED 2026-07-03 (third arc): 3 + 4 + 6-core + G9, dashboard v65
- **Phase 3 creators LIVE** (`src/excava_creators.py`, daily creators.yml): discovery gap-radar →
  data-grounded drafts → independent self-test → publish INTO the project, always labeled
  **"Created by EXCAVA"** (owner rule → guardrail **G-12**); `--test-before-run "<name>"` re-tests
  before first use. **PACKAGES** = owner's term for multi-element bundles. Creators dept staffed.
- **Phase 4 sandbox verify LIVE** (`src/verify_connectors.py`, 6-hourly connectors_verify.yml):
  owner chose test-run EVERYTHING — resolve real install (npm/PyPI keyless) → run in clean-env
  sandbox (no secrets, temp dir, timeout) → `data/connectors_verified.json`; tab shows progress +
  shrinks to verified-only at ≥25 passes (D5). ~10 days of batches for all 1,142.
- **Phase 6 core LIVE**: direction loop ("EXCAVA: direction …" issue command + cockpit 🧭 card +
  beat acknowledgment with EXCAVA's reading) + change tutorials (`data/tutorials.json`, v62-v65
  walkthroughs; the beat NAGS when a build ships without one). Remaining: other 8 systems, HORSE.
- **G9 "Agency/Orchestration"** on the North Star (born at 80/100). PORTABLE_HARNESS.md documents
  the spine as a package (owner: port nothing yet). Source trust-scores seeded
  (`data/source_trust.json`), intake items now carry trust.

## 0a2. GUARDRAILS — READ THIS, information-loss protection (v84, owner law 2026-07-06)
The project must never topple or lose committed work. **Two enforcers, run every beat:**
- **`src/git_safe.py`** — the ONLY safe way to commit/push. Use it: `python -m src.git_safe ship -m
  "msg" -a <files>` (commit via UTF-8 message-file → no PowerShell mangling; then backup → sync →
  push → **verify origin==HEAD**). `sync` QUARANTINES colliding untracked files into `_ATTIC/` (NEVER
  `git clean -fd` — that deletes). `backup` bundles all history to `_ATTIC/backups/`.
- **`src/guardrails.py`** — 12 checks (G-A…G-L) → `data/guardrails_status.json` (shown on the cockpit's
  🛡 Guardrails card) + append-only `data/guardrails_log.jsonl` (git-ignored, per-machine). Full contract
  + recovery steps: **`GUARDRAILS.md`**. Fixes the two mechanical failures that risked the repo.
- **Recovery:** lost file → `_ATTIC/quarantine/<ts>/`; wrecked repo → clone `_ATTIC/backups/repo-*.bundle`.
- **Never again:** no blind `git clean -fd`/`rm -rf` on untracked content; no inline quoted commit
  messages in PowerShell; no unverified push. `_ATTIC/`, `*.bundle`, `data/horse/` are git-ignored.

## 0d. EXCAVA v2 BUILD STATE (2026-07-06, Fable executing EXCAVA_V2_STEPS.md — continue HERE; live build v84)
- **M1 ✅ COMPLETE (v66, dd665b39):** element model (6,422 els, schema+index+set_field) · deep_retrieve
  (full-source enrichment, stubs-first) · discovery_agent (hourly; GitHub/HN/PH/social; live-tested 58 new)
  · verify_elements (2-source+live, rolling+on-access, conflicts noted) · relate (4,796 with related) ·
  prewarm (52 targets) · badges+action-row on all list tabs · #element/<id> detail view · core_spoton.yml.
- **M2 ✅ COMPLETE (v67→fixed in v68, 988f6b1b):** PROTOCOLS.md P1-P14 + SAFE-tripping audit (proven) ·
  excava_engines (9 families, Hermes/OmniRoute optional, fall-through) · excava_leases (dept budgets,
  RPM, Claude-cap) · 38 NAMED agents (Echo/Marrow/Iris/Ledger/Root/Boulder/Chroma/Wire/Ratchet/Bastion/
  Nova + doers/checkers/improvers; --roster) · excava_chat rooms (debate→converge→ARTIFACT:
  package/bus-task/creation; day archives) · workers dispatch/dissolve · rooms advance每 beat ·
  excava_selfimprove (auto budget-shift, room-retire, PITCH filing). Rooms speak on CI beats (engines
  live in secrets; local runs degrade honestly).
- **M3 ✅ COMPLETE (v79, d6e13e0b):** shipped 2026-07-06 (Fable). Slice-1 (v68) = tokens.css + sidebar
  shell + 🗣 Rooms + console hero. Then: **M3.2** monster cast (`src/make_monsters.py`, 11 species ×3
  variants SVG in docs/assets/monsters/, wired into Rooms bubbles + floor stations + bus bots) · **M3.3**
  isometric factory floor + side cutaways (`docs/floor/floor.js`: ground+buildings+cutaway; monster at
  each door; floor clock=M2.7 timing) · **M3.4** animation catalog (11 props, `animForEvent` grounds each
  in a real bus/beat event) · **M3.6** final card visual (refined-neobrutalist, actions on hover/focus) ·
  **M3.7** 📦 Results feed (attributed, day/dept/maker filters, inline artifact bubble, new-badge) ·
  **M3.8** North-Star constellation (9 orbiting goal-stars, size=score, click→goal) · **M3.9** brain
  graph click→explore→"make cluster a package" · **M3.11** steering (header bell+count, dismissible
  approval banner, walk-up herald monster, pitches-as-conversations modal) · **M3.11b** 🎛 Taste tab
  (editable design-taste vs work-taste, feeds HORSE) · **M3.12** mobile pass (read/review/approve/send;
  run buttons off ≤640px; fixed a real [hidden]-override bug on modal/banner/walkup) · **M3.13** ship:
  interactive walkthrough RUNNER (E7 — navigates tabs, spotlights the new thing, Next/Back) + M3 tutorial
  + m3-podcast.wav (System.Speech).
- **⚠ LESSON (cost us v67):** NEVER bump builds/edit utf-8 files via PowerShell Get/Set-Content —
  python utf-8 only. Also: **commit -m messages must NOT contain embedded double-quotes** (PowerShell
  mangles native-exe args → git treats trailing words as pathspecs; use a simple single-line message).
  And: `git stash pop` can OOM on the huge untracked skill trees — extract just your files with
  `git checkout stash@{0} -- <paths>` instead of a full pop, and `git clean -fd skills other-skills
  data/excava/traces data/excava/handoffs backups` before a rebase (untracked CI/agent files block it).
- **M4 ✅ COMPLETE (v83, bc8d6970):** shipped 2026-07-06 (Fable). **M4.2** HORSE (`src/horse.py` — 10
  runners each fully execute the goal on varied free engines, scored vs work-taste, top-3 merged;
  console `/horse` → `excava_channel` HORSE handler → `run_horse`, runs in CI; merged artifact in the
  Results feed) · **M4.3** 🧰 Packages tab (`data/packages.json` 3 seeded kits; assemble w/ loose-name→id
  resolution, pin, edit, Run-all/Run-each, Save-to-EXCAVA; merges server + creations + localStorage) ·
  **M4.4** parent launcher (`launcher/` = **ORBIT**, its OWN calm minimal brand, project-cube grid, full
  context switch, EXCAVA-made projects auto-appear) · **M4.5** hub-as-database (`src/build_hub_api.py` →
  `docs/hub_api.json` public endpoint, packages resolved to element install+url + compact real-element
  index; **wired into the excava beat** so it refreshes every cycle; Packages tab shows endpoint+copy) ·
  **M4.6** ship: "Proof it's real" cockpit card (unattended CI artifact + goal→package path) + M4 tutorial
  + m4-podcast.wav.
- **M4.1 portable activator = [OPUS]-RESERVED** (compressed-hub SKILL.md + live fetch, obeys triggers,
  offline). Fable did NOT build it — it's on the Opus track. This is the ONLY unbuilt core-program step.
- **NEXT (per program): M5 is DEFERRED behind the core; BREADTH is next — B1/B3/B6 FIRST** (expand each
  to full steps, then build), then B2/B4/B5, alongside M5. B1 finish the 52 goals (§9 order) · B3 per-tab
  self-improvement + meta-brain · B6 EXCAVA-as-MCP-server · B2 omni-source tiers 2-3 · B4 portability
  (Budoaris first if asked) · B5 cleanup (formats filter, brain white-nodes, token-split). M5 (external
  actions) stays gated/deferred. Plan files: EXCAVA_V2_STEPS.md (+ADDITIONS §I) — the whole program is
  now complete through M4 except OPUS M4.1; only AFTER the whole program may Fable ask questions / suggest
  adding OpenClaw/Hermes/other tools.
- **Push mechanics learned this session:** commit -m must be a SIMPLE single-line string (NO embedded
  double-quotes — PowerShell mangles native args → git treats words as pathspecs). Before every rebase:
  `git checkout -- data backups` + `git clean -fd data/horse data/excava/traces data/excava/handoffs
  backups skills other-skills` (untracked CI/agent trees block rebase and can OOM `git stash pop` — use
  `git checkout stash@{0} -- <paths>` to extract, never a full pop). git's stderr progress trips
  PowerShell's NativeCommandError but the ref-update line confirms success.
- Gate note: internal gate was CLOSED this session by a REAL data_guard restore (designs.json 242→670)
  — correct behavior; it self-clears on the next clean guard pass.

## 1. WHAT THIS IS
A **personal build-leverage system** for Eitan — a hub of every AI capability (tools/skills/models/MCP/
prompts/commands/designs) mined from ONE YouTube playlist, used with all his tools to build things fast.
**EXCAVA** = the agentic-OS layer orchestrating it (multi-agent orchestrator + harness, using
Excavatortron as its database). Free on GitHub Actions. "LIV" = *live, together* (him + me), not a person.

## 2. CURRENT STATE (2026-07-02)
- Dashboard build **v62** (docs/, GitHub Pages). Theme = "Heavy Machinery" (hazard-yellow + ink neobrutalism, Archivo Black).
- Link coverage **~39%**, climbing (+5%/day target in `data/coverage_log.json`, shown on the 🔋 card).
- EXCAVA cockpit = **home tab**: living floor + task inbox (`data/excava_inbox.json`) + resources card + 8-goal North-Star bars. **Residents** wander every tab (bubbles = real dept status; click → cockpit).
- Activator: portable SKILL.md in `~/.claude/skills/excavatortron-activator/` + Desktop + `docs/activator-skill.md`. **KNOWN BROKEN → Opus 4.8 track (§5).**
- Connectors are **~94% fake** (empty/placeholder install) — Phase 4 fixes.

## 3. PHASE 0 — SHIPPED 2026-07-03 (the OS spine is LIVE)
- **File bus** `src/excava_bus.py`: enqueue → route → claim → hand-off/complete/fail; atomic writes;
  per-task traces (`data/excava/traces/*.jsonl`, incl. "why X over Y" routing events).
- **Hand-off gate (G-4)**: a hand-off missing what_was_done/artifacts/what_remains/context_for_next is
  REJECTED + traced. Docs land in `data/excava/handoffs/` as readable markdown.
- **Registry** `data/excava/agents.json`: 3 tiers, 11 departments mapped 1:1 to the real lanes, scoped
  tools (G-7); `creators` defined but unstaffed = mechanically gated until Phase 3.
- **Orchestrator** `src/excava.py` (same CI entry, same status schema + new `os` section): gate → inbox
  outranks (G-8) → priorities → specialization routing → ≤4 worker ticks/beat → 3-tier escalation → owner.
- **Shared memory**: vector index = read side; `data/excava/state.json` = write side (`bus.remember`).
- **Guardrails**: `data/excava/guardrails.md` (G-1…G-11), enforced in code.
- **Done-criterion PROVEN on real work**: owner inbox task t1 (link coverage) crossed links → memory via a
  real hand-off doc (`data/excava/handoffs/push-link-coverage-towar-31649--01--…`), completed next beat.
  Repeatable proof: `python -m src.excava --selftest` (scratch bus; asserts the doc-less hand-off is rejected).
- Phase-0 workers are ASSESSORS (read their dept's real data, move tasks with grounded docs); heavy work
  still lives in the CI lanes — later phases add execution muscle, the Worker contract stays.

## 3a. PHASES 1+2 — SHIPPED 2026-07-03 (you drive it + safe 24/7), dashboard v63
- **Multi-channel task send**: cockpit send-box → prefilled GitHub issue "EXCAVA: <task>" →
  `excava_inbox.yml` workflow applies it via `src/excava_channel.py`, commits, replies a receipt,
  closes the issue (phone-friendly). Channels: issue / tell Claude / edit inbox file.
- **Kill switch + safe-mode**: `excava_config.json mode` = run|safe|kill (issue "EXCAVA: kill|safe|run"
  or cockpit links). kill = bus untouched; safe = sync+route, no worker acts. Mode chip on cockpit + strip.
- **Priority-weights dial**: `excava_config.json priority_weights` orders which auto-priorities reach
  the bus ("EXCAVA: weight access 95"). Owner inbox always outranks (G-8).
- **Approval queue**: `data/excava_approvals.json` — everything owner-blocked, categorized
  (escalated/outward/unroutable/missing-resource); cockpit widget with per-item approve links
  ("EXCAVA: approve <id>" → re-queued next beat).
- **Phase 2 safety**: lease recovery (claims >6h = crashed worker → re-queued, traced) · bus pruning
  (done >7d → data/excava/archive/) · per-dept usage accounting (state.json) · fail-streak backpressure
  (3 straight fails → 6h cooldown, self-heals) · **continuous self-audit** (guardrails-vs-code + bus
  invariants each beat; problems force AUTO SAFE-MODE).
- **Cockpit v63 shows the spine**: "You drive it" card (send box, mode, weights), OS spine board
  (beat #, per-dept bus counts, beat log, last hand-off link), approval queue. Verified via DOM checks
  (screenshots still time out on the crew animation — known).

## 3b. THE PLAN (full steps in EXCAVA_PROGRAM.md)
9 phases: **P0 OS spine** (bus + shared-memory + orchestrator — build FIRST) → P1 you-drive-it → P2 safe
24/7 → P3 Creators dept → P4 connectors made real → P5 living OS (crew v2) → P6 direction-loop + 10
systems → P7 portability + breadth → P8 North-Star G9 + cleanup. **56 goals** (52 + G53-56 gap-audit),
each mapped to a phase. Core insight: EXCAVA today is a "tab pile," not an OS — build the hand-off +
shared-memory layer before more visual polish. **D1-D5 gate the start.**
Explicitly covered (were implicit, added 2026-07-02b): **dynamic departments** (fully autonomous — P0/P3/P5),
**crystallize repeated patterns into skills** (P3), **beyond-project capabilities** (build MY things=P7,
research & briefs=P3, daily ops/digests=G50/G36). Full coverage audit is in EXCAVA_PROGRAM.md.

## 4. STANDING RULES (non-negotiable)
- **Free only, forever** — "free tier that needs a card on file" = PAID → skip (Bright Data proxy declined).
- **Fable = 60-100%, ALL visuals**; Opus 4.8 = reserved track (§5) + accuracy fixes.
- **Every forward step deepens EXCAVA's integration.**
- **Quality over quantity** (300 verified > 3000 dead).
- **Ask questions, never block** — park in QUESTIONS.md, proceed with defaults, his later answers adjust. Avoid AskUserQuestion for big batches (token cost); use plain text / QUESTIONS.md. **He does NOT want to babysit.**
- **NOSG**: message ends with NOSG → skip options/advice, do the best thing, one-line report.
- **Resource-check before tasks**; **security-first** (untrusted creators); **token-reduction** before heavy work.
- **Ship visible committed progress each session.** Bump `APP_BUILD` + `sw.js` version on every dashboard change.
- **Drain transcripts gently** each session (residential; don't burst → IP block).

## 5. RESERVED FOR OPUS 4.8 (NOT Fable)
SKILL.md/activator working end-to-end · "Open code" (github.dev) button fix · preview <3s + Arena images
prioritized · data-retrieval accuracy + fixing anything Fable built inaccurately.

## 6. CONSISTENCY CHECK (after EVERY task — memory `feedback-consistency-check`)
After each task, before moving on, verify + state in ONE line: (a) it advances a specific
EXCAVA_PROGRAM phase/goal; (b) it contradicts NO decision/answer Eitan gave; (c) it respects §4. If
inconsistent → flag + fix before proceeding.

## 7. REPO MECHANICS
- Repo `C:\Users\eitan\AI-YouTube-Skills` · remote `Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor` · branch `main` · Pages: `.../AI-YouTube-Playlist-Information-Extractor/docs/`.
- **Push pattern** (dirty generated files block otherwise): add → commit → `git stash -u` → `git pull --rebase` → `git push` → `git stash drop`.
- `data/*.json` update in CI hourly — don't commit local test copies; revert them.
- Preview: launch config `dashboard` (python http.server 8787, root=repo). Crew animation makes screenshots time out → verify via `preview_eval` DOM queries.
- Commit trailer: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` (Opus on that track).

## 8. NEXT SESSION
1. **Phases 3+4** per sequencing (creators dept behind the gate; connectors made real + sandbox
test-runs). 2. P5 leftovers: job menus on residents, special visitors, per-dept animation vocabulary.
3. **Phase 9 deepening**: wire `social_intake.json` consumption into the mining lane's verify+security
gate (intake → hub); integrate agent-reach's keyless tools; Eitan's channel/subreddit list (Q22).
4. **Phase 6 start (D2)**: direction-loop + change-tutorials, daemon-grade (see QUESTIONS #25).
5. Transcript drain: 2026-07-03 run hit a pre-existing IP block after 4 videos (auto-stopped correctly);
1,389 still lack real transcripts — next residential session, retry gentler (`--sleep 6 --limit 60`).
6. Keep the consistency check + ask-checkpoints + PROJECT_MEMORY contract running. 7. Update this
handoff at session end.
