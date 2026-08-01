# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-354` (dept) · 2026-07-30T17:31:43.447826+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a 7-day rolling minimum threshold for the top 5% of prompts by usage—flag if performance drops below their 30-day average.
2. Apply a 30-day usage-weighted decay metric to the remaining 95% of prompts.
3. Automate recalculation of the top 5% thresholds daily to balance freshness and stability.
4. Integrate silent failure detection into the 30-day metric to catch regressions without over-rotation.
5. Add compute cost monitoring to ensure the hybrid system remains efficient.
6. Document the hybrid metric logic in the prompt routing engine’s codebase.

**What changed:** Hybrid 7-day rolling minimum (top 5%) + 30-day weighted decay (rest) replaces prior single-metric proposals.
