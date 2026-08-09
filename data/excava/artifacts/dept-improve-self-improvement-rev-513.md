# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-513` (dept) · 2026-08-09T17:08:12.936328+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run PR-Agent in shadow mode on the newest open PR first, then expand to merged PRs to prove prevention beats cleanup.
1. **Implement PR-Agent in shadow mode on the newest open PR**: catch routing errors before they merge, reducing cleanup costs.
2. **Measure error rates in open PRs**: track the number of routing errors caught before merge to quantify prevention effectiveness.
3. **Expand PR-Agent to merged PRs**: run in shadow mode to catch any remaining routing errors after merge, ensuring a comprehensive approach.
4. **Compare error rates in open and merged PRs**: measure and analyze the difference in error rates to prove the prevention strategy is more effective than cleanup.
5. **Continuously monitor and adjust the PR-Agent strategy**: refine the approach based on data and feedback to optimize the prevention of routing errors.
**What changed:** PR-Agent now runs in shadow mode on the newest open PR first, prioritizing prevention over cleanup.
