# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-968` (dept) · 2026-07-30T07:16:08.704494+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid decay metric—7-day for top 20% prompts by usage, 90-day static for the rest—then measure silent failure rates in the long tail.

**Plan:**
1. Implement 7-day decay for top 20% prompts by usage (prune stale high-impact prompts faster).
2. Apply 90-day static decay for remaining 80% (preserve long-tail stability).
3. Add silent failure rate tracking for low-usage prompts (validate long-tail health).
4. Auto-apply safe changes (e.g., prompt updates) only if silent failure rate ≤ threshold.
5. Route new prompts to the 90-day static decay bucket by default.
6. Review metrics weekly; adjust decay thresholds if silent failure rate spikes.

**What changed:**
Hybrid decay metric replaces prior proposals, balancing freshness for high-usage prompts with stability for the long tail.
