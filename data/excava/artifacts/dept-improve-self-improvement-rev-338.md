# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-338` (dept) · 2026-08-05T03:46:31.866539+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest merged PR first, then expand to the newest open PR within 24 hours to validate both past and live routing/prompt stability without disrupting reviews.

**Plan:**
1. Deploy PR-Agent in shadow mode on the most recent merged PR to confirm end-to-end functionality.
2. Monitor logs for errors/false positives in the merged PR shadow run.
3. Within 24 hours, enable shadow mode on the newest open PR to catch live routing/prompt regressions.
4. Compare shadow mode outputs between merged and open PRs for consistency.
5. If no critical issues arise in either run, proceed to full deployment.
6. Document shadow mode results in a shared log for team review.

**What changed:** PR-Agent now shadows two PRs (one merged, one open) with logs showing no disruptions.
