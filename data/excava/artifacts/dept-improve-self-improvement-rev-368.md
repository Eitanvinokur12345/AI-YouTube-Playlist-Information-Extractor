# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-368` (dept) · 2026-08-30T02:58:14.328043+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on all PRs for two weeks, then switch to a parallel A/B test on new-contributor PRs for one week to catch false negatives.

**Plan:**
1. Deploy PR-Agent in shadow mode across all PRs for 14 days.
2. Collect metrics: review time, false positives/negatives, and build impact.
3. After two weeks, enable a parallel A/B test on PRs from new contributors only.
4. Run the A/B test for 7 days, comparing PR-Agent’s reviews against human reviews.
5. Measure false negatives by auditing missed issues in new-contributor PRs.
6. Compile data and present findings to stakeholders for final adoption decision.

**What changed:**
Added a targeted A/B test on new-contributor PRs to expose false negatives after initial shadow-mode validation.
