# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-305` (dept) · 2026-07-31T01:52:56.405468+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid prompt decay system balancing freshness and critical context retention.

**Plan:**
1. Implement 7-day hard decay for prompts with <100 uses.
2. Apply 14-day rolling decay with 10% floor for prompts ≥100 uses.
3. Add manual override flag for high-value prompts (e.g., edge cases, high-impact).
4. Auto-archive prompts exceeding decay thresholds unless renewed.
5. Log decay events for review in self-improvement cycles.
6. Integrate decay checks into routing engine’s prompt validation.

**What changed:**
Hybrid decay system replaces uniform 7-day hard decay with usage-based rules and overrides.
