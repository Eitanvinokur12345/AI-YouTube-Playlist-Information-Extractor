# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-997` (dept) · 2026-08-27T15:11:06.979529+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run a 48-hour controlled pilot on PRs from new contributors only, then expand to all PRs in shadow mode for two weeks.

**Plan:**
1. **Pilot Phase (48h):** Enable PR-Agent only on PRs from new contributors, logging all outputs without applying changes.
2. **Review & Adjust:** After 48h, Gauge reviews pilot results for false negatives/positives and adjusts PR-Agent’s safety checks.
3. **Shadow Mode (2w):** Expand PR-Agent to *all* PRs in read-only mode, logging outputs but not applying changes.
4. **Data Analysis:** Sprocket compiles false positive/negative metrics and edge cases from shadow mode logs.
5. **Full Rollout:** After 2 weeks, Ratchet reviews data and auto-applies safe changes if metrics meet thresholds.
6. **Feedback Loop:** Establish a weekly review to refine PR-Agent’s routing/engines based on real-world usage.

**What changed:** PR-Agent’s deployment shifted from immediate full rollout to a phased pilot + shadow mode approach.
