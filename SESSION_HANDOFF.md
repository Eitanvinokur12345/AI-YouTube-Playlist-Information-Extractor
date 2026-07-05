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

## 0d. EXCAVA v2 BUILD STATE (2026-07-05, Fable executing EXCAVA_V2_STEPS.md — continue HERE)
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
- **M3 slice 1 ✅ (v68, 2e1e03b2):** tokens.css design system · sidebar shell (wide screens) · 🗣 Rooms
  messenger tab (war-room round table; agent·engine·ms badges; suited leads raised) · console hero
  (dept-route/mic/attach/slash→P6 triggers/away-digest).
- **⚠ LESSON (cost us v67):** NEVER bump builds/edit utf-8 files via PowerShell Get/Set-Content —
  python utf-8 only. v67's mojibake was restored from git (dd665b39) and re-applied.
- **M3 REMAINING:** M3.2 monster cast (SVG/code-drawn, free-first; show Eitan samples, no gate) ·
  M3.3 isometric floor + cutaways · M3.4 animation catalog (11) · M3.6 card final visual · M3.7 results
  feed · M3.8 North-Star constellation · M3.9 brain graph→package · M3.11 steering banner/bell/monster-
  walks-up · M3.11b editable taste panel (design vs work) · M3.12 mobile pass · M3.13 ship.
- **THEN:** M4 (activator [OPUS], HORSE, packages UI, launcher own-brand, hub-API, prove-real) ·
  M5 deferred · breadth B1/B3/B6 first. Plan files: EXCAVA_V2_STEPS.md (+ADDITIONS §I design direction).
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
