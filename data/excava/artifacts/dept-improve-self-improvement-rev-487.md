# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-487` (dept) · 2026-08-15T20:53:00.389952+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on all PRs—open and merged—for two weeks, logging every suggestion privately, then promote only suggestions that correlate with real fixes to live mode.

**Plan:**
1. Enable PR-Agent in shadow mode on *all* PRs (open and merged) for 14 days.
2. Log every suggestion privately (no team visibility).
3. After 14 days, analyze correlation between suggestions and actual fixes in merged PRs.
4. Promote only suggestions with ≥X% match to real improvements to live mode.
5. Gradually roll out live mode to teams, starting with low-risk PRs.
6. Monitor adoption rates and adjust suggestion thresholds as needed.

**What changed:**
PR-Agent suggestions now require proof of impact before becoming blocking or visible.
