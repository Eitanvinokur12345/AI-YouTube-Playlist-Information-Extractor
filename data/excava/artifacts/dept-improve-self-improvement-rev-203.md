# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-203` (dept) · 2026-08-17T01:16:13.279806+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode *only on merged PRs* for two weeks to validate fixes without training reviewers to ignore feedback.

**Plan:**
1. Configure PR-Agent to run in shadow mode exclusively on merged PRs for the pilot duration.
2. Tag merged PRs exceeding 5 files changed as "high-risk" for shadow mode analysis.
3. Collect false positive rates, edge cases, and actionable feedback in a dedicated log.
4. Disable shadow mode comments for reviewers (no visible autofeedback).
5. Owner Overhaul compiles a go/no-go report summarizing pilot data and recommendations.
6. Deliver report to the lead by the end of the two-week pilot.

**What changed:**
Shadow mode now runs *only on merged PRs* (high-risk flagged) for two weeks, excluding open PRs.
