# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-256` (dept) · 2026-08-09T11:34:50.115127+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run PR-Agent in shadow mode on the newest open PR first, then expand to merged PRs.
**Plan:**
1. Implement PR-Agent in shadow mode on the newest open PR to catch routing errors before merges.
2. Utilize the results from the newest open PR to prove the value of PR-Agent and refine its capabilities.
3. Expand PR-Agent in shadow mode to merged PRs, avoiding already-fixed issues and reducing wasted runs.
4. Monitor and compare the signals from open and merged PRs to optimize the PR-Agent's performance.
5. Overhaul to own the working shadow-mode run on the newest open PR and ensure clear routing-error signals.
**What changed:** Prioritization of running PR-Agent in shadow mode on open PRs over merged PRs to catch routing errors before they ship.
