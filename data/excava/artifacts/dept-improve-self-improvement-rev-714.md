# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-714` (dept) · 2026-08-27T14:45:17.527418+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Enable PR-Agent in shadow mode on *all* PRs for two weeks to collect baseline false positive/negative data.
2. After two weeks, switch to running PR-Agent in parallel on a *random 10% of PRs* for one week to compare missed issues against manual review.
3. Aggregate results into a confidence score for PR-Agent’s accuracy (false positives, false negatives).
4. Share findings with teams to align on next steps (e.g., full rollout, adjustments, or further testing).
5. Document edge cases (e.g., new contributors, unassigned PRs) for future iterations.
6. Schedule a review meeting to finalize rollout strategy based on data.

**What changed:** Shadow mode expanded to all PRs for two weeks, followed by random 10% parallel review to validate accuracy.
