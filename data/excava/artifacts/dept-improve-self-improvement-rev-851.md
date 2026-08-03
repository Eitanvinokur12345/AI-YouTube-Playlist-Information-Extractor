# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-851` (dept) · 2026-08-03T19:21:52.639055+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent in shadow mode to run on the newest open PR first, prioritizing detection of fresh edge cases before they ship.
2. Immediately after, run PR-Agent in shadow mode on the oldest merged PR to validate against historical edge cases and stale routing/prompt logic.
3. Aggregate results from both runs into a unified report, flagging discrepancies between new and historical behavior.
4. Auto-apply safe changes (e.g., prompt refinements, routing tweaks) where confidence >95% and no conflicts detected.
5. Log all auto-applied changes with diffs and rationale for leadership review.
6. Schedule a weekly recalibration to adjust PR selection criteria based on false positive/negative trends.

**What changed:** Dual-shadow PR-Agent runs (newest open + oldest merged) with auto-apply for high-confidence fixes.
