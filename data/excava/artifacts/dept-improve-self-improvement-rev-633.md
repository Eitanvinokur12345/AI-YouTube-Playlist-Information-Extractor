# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-633` (dept) · 2026-08-13T08:03:39.453683+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on open PRs first, then expand to merged PRs after one week of tuning.

**Plan:**
1. Configure PR-Agent in shadow mode for all open PRs (no human-facing changes).
2. Collect and log PR-Agent’s review output vs. human reviews for one week.
3. Analyze signal-to-noise metrics (false positives/negatives, review depth).
4. After one week, expand shadow mode to merged PRs for baseline validation.
5. Compare PR-Agent’s merged PR feedback against human reviews post-merge.
6. Adjust PR-Agent’s rules/config based on collected metrics.

**What changed:** PR-Agent shadow mode prioritized open PRs first, with merged PR validation deferred to Week 2.
