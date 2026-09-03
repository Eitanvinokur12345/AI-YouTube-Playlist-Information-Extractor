# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-103` (dept) · 2026-09-03T04:06:53.983504+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on all PRs for two weeks, then switch to parallel mode on PRs from new contributors only.

**Plan:**
1. Deploy PR-Agent in shadow mode (no real reviews) on all PRs for 14 days.
2. Collect metrics: false negatives, dev reactions, and build failures.
3. After 2 weeks, enable parallel mode (real reviews) exclusively on PRs from new contributors.
4. Compare merge rates, rework frequency, and dev feedback between shadow and parallel modes.
5. If results are positive, expand parallel mode to all PRs; otherwise, refine prompts/safety checks.
6. Finalize automation rollout or rollback based on data.

**What changed:** PR-Agent moves from shadow mode (all PRs) to parallel mode (new contributors only).
