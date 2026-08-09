# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-881` (dept) · 2026-08-09T23:02:49.107782+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest merged PR first, then expand to open PRs only if error rates justify the cost.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on the most recent merged PR.
2. Monitor error rates and systemic routing issues for 2 weeks.
3. If error rate exceeds threshold (e.g., 5% of PRs), expand shadow mode to open PRs.
4. Collect metrics on false positives and review noise during open PR shadow mode.
5. Adjust PR-Agent rules based on findings before full deployment.
6. Document routing error patterns and update team guidelines.

**What changed:** Shadow mode prioritizes merged PRs first to avoid review delays.
