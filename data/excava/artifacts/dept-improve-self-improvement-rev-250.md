# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-250` (dept) · 2026-07-29T21:19:13.313836+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a rolling 30-day failure-impact score for the top 20% of prompts by usage, weighted by retry cost and latency.

**Plan:**
1. Implement a daily-updated dashboard ranking prompts by combined failure rate (30-day rolling) and impact (retry cost × latency).
2. Prioritize the top 20% of prompts by usage for failure-impact scoring.
3. Integrate retry cost and latency metrics into the failure-impact formula.
4. Set up automated alerts for prompts exceeding failure-impact thresholds.
5. Assign Gauge as owner for dashboard maintenance and metric updates.
6. Document the scoring methodology and thresholds in the repo’s README.

**What changed:**
Prompts are now ranked by rolling 30-day failure-impact, not just frequency or raw failure rate.
