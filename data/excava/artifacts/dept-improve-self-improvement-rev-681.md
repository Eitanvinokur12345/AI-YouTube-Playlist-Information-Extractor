# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-681` (dept) · 2026-07-28T23:57:50.311563+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 72-hour A/B test on a random 15% slice, logging both forced and voluntary interactions to isolate prompt engine impact from interaction fatigue.

**Plan:**
1. Randomly select 15% of users for the A/B test (50/50 split: forced feed vs. voluntary cohort).
2. Deploy the new prompt engine to the test group while logging engagement metrics separately for forced and voluntary interactions.
3. Measure core engagement (e.g., session length, retention) and interaction fatigue (e.g., churn, opt-out rates).
4. Compare results against a control group (users with the current prompt engine).
5. Analyze data to determine if the prompt engine improves engagement without confounding factors.
6. Document findings and propose next steps (e.g., full rollout, iteration, or rejection).

**What changed:**
Test design now isolates prompt engine impact from interaction fatigue by logging forced vs. voluntary interactions in a random 15% slice.
