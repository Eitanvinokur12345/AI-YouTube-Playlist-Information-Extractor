# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-274` (dept) · 2026-08-03T17:45:42.792390+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run PR-Agent in shadow mode on the newest open PR with a known issue first, then expand to the oldest merged PR with known issues.
1. **Identify** the newest open PR with a known issue to run PR-Agent in shadow mode.
2. **Run PR-Agent** in shadow mode on the identified PR to catch current routing and prompt gaps.
3. **Analyze results** to validate the tool's accuracy in addressing today's failures.
4. **Expand** PR-Agent in shadow mode to the oldest merged PR with known issues to validate historical behavior.
5. **Review** and **apply** safe changes based on the results from both runs.
**What changed:** The approach to testing PR-Agent's accuracy now prioritizes current failures while still validating historical behavior.
