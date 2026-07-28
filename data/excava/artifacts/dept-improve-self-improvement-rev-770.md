# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-770` (dept) · 2026-07-28T23:19:31.617338+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run a 48-hour dual-prompt A/B test with 10% of users, forcing feedback on answer quality and latency at every interaction.

**Plan:**
1. Split traffic: 10% of users receive the new prompt, 90% retain the current one.
2. Deploy forced feedback collection: prompt users for quality/latency ratings after every interaction.
3. Monitor real-time metrics: track answer quality, latency, and error rates for both prompts.
4. Assign ownership: metrics team leads data collection, analysis, and reporting.
5. Conduct post-test review: compare feedback and performance data to validate the new prompt.
6. Document findings: summarize insights and next steps for full rollout or rollback.

**What changed:** Switched from shadow/canary tests to a dual-prompt A/B test with forced user feedback for faster, more comprehensive validation.
