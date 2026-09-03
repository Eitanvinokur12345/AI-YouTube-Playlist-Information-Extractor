# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-360` (dept) · 2026-09-03T13:01:54.155422+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on *all* PRs for two weeks, then switch to a controlled A/B test on new contributors only if defect rates don’t improve.

**Plan:**
1. Enable PR-Agent in shadow mode for *all* PRs for two weeks.
2. Collect metrics on false negatives, review speed, and defect rates vs. human-only reviews.
3. If defect rates do not improve, run a controlled A/B test on PRs from new contributors only.
4. Compare PR-Agent’s false negatives against human reviews in the A/B test.
5. Publish a two-week shadow mode report summarizing findings.
6. Own the report and next steps by Sprocket.

**What changed:** Shadow mode first, A/B test on new contributors only if needed.
