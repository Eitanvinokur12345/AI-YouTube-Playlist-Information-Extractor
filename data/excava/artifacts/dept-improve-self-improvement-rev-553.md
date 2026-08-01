# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-553` (dept) · 2026-07-31T00:26:27.313274+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a hybrid decay system:
   - 7-day hard decay for prompts with ≤100 uses.
   - Rolling 30-day weighted decay with a 10% floor for prompts >100 uses.
2. Tag prompts by role (e.g., "onboarding," "edge-case handler") to exempt critical prompts from decay.
3. Auto-apply safe changes via a review pipeline that flags high-risk deletions for manual approval.
4. Log decay events and usage metrics in a dashboard for auditing.
5. Run a 30-day trial, then adjust decay weights/floors based on retention data.
6. Pitch the system to stakeholders with a 1-week review cycle for exceptions.

**What changed:** Hybrid decay with role-based exemptions and auto-apply pipeline.
