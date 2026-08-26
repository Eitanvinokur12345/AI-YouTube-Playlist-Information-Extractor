# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-237` (dept) · 2026-08-26T09:37:31.581278+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on *only* new-contributor PRs for two weeks, measuring comment-to-action ratios to decide next steps.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on PRs from new contributors (first-time or low-activity users).
2. Track and log all PR-Agent comments and subsequent reviewer actions (e.g., commits, dismissals, or approvals) for two weeks.
3. Calculate the comment-to-action ratio weekly, flagging any PR-Agent comments that lead to no visible changes.
4. After two weeks, review data with the team to determine if the ratio exceeds 3:1 (comments to actions).
5. If ratio >3:1, expand shadow mode to all PRs; otherwise, discontinue the experiment.
6. Document findings in a shared report (e.g., GitHub issue) to inform future tooling decisions.

**What changed:** PR-Agent shadow mode limited to new-contributor PRs for two weeks, with expansion criteria based on comment-to-action ratios.
