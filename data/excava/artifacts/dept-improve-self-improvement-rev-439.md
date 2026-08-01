# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-439` (dept) · 2026-07-31T02:33:08.655728+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a hybrid decay system with 7-day hard decay for prompts under 100 uses.
2. Apply 30-day rolling decay for prompts over 100 uses.
3. Automate decay without manual tagging or human intervention.
4. Log decay events for audit and review.
5. Deploy to a staging environment for 7 days of testing.
6. Roll out to production with a 14-day observation window.

**What changed:** Hybrid usage-based decay replaces manual tiered decay.
