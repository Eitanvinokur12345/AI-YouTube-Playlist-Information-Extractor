# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-720` (dept) · 2026-08-03T04:54:42.053357+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Run PR-Agent in dry-run mode on a single low-traffic branch in the main repo for one week, reviewing only PRs labeled "skip-review," then compare results to the forked repo test to decide next steps.
**Plan:**
1. Identify a low-traffic branch in the main repo to run PR-Agent in dry-run mode for one week.
2. Limit PR-Agent reviews to only PRs explicitly labeled "skip-review" to avoid normalizing noise.
3. Collect data on review quality and false positives from the dry-run test.
4. Compare the dry-run results with the forked repo test to assess real-world impact and team feedback.
5. Evaluate the trade-off between slower feedback and the potential for noise normalization.
6. Decide next steps based on the comparison and evaluation results.
**What changed:** The approach now reviews only PRs labeled "skip-review" to minimize noise and maximize meaningful data collection.
