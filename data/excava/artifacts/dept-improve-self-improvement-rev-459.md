# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-459` (dept) · 2026-09-03T20:21:45.400024+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in parallel mode only on new contributors’ PRs for two weeks to measure real impact with 70% less compute cost and noise.

**Plan:**
1. Configure PR-Agent to run in parallel mode exclusively on PRs from new contributors (no prior contributions).
2. Deploy for two weeks, logging false positives/negatives and team reactions (comments, reactions, or PR edits).
3. Aggregate metrics: compute cost, noise volume, and signal quality (actionable vs. ignored feedback).
4. Conduct a team survey post-deployment to assess sentiment and defensive reactions.
5. Analyze data to determine full deployment viability (false positive rate <10%, team adoption >60%).
6. Document findings in a shared report for team review.

**What changed:** PR-Agent parallel mode limited to new contributors’ PRs for two weeks.
