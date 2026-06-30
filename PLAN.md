# Excavatortron / EXCAVA — working plan

_Last updated: 2026-06-30. This is the portable plan so the project isn't trapped in one chat thread._

## What this is (purpose)
A **personal build-leverage system** for Eitan (others later): a hub of every AI capability
(tool / skill / model / MCP connector / prompt / command / design) that he can **use, with all his other
tools, to actually build the things he wants** — fast. It self-runs for free in the cloud (GitHub
Actions) and is meant to *do*, not just list.

## The 6 goals (concepts, not features) — honest status
| Goal | Concept | Status |
|---|---|---|
| G1 Omniscience | know every capability, current | ~22% (349/1555 videos analyzed) |
| G2 Zero friction (know→do) | one step to activate in any tool | ~15% (activator emits text/links, doesn't *do* setup) |
| G3 Truth & access | every entry real, verified, usable | ~18% (≈4 of 5 items have no working link) |
| G4 Autonomy | runs/grows/self-corrects free | ~80% — works (the win) |
| G5 Leverage | makes you faster to build | ~10% — not yet built *through* |
| G6 Open infrastructure | machine-readable platform | ~50% (JSON exists; only the dashboard consumes it) |

**Reality: ~85% built, ~30% working.** Huge surface, thin depth. Only G4 (autonomy) is healthy.

## The core diagnosis — speed is a MANAGEMENT problem, not a power problem
The system's own `priorities.json` says "add Gemini keys to speed it." That's wrong. The real
bottlenecks:
1. **Watching video to extract text facts** (~minutes/video) instead of fetching a **transcript** and
   analyzing text (~1s on a fast engine). Transcripts are IP-blocked from the cloud → use **Bright Data**
   (residential, token added) to fetch them. Biggest single unlock.
2. **One LLM call per item** → batch ~25/call.
3. **Serial HTTP verification** → verify in parallel (thread pool).
4. **Slow grounded-Gemini for everything** → fast engines (Cerebras ~2000 tok/s, Groq) first; grounding
   only for the hard residue.
5. **Cron + 60-min job caps** throttle throughput regardless of key count.

## Plan — "MAKE IT WORK" (freeze new features until F1+F2 done)
### F1 — Speed / throughput (in progress)
- [x] Resolver rewrite: batch 25/call + parallel verify + fast-engine-first (grounding = residue only).
- [ ] Transcript lane via Bright Data → fast text analysis instead of watching video (needs cloud verify).
- [ ] Raise per-run limits / cadence once per-item cost is low.
- **Targets:** link coverage 18% → 90%; videos 22% → 80% — in weeks, not months.

### F2 — Real access / activation (the actual product)
- The activator/EXCAVA **performs setup in-session** (the setup-recipes already on 1,637 items feed it);
  links only for unavoidable external steps (signup/API key). Prove "know → do" end-to-end on the now-linked items.

### F3 — Resume the rest (only after F1+F2)
- Competitor-directory ingestion (fast way to fill coverage; dedup hard).
- Designs polish; EXCAVA real autonomy — stays gated until **G3 ≥ 70** (its own rule).

## Deferred (build after the program; see memory `project-excava-roadmap`)
- **EXCAVA "HORSE":** on activation, fan out ~10 agents w/ different tool-sets → merge best parts by base
  values into one final result; simple portable activator; trigger word HORSE.
- **Activator overhaul + 30 questions + live examples.**
- **Run a repo DIRECTLY** (opensrc.sh + graphify) → pre-prepared ready-to-run env.
- **Per-tab self-improvement** + a **new-source-hunting** protocol.
- Split token-reduction into 2 skills (heavy/light).
- Deep EXCAVA-integration design conversation (it changes the whole structure).

## Principles
- Make it **work** (access + completeness) before adding surface.
- **Quality over quantity** — 300 verified+activatable beats 3,000 dead names.
- Token-reduction protocol before heavy work (ironclad).
- Show the list, get approval, then build. Ship visible, committed progress each session.
