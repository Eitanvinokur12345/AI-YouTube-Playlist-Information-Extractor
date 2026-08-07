# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-834` (dept) · 2026-08-07T17:26:23.318538+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest open PR first, then expand to merged PRs.

**Plan:**
1. Configure PR-Agent in shadow mode to analyze the newest open PR immediately upon PR creation.
2. Log all PR-Agent outputs (reviews, suggestions, flags) for the newest open PR without posting them.
3. After 1 full sprint (or 1 week), review shadow mode logs for routing/prompt regressions or systemic issues.
4. If no critical issues are found, expand shadow mode to the newest merged PR for consistency verification.
5. Iterate: Adjust prompts/routing based on findings, then re-test on open PRs before enforcing changes.
6. Document all shadow mode results in a shared log for team review and future reference.

**What changed:** Prioritized open PR shadow mode to catch systemic issues early, delaying merged PR verification until after validation.
