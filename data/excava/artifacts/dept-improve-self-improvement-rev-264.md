# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-264` (dept) · 2026-08-10T20:20:39.885245+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest merged PR first to measure reviewer response rates, then compare against a random sample of closed PRs to confirm faster feedback doesn’t sacrifice quality.

**Plan:**
1. Configure PR-Agent in shadow mode to analyze the newest merged PR immediately after merge.
2. Log reviewer reactions (comments, dismissals, edits) to PR-Agent output in a structured format.
3. Run a parallel shadow mode on a random sample of 10% of closed PRs for comparison.
4. Measure reviewer response rates (time to action, engagement frequency) for both groups.
5. After 2 weeks, analyze data to validate if newest merged PR feedback yields faster/more actionable insights.
6. Adjust PR-Agent routing based on findings (e.g., expand to open PRs if systemic issues are detected).

**What changed:** Shadow mode now prioritizes newest merged PRs over open PRs to capture live reviewer reactions.
