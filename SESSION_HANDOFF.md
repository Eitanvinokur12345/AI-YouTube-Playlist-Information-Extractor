# SESSION HANDOFF — start here (new-session continuation format)

_Everything a fresh session needs to continue Excavatortron/EXCAVA with zero context loss.
Last updated: 2026-07-02. Keep this current at the end of every working session._

## 0. FIRST ACTIONS (do before anything)
1. **Load memory** (re-read specifically): `project_excavatortron`, `project-excava-makeit-work`, `project-excava-roadmap`, `project-excava-direction-loop` (⚠ missed once before), `feedback-fable-workflow`, `feedback-nosg`, `feedback-ship-visible-progress`, `feedback-consistency-check`.
2. **Read the plan**: `EXCAVA_PROGRAM.md` (approved-pending program: 56 goals / 9 phases / ask-checkpoints), `PLAN.md` (P/F history), `QUESTIONS.md` (open, non-blocking).
3. **Run the consistency check** (§6) and keep running it after every task.
4. **Don't start Phase 0 until Eitan answers D1–D5** in EXCAVA_PROGRAM.md (esp. D1: cron-heartbeat vs always-on). Everything else can proceed with defaults.

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

## 3. THE PLAN (full steps in EXCAVA_PROGRAM.md)
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
1. Get D1–D5. 2. Start **Phase 0** (unblocks everything). 3. Then P5 early (so Eitan SEES the spine).
4. Keep the consistency check + ask-checkpoints running. 5. Update this handoff at session end.
