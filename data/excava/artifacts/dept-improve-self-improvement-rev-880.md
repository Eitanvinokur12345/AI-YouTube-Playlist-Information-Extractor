# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-880` (dept) · 2026-07-22T18:17:30.899412+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy the new prompt engine to a 5% canary user cohort, doubling traffic every 24 hours (5% → 10% → 20% → 40% → 100%) if no critical errors.
2. Run a parallel 48-hour shadow test of the new engine against the old one, measuring output quality, latency, error rates, and infra load.
3. Gauge owns the shadow test metrics; Sprocket owns the canary rollout metrics.
4. Compare both datasets for user impact, task breakage, and infra load after 48 hours.
5. Generate a go/no-go report with clear metrics and recommendations.
6. Ratchet makes the final call based on the report.

**What changed:** Combined canary rollout + shadow test for comprehensive risk assessment.
