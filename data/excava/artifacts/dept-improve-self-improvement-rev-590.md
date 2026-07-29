# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-590` (dept) · 2026-07-29T21:48:37.065709+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid metric—7-day decay for new failures *and* rolling 30-day window for persistent ones—weighted by user impact, applied only to the top 20% of prompts by usage.

**Plan:**
1. Implement a combined scoring system: (7-day decay for new failures) + (30-day rolling window for persistent failures), weighted by user-reported impact.
2. Limit the metric to the top 20% of prompts by usage to prioritize high-impact cases.
3. Create a single dashboard ranking prompts by this hybrid score, updated daily.
4. Integrate user-reported issues with failure-rate data to ensure dissatisfaction is captured.
5. Set up automated alerts for prompts scoring above a configurable threshold.
6. Document the metric logic and thresholds in the codebase for transparency.

**What changed:**
Hybrid failure metric (7-day + 30-day) replaces standalone rolling windows, applied only to top 20% prompts.
