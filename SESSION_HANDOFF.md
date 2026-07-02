# SESSION HANDOFF — start here (new-session continuation format)

_Everything a fresh session needs to continue Excavatortron/EXCAVA with zero context loss.
Last updated: 2026-07-02. Keep this current at the end of every working session._

## 0. FIRST ACTIONS (do before anything)
1. **Load memory** (re-read specifically): `project_excavatortron`, `project-excava-makeit-work`, `project-excava-roadmap`, `project-excava-direction-loop` (⚠ missed once before), `feedback-fable-workflow`, `feedback-nosg`, `feedback-ship-visible-progress`, `feedback-consistency-check`.
2. **Read the plan**: `EXCAVA_PROGRAM.md` (approved-pending program: 56 goals / 9 phases / ask-checkpoints), `PLAN.md` (P/F history), `QUESTIONS.md` (open, non-blocking).
3. **Run the consistency check** (§6) and keep running it after every task.
4. **D1 ANSWERED 2026-07-03: cron heartbeat** → **Phase 0 SHIPPED same day** (see §3). D2–D5 still open in QUESTIONS.md §F (D2 — his 2-3 alignment systems — has no default and gates Phase 6 only).

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
1. Get D2 (his 2–3 alignment systems; D3–D5 proceed on defaults). 2. **Phase 1 + 2** (task-send form →
bus, kill switch, approval queue; leases/ceilings, crash recovery, bus pruning). 3. Then **P5 early** —
wire the cockpit/residents to the REAL bus (`excava_status.json` already carries the new `os` section:
beats, per-department load, beat_log, last hand-off) so Eitan SEES the spine.
4. Transcript drain: 2026-07-03 run hit a pre-existing IP block after 4 videos (auto-stopped correctly);
1,389 still lack real transcripts — next residential session, retry gentler (`--sleep 6 --limit 60`).
5. Keep the consistency check + ask-checkpoints running. 6. Update this handoff at session end.
