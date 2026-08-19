# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-996` (dept) · 2026-08-19T06:28:21.884530+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode only on PRs flagged by both new contributors *and* high-risk changes for two weeks.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on PRs where:
   - `author_is_new_contributor` is `true` (existing contributor flag)
   - `change_risk_score` exceeds a predefined threshold (high-risk heuristic)
2. Log all PR-Agent feedback (comments, suggestions) to a dedicated channel without posting to PRs.
3. After each PR is merged, compare PR-Agent’s feedback against human reviews to quantify:
   - Missed issues (human reviews flagged but PR-Agent did not)
   - False positives (PR-Agent flagged but human reviews did not)
4. Track developer friction metrics (e.g., review time, comment volume) for flagged vs. non-flagged PRs.
5. Run the trial for exactly two weeks, then compile a report with the above metrics.
6. Owner (Overhaul) presents findings and recommends next steps (e.g., full rollout, scope adjustment, or discontinuation).

**What changed:** PR-Agent shadow mode now targets only high-risk PRs from new contributors.
