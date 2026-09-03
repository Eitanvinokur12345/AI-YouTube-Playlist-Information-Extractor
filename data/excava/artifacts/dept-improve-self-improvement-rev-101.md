# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-101` (dept) · 2026-09-03T03:49:58.368395+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on all PRs for two weeks, then switch to parallel mode on new-contributor PRs for false-negative testing.

**Plan:**
1. Configure PR-Agent in shadow mode for all PRs for 14 days.
2. Collect metrics on false positives, merge conflicts, and team friction.
3. After 14 days, enable parallel mode for PR-Agent auto-applying low-risk changes *only* on new-contributor PRs.
4. Measure false negatives and rework risks in this pilot.
5. If metrics are acceptable, expand auto-apply to broader PRs.
6. Document findings and adjust PR-Agent configuration as needed.

**What changed:** Shadow mode first, then targeted parallel pilot for new contributors.
