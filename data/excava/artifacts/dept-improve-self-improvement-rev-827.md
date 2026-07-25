# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-827` (dept) · 2026-07-25T03:50:43.516956+00:00
> Participants: Ratchet, Sprocket, Gauge · synthesized by transcript-summary (no engine)

**Decision:** DECISION: Run a 5% canary rollout *and* a parallel 48-hour shadow test on the new prompt engine.

The result must deliver: real-time error monitoring for the canary, plus full traffic replay validatio

**Plan (from the debate):**
1. DECISION: Run a 5% canary rollout *and* a parallel 48-hour shadow test on the new prompt engine.

The result must deliver: real-time error monitoring for the canary, plus full traffic replay validatio
2. Run a shadow test first: replay 100% of real user traffic through the new prompt engine without affecting responses. This catches hidden flaws without risking user experience. The trade-off is higher 
3. Shadow testing replays traffic but misses the real risk: silent failures only surface when users interact with the new system in production. A better alternative is canary deployment with gradual traf
4. Run a shadow test first. It’s the safest way to catch hidden flaws without touching real users. The trade-off is higher compute cost and latency during the test, but that’s cheaper than a failed rollo
5. Shadow testing’s real risk is that it only validates *traffic patterns*, not *user outcomes*—a new prompt engine might return plausible but wrong answers that users act on, and you won’t know until it

**What changed:** first real room artifact.
