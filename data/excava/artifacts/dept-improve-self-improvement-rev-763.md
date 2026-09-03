# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-763` (dept) · 2026-09-03T20:54:43.441514+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in parallel mode on *new contributors only* for one week, then expand to all PRs only if the false-positive rate stays below 15%.

**Plan:**
1. Configure PR-Agent to run in parallel mode on PRs from *new contributors only* (defined as contributors with <3 merged PRs in the repo).
2. Monitor false-positive rate (automated comments flagged as incorrect by reviewers) for 7 days.
3. If false-positive rate ≤15%, expand parallel mode to *all* PRs and document the change.
4. If false-positive rate >15%, pause expansion, analyze root causes, and adjust PR-Agent configuration before retrying.
5. Publish a public artifact (e.g., GitHub issue or doc) summarizing the trial results, thresholds, and next steps.
6. Assign a lead to track the trial, collect feedback, and enforce the 15% threshold.

**What changed:** Limited initial rollout to new contributors only, with a 15% false-positive threshold for full expansion.
