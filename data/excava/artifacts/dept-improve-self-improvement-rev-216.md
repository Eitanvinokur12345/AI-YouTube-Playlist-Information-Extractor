# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-216` (dept) · 2026-09-03T03:32:59.780973+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in parallel mode on PRs from new contributors only for two weeks, with maintainers manually verifying every suggestion before merging.

**Plan:**
1. Configure PR-Agent to run in parallel mode on PRs authored by new contributors (defined as contributors with <3 merged PRs in the repo).
2. Add a mandatory manual review step for all PR-Agent suggestions in these PRs, with maintainers approving or rejecting each suggestion before merging.
3. Log all PR-Agent suggestions, approvals, rejections, and manual overrides to a dedicated dashboard for analysis.
4. After two weeks, analyze logs to measure PR-Agent’s impact on review time, merge rate, and suggestion accuracy.
5. Share findings with the team to decide whether to expand PR-Agent’s use or adjust its configuration.
6. Archive logs and disable the parallel mode test after the evaluation period.

**What changed:** PR-Agent now runs in parallel mode on new contributor PRs with mandatory manual verification and logging for two weeks.
