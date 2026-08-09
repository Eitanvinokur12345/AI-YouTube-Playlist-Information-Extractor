# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-214` (dept) · 2026-08-05T02:32:08.948702+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run PR-Agent in shadow mode on the newest merged PR first.
2. Expand backward in weekly batches of 10 merged PRs.
3. Stop if no new issues appear for two consecutive batches.
4. Log all detected systemic issues for review.
5. Auto-apply safe fixes via PR-Agent where approved.
6. Pitch findings to the team for broader process improvements.

**What changed:** Prioritized systemic issue detection in merged PRs with a clear stopping condition.
