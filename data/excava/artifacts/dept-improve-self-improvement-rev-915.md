# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-915` (dept) · 2026-08-05T03:09:32.385457+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest merged PR first, then expand to older unmerged PRs.

**Plan:**
1. Configure PR-Agent in shadow mode for the newest merged PR.
2. Log all findings (issues, suggestions, false positives) without applying changes.
3. Review logs to validate tool accuracy against real-world feedback loops.
4. Expand shadow mode to the oldest unmerged PR to test systemic issue detection.
5. Compare findings between merged and unmerged PRs to refine routing/engines.
6. Schedule a review of auto-apply rules based on shadow mode insights.

**What changed:** Shadow mode prioritizes newest merged PR first, then older unmerged PRs.
