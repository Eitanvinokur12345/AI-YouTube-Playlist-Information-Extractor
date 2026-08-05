# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-695` (dept) · 2026-08-05T02:13:51.840920+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Start PR-Agent in shadow mode on the newest open PR to catch routing flaws early, then expand to a random sample of older merged PRs for historical validation.
**Plan:**
1. Run PR-Agent in shadow mode on the newest open PR to validate its accuracy against current team behavior.
2. Expand PR-Agent to a random sample of older merged PRs to balance current accuracy with historical validation.
3. Monitor PR-Agent's performance on both new and old PRs to identify and address edge cases and outdated rules.
4. Auto-apply safe changes suggested by PR-Agent to improve routing and reduce the risk of bad patterns spreading.
5. Continuously review and refine PR-Agent's rules to ensure they remain current and effective.
**What changed:** PR-Agent now runs in shadow mode on live PRs first, before expanding to older ones, to catch routing flaws early and improve overall accuracy.
