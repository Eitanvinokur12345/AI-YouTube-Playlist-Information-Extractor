# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-483` (dept) · 2026-08-27T14:25:30.404729+00:00
> Participants: Overhaul, Sprocket, Ratchet, Gauge · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in parallel review mode on *all* PRs for one week, then decide next steps based on false negative data.

**Plan:**
1. Deploy PR-Agent in parallel review mode (flags issues but humans retain final approval).
2. Track false negatives (issues humans catch that PR-Agent missed) and false positives (PR-Agent flags but humans disagree).
3. Collect data for one week, focusing on false negative rate and human review workload.
4. Analyze results to determine if PR-Agent’s reliability justifies expansion or if adjustments are needed.
5. Present findings to the team with a clear go/no-go decision for full deployment.
6. If false negative rate is acceptable, proceed with broader rollout; otherwise, refine PR-Agent or adjust scope.

**What changed:** Parallel review mode replaces shadow mode for one week to measure real-world false negatives.
