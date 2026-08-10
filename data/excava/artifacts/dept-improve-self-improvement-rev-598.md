# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-598` (dept) · 2026-08-10T21:19:36.370056+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on open PRs first, then expand to merged PRs.

**Plan:**
1. Configure PR-Agent to run in shadow mode on all open PRs for one week.
2. Collect and review PR-Agent feedback alongside human reviews to assess accuracy and noise.
3. After one week, expand shadow mode to merged PRs to validate retroactive improvements.
4. Document false positives/negatives and adjust PR-Agent’s configuration or prompts as needed.
5. After two weeks, evaluate impact on review queue noise and retrofitting costs.
6. If successful, propose permanent adoption of PR-Agent in shadow mode to the team.

**What changed:**
PR-Agent now runs in shadow mode on open PRs first, with merged PRs added after one week.
