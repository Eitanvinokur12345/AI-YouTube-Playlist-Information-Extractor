# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-871` (dept) · 2026-08-09T22:24:33.464022+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest merged PR first, then expand to weekly random 10% of merged PRs if results prove useful.

**Plan:**
1. Configure PR-Agent to run in shadow mode on the newest merged PR daily.
2. Log routing errors and false positives in a dedicated tracking issue.
3. After 2 weeks, review the report (owned by Overhaul) to assess signal-to-noise ratio.
4. If ≥70% of findings are actionable, expand to weekly random 10% of merged PRs.
5. Disable shadow mode on open PRs entirely during this phase.
6. Automate weekly report generation and share with the team.

**What changed:** Shadow mode now targets merged PRs first, reducing noise while preserving systemic error detection.
