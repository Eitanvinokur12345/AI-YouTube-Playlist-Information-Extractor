# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-159` (dept) · 2026-09-03T19:12:51.311429+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in parallel mode on new contributors’ PRs only for two weeks to measure false negatives where context gaps hurt most.

**Plan:**
1. Configure PR-Agent to run in parallel mode only on PRs from new contributors (defined as <5 merged PRs in the repo).
2. Log all PR-Agent outputs (suggestions, false positives, false negatives) for new contributor PRs during the two-week trial.
3. Compare false negative rates (missed issues) between new and veteran contributors using historical data as baseline.
4. Track compute/time savings by limiting scope to ~20% of PRs (new contributors only).
5. Collect team feedback on suggestion quality and noise levels via a short survey after the trial.
6. Analyze results to determine next steps (e.g., expand scope, adjust thresholds, or disable PR-Agent).

**What changed:** PR-Agent now runs in parallel mode exclusively on new contributors’ PRs for two weeks to validate false negative impact.
