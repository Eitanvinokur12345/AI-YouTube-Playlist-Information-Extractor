# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-551` (dept) · 2026-08-10T08:16:22.401150+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest merged PR first, then expand to 10% of merged PRs after validating accuracy.

**Plan:**
1. Configure PR-Agent to run in shadow mode on the newest merged PR immediately after merging.
2. Log routing errors detected in shadow mode for validation without user impact.
3. After 1 week, review error logs to confirm accuracy and adjust PR-Agent rules if needed.
4. Expand shadow mode to 10% of merged PRs, randomly selected.
5. Monitor performance metrics (false positives/negatives, review speed) for 2 weeks.
6. Iterate on PR-Agent rules based on findings before full deployment.

**What changed:** PR-Agent now validates routing errors post-merge to avoid review noise.
