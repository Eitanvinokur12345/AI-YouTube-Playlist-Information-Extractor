# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-876` (dept) · 2026-09-04T00:21:04.826843+00:00
> Participants: Ratchet, Sprocket, Gauge, Overhaul · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in parallel mode for all PRs, auto-applying feedback only from established contributors while routing new contributors’ feedback to a human queue.

**Plan:**
1. Configure PR-Agent to process all PRs in parallel mode.
2. Implement contributor trust tiering (established vs. new) based on GitHub activity history.
3. Auto-apply feedback from established contributors; route new contributors’ feedback to a human review queue.
4. Add a "trust tier" label to PRs for visibility.
5. Monitor false-positive rates and reviewer workload for 2 weeks, adjusting thresholds as needed.
6. Document the process in the team’s internal wiki.

**What changed:**
Auto-apply only for trusted contributors; new contributors’ feedback now requires human review.
