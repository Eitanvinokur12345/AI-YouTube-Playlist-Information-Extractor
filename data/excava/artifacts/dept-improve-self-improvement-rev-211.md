# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-211` (dept) · 2026-08-10T19:52:19.303618+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run PR-Agent in shadow mode on a random sample of closed PRs first to measure false positives, then expand to open PRs only if the rate stays below 15%.
**Plan:**
1. Select a random sample of closed PRs for initial PR-Agent testing in shadow mode.
2. Measure the false-positive rate of PR-Agent output on the closed PR sample.
3. Validate PR-Agent's signal-to-noise ratio based on the false-positive rate measurement.
4. Establish a written threshold of 15% for the false-positive rate to determine expansion to open PRs.
5. Expand PR-Agent to open PRs in shadow mode if the false-positive rate is below the established threshold.
6. Monitor and adjust the PR-Agent's performance based on feedback from the team.
**What changed:** PR-Agent deployment strategy shifted from immediately applying to open PRs to a phased approach starting with closed PRs to ensure signal quality and team trust.
