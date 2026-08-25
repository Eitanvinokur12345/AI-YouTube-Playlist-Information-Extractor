# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-964` (dept) · 2026-08-25T21:00:14.745826+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Deploy PR-Agent in shadow mode on *all* PRs for one week.
2. Collect and log all PR-Agent output (flags, suggestions, noise) for analysis.
3. Categorize results by contributor experience (new vs. veteran) to compare noise levels.
4. Generate a noise baseline report (owner: Overhaul) with metrics on false positives/negatives.
5. If noise is similar across groups, expand to all contributors; if biased toward new contributors, adjust scope.
6. Present findings to the team for final decision on full rollout or refinement.

**What changed:** Shadow mode now runs on *all* PRs for one week, with noise baseline analysis by contributor experience.
