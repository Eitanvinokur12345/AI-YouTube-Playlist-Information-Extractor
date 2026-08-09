# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-929` (dept) · 2026-08-03T06:36:21.675778+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Run PR-Agent in shadow mode on the oldest merged PR with known issues for one week to measure real catch-rate without disruption, logging errors only.
**Plan:**
1. Identify the oldest merged PR with known issues in the main repository.
2. Configure PR-Agent to run in shadow mode on the selected PR, logging errors and misses without blocking any merges.
3. Run PR-Agent in shadow mode for one week to collect data on its catch-rate and false positives.
4. Deliver a report of PR-Agent's misses and false positives to Overhaul after the one-week test period.
5. Review the report to assess PR-Agent's performance and identify areas for improvement.
**What changed:** The approach to testing PR-Agent was changed from dry-run mode to shadow mode on a specific PR to get a faster and more accurate signal on its catch-rate.
