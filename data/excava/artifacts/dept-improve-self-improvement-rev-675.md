# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-675` (dept) · 2026-07-30T17:54:05.885132+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement 7-day hard decay for prompts with >5000 calls/month.
2. Apply 14-day rolling weighted decay with 15% floor for prompts 1000–4999 calls/month.
3. Set 90-day rolling minimum threshold for all other prompts (<1000 calls/month).
4. Auto-apply safe changes (e.g., prompt edits) only if decay score improves by ≥10%.
5. Route new prompts through a 7-day probationary period before full integration.
6. Log decay triggers and overrides in a weekly report for manual review.

**What changed:** Hybrid decay rules with tiered thresholds and auto-apply safeguards.
