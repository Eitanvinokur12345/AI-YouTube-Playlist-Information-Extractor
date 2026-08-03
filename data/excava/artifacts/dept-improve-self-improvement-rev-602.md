# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-602` (dept) · 2026-08-03T19:41:13.450904+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Run PR-Agent in shadow mode on the newest open PR first, then rotate to the oldest merged PR after two weeks to balance fresh risk prevention with legacy path stability.

**Plan:**
1. Configure PR-Agent to run in shadow mode on the newest open PR immediately.
2. Monitor shadow mode reports for 2 weeks, prioritizing fresh PR risk prevention.
3. After 2 weeks, switch shadow mode to the oldest merged PR to surface systemic issues.
4. Review shadow mode reports for both PRs to identify prompt/routing improvements.
5. Apply safe, non-disruptive changes to prompts/engines/routing based on findings.
6. Iterate monthly, alternating focus between newest open and oldest merged PRs.

**What changed:** Shadow mode reports for both PRs now exist and are reviewed for systemic prompt/routing issues.
