# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-912` (dept) · 2026-08-03T18:44:52.232086+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Configure PR-Agent in shadow mode for the newest open PR.
2. Monitor shadow outputs for divergence or errors in routing/prompts.
3. If outputs are clean, proceed to shadow mode on the oldest merged PR.
4. Compare results between both PRs to validate edge cases and fresh logic.
5. Prioritize fixes for the newest PR’s routing if outputs diverge.
6. Document findings and apply safe changes to prompts/engines/routing.

**What changed:** Shadow mode testing order updated to newest open PR first, then oldest merged PR.
