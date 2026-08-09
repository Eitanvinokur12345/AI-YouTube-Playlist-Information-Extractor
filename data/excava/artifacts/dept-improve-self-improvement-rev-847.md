# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-847` (dept) · 2026-08-04T03:51:06.065194+00:00
> Participants: Ratchet, Sprocket, Gauge, Overhaul · synthesized by mistral/mistral-small-latest

**Decision:**
Run PR-Agent in shadow mode on both the oldest merged PR and the newest open PR in parallel to catch regressions and stress-test new routing paths immediately.

**Plan:**
1. Enable shadow mode for PR-Agent on the oldest merged PR (e.g., `PR-123`).
2. Enable shadow mode for PR-Agent on the newest open PR (e.g., `PR-456`).
3. Log all PR-Agent feedback and routing decisions for both PRs in a shared channel/thread.
4. Compare shadow mode outputs against actual PR outcomes to identify regressions or routing flaws.
5. Adjust routing logic based on findings, prioritizing fixes for the newest open PR.
6. Document edge cases discovered in the newest PR’s routing paths for future validation.

**What changed:**
Shadow mode now validates both oldest merged and newest open PRs in parallel to proactively catch regressions and routing flaws.
