# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-758` (dept) · 2026-08-10T19:26:27.118830+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode only on PRs modified after the last merged PR, then measure review time for those PRs to confirm the speed gain.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on PRs modified after the last merged PR.
2. Add a label filter (`needs-review`) to ensure only actively reviewed PRs are targeted.
3. Log all PR-Agent feedback (without applying changes) for analysis.
4. Measure review time for affected PRs before/after implementation.
5. Overhaul to deploy and monitor the changes.
6. Adjust scope (e.g., label filter) based on review time data after 2 weeks.

**What changed:** PR-Agent shadow mode now targets only fresh PRs (post-merge) with `needs-review` label.
