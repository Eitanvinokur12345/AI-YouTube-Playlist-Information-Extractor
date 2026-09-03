# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-126` (dept) · 2026-09-03T20:38:20.134967+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in parallel mode only on new contributors’ PRs for two weeks to measure false positives/negatives without training the team to ignore feedback.

**Plan:**
1. Configure PR-Agent to run in parallel mode exclusively on PRs from new contributors (first-time or <3 PRs merged).
2. Log all PR-Agent feedback (false positives/negatives) in a dedicated tracking issue for review.
3. Disable parallel mode after two weeks and analyze the logged data to assess accuracy and team impact.
4. Conduct a team survey to gauge whether noise affected review behavior.
5. Present findings to the lead for a go/no-go decision on broader adoption.
6. Archive the tracking issue and document lessons learned for future tooling evaluations.

**What changed:** PR-Agent parallel mode restricted to new contributors’ PRs for controlled false-positive/negative measurement.
