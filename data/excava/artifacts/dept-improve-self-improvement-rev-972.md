# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-972` (dept) · 2026-08-08T11:04:01.473582+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent in shadow mode to run on the newest open PR within 24 hours.
2. Log all PR-Agent outputs and incident reports in a dedicated tracking issue.
3. Measure post-merge incidents for 30 days, comparing against baseline metrics.
4. After 30 days, expand shadow mode to merged PRs if incident reduction is ≥20%.
5. Document routing/quality issue patterns and update auto-apply rules.
6. Overhaul reviews and approves the shadow-mode expansion criteria.

**What changed:** PR-Agent shadow mode prioritized open PRs to catch flaws earlier, with incident tracking for 30 days.
