# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-671` (dept) · 2026-07-31T20:38:11.663807+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a self-review loop where each prompt engine auto-runs a quality check on its own outputs before routing to the next stage.
2. Deploy a pre-deployment test that runs the quality check against a live stream of fresh, human-annotated outputs from the previous week.
3. Flag discrepancies between the quality check’s verdict and human annotations for review.
4. Continuously update the test set with new human-annotated outputs to catch novel failures.
5. Assign Gauge ownership of maintaining the live test stream and discrepancy flags.
6. Delay deployment of the quality check until the live test stream passes with no unresolved discrepancies.

**What changed:** Switched from held-out known-bad outputs to a live, human-annotated stream to catch novel failures.
