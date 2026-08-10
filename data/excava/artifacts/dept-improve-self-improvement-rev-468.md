# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-468` (dept) · 2026-08-10T21:00:50.815628+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run PR-Agent in shadow mode on open PRs first, tune signal-to-noise, then expand to merged PRs
**Plan:**
1. Initialize PR-Agent in shadow mode on open PRs to catch edge cases early and identify areas for tuning.
2. Monitor and analyze the signal-to-noise ratio of PR-Agent's feedback on open PRs to determine the optimal tuning parameters.
3. Apply the tuned parameters to PR-Agent and expand its shadow mode operation to merged PRs, ensuring a consistent review process.
4. Continuously review the performance of PR-Agent on both open and merged PRs to identify any additional tuning needs.
5. Own the tuning and rollout process to ensure seamless integration and minimal disruption to the development workflow.
**What changed:** Expanded rollout approach to prioritize open PRs for initial tuning before expanding to merged PRs.
