# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-931` (dept) · 2026-08-03T19:03:21.015632+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent in shadow mode to run on both the oldest merged PR and the newest open PR simultaneously.
2. Capture and compare PR-Agent’s outputs (feedback, edge cases, routing paths) for both PRs in a single report.
3. Prioritize validation of stable routing paths using the oldest merged PR’s results.
4. Log and analyze fresh edge cases from the newest open PR’s results separately.
5. Use the comparison to identify discrepancies between stable and new routing behavior.
6. Iterate on prompts/engines/routing based on findings, applying safe changes to both PRs if validated.

**What changed:** Parallel shadow-mode validation of oldest merged and newest open PRs for stable and edge-case routing comparison.
