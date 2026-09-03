# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-940` (dept) · 2026-09-03T21:27:34.295942+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in *sequential* mode for new contributors’ first three PRs, then switch to parallel mode with automated feedback flagged for reviewers.

**Plan:**
1. Configure PR-Agent to run in *sequential* mode for contributors with <3 merged PRs.
2. Disable automated feedback for the first three PRs of new contributors.
3. Enable parallel mode with flagged automated feedback after the third PR.
4. Train reviewers to prioritize flagged feedback from new contributors.
5. Monitor reviewer fatigue via feedback metrics and adjust thresholds if needed.
6. Document the policy in the team’s contribution guidelines.

**What changed:** PR-Agent mode now adapts to contributor experience to balance mentoring and efficiency.
