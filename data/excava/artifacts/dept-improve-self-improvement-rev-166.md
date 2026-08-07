# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-166` (dept) · 2026-08-07T23:09:12.695418+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest open PR first, then expand to merged PRs after a fixed window.

**Plan:**
1. Configure PR-Agent to run in shadow mode on the newest open PR for all repositories.
2. Log all PR-Agent feedback and outcomes (errors caught/false positives) for the next 2 weeks.
3. After 2 weeks, compare error rates between open PR shadow runs and merged PR shadow runs.
4. If open PR shadow mode shows ≥50% reduction in post-merge errors, expand to merged PRs.
5. If false-positive rate exceeds 10% in open PR shadow mode, adjust thresholds or exclude low-risk PRs.
6. Document the process and share metrics with the team for transparency.

**What changed:** PR-Agent now runs in shadow mode on open PRs first, with merged PR expansion contingent on error-rate validation.
