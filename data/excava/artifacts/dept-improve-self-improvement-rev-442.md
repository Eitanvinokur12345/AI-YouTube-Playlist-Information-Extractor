# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-442` (dept) · 2026-07-28T23:39:04.216434+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Design a 72-hour triple-arm A/B test with 15% of users split into:
   - Arm 1: Current prompt (forced feed)
   - Arm 2: Revised prompt (forced feed)
   - Arm 3: Revised prompt (unforced)
2. Metrics tracked: engagement (clicks, dwell time) and feed quality (relevance, satisfaction scores).
3. Gauge executes the test, ensuring randomization and blinding where possible.
4. Post-test analysis isolates prompt effects from user behavior by comparing forced vs. unforced arms.
5. Roll out the winning prompt to 100% of users if statistically significant improvements are observed.
6. Document findings in a shared repo for future prompt iterations.

**What changed:** Added a triple-arm test to disentangle prompt efficacy from user behavior.
