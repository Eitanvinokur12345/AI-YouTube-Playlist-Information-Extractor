# Power findings — EXCAVA mining its OWN knowledge to improve EXCAVA (2026-07-07)

_Owner directive: with ~13k elements, don't fixate on CortexOS — find several real improvements
(token reduction, a server, other agent OSes, other things). This is the "Power" department's job,
done manually this tick; it should run continuously. Honest element count: ~6,978 indexed +
~6k connectors/skills/tools/prompts/models ≈ **13k** (not 100k)._

## Actionable NOW (free, no owner action) — wire these
1. **Token reduction — "Claude Code Usage Optimization" (3-command workflow) + handoff-docs pattern.**
   EXCAVA already uses handoff docs for context; apply the same discipline to engine prompts: trim
   room/worker prompts, cap history, drop restated boilerplate. Cheap, direct token cut.
2. **Parallel Multi-Agent Task Decomposition ("spin up 50+ agents in parallel").** We already run
   multi-cycle beats + no cross-dept waiting; formalize task decomposition so one big task fans out
   to many small parallel ones (aligns with the huge-task→war-room rule).
3. **Alternative model backends / router.** We already lead with proven engines (groq/sambanova/
   mistral/gh-models); the data has more free backends — expand the pool + smarter routing.

## Needs OWNER (P5d owner-only-high-leverage pitch) — one free account/token each
4. **Always-on server for true cadence:** Modal (free serverless cron) · Ollama self-host (local) ·
   uptime pinger → repository_dispatch. Fixes GH's throttled ~hourly cron. (From last tick.)
5. **Bigger free engine capacity:** more free API keys / OmniRoute gateway — unlocks "dizzying pace."

## Agent OS / framework ideas to study (beyond CortexOS)
- "Everything Claude Code Multi-Agent Setup" (Afan Musthafa) · CrewAI/AutoGen/LangGraph patterns ·
  Multi-Agent Debate Panel · cortextOS. Borrow patterns; EXCAVA's own bus/gate/memory stays the spine.

## The real meta-fix (top priority)
EXCAVA had "Claude Code 24/7 Daemon" and all of the above on its shelf the whole time and never used
its own knowledge on itself — because the **Power department doesn't exist yet**. Build it: a lane
that mines the index for improvements, auto-applies the safe ones (token trims, routing, prompts),
and pitches the owner-gated ones. THAT is the organ that turns 13k elements into a compounding edge.
