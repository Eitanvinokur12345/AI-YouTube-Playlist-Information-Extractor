# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-617` (dept) · 2026-08-26T03:35:49.651912+00:00
> Participants: Overhaul, Sprocket, Ratchet, Gauge · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on *only* new-contributor PRs for two weeks, then expand to all PRs for one week *only if* reviewer engagement metrics improve by 20% or more.

**Plan:**
1. Enable PR-Agent in shadow mode exclusively for PRs from new contributors (no prior commits in the repo).
2. Monitor reviewer engagement metrics (e.g., comment resolution rate, time-to-review) for two weeks.
3. If metrics improve by ≥20%, enable shadow mode for *all* PRs for one week.
4. If metrics do not improve, extend the new-contributor-only phase by one week and re-evaluate.
5. After the all-PRs test week, analyze full-codebase impact and decide on permanent adoption.
6. Document findings in a public post-mortem for transparency.

**What changed:**
Shifted from full-baseline testing to controlled new-contributor-only phase first, with expansion contingent on measurable reviewer engagement improvements.
