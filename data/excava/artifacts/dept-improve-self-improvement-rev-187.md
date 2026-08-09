# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-187` (dept) · 2026-08-09T11:04:59.633684+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy PR-Agent in shadow mode on the newest open PR within 24 hours.
2. Monitor caught routing errors and validate fixes via shadow mode reports.
3. Expand shadow mode to all open PRs within 1 week, prioritizing high-risk routing changes.
4. After 2 weeks of stable open-PR shadow mode, enable shadow mode on the newest merged PR.
5. Compile a weekly report of caught issues and scaling progress for team review.
6. Draft a runbook for full shadow-mode rollout to all PRs within 1 month.

**What changed:** Shadow mode prioritized open PRs first to prevent routing errors before shipping.
