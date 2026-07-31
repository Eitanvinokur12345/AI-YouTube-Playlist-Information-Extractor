# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-421` (dept) · 2026-07-31T01:05:57.093237+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 14-day rolling decay with a 10% floor for all prompts.

**Plan:**
1. Implement a rolling 14-day decay algorithm for all prompts in the system.
2. Set a 10% floor to ensure rare edge-case prompts are retained.
3. Add logging to track pruned prompts and their triggers for review.
4. Run a 7-day A/B test comparing routing stability with the old 7-day hard decay.
5. After testing, apply the decay to all prompts and monitor engine performance.
6. Document the change in the system’s prompt management guidelines.

**What changed:** Switched from 7-day hard decay to 14-day rolling decay with 10% floor.
