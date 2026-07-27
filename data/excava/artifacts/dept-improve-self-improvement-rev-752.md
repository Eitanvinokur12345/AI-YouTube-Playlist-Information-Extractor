# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-752` (dept) · 2026-07-27T19:01:12.965342+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy a 0.1% canary of the new prompt changes to users for 48 hours.
2. Log dual-prompt A/B results and enforce a 0.01% error-rate SLA.
3. Sprocket executes the canary deployment and monitoring.
4. Gauge validates error rates and escalates breaches.
5. If SLA is met, scale canary to 1% for 72 hours.
6. If stable, roll out to 100% with the Claude Self-Improvement Skill Pack for automated prompt tuning.

**What changed:** Switched from 5% canary to 0.1% canary with stricter SLA and dual-prompt logging.
