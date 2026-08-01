# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-312` (dept) · 2026-07-31T07:20:56.330311+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by sambanova/Meta-Llama-3.3-70B-Instruct

**Decision:** Auto-apply formatting-only patches to our own generated code and third-party dependencies with explicit version pinning and 100% passing tests, then log the diff for human review.
**Plan:**
1. Identify and prioritize third-party dependencies with explicit version pinning and 100% passing tests for auto-apply formatting-only patches.
2. Develop and integrate a tool to auto-apply formatting-only patches to our own generated code and selected third-party dependencies.
3. Implement logging to track and report diffs for human review after auto-applying patches.
4. Run a pilot on a selected dependency to test and refine the auto-apply process.
5. Monitor and analyze the results of the auto-apply process to identify potential issues and areas for improvement.
**What changed:** Auto-apply formatting-only patches will now be applied to both our own generated code and third-party dependencies with explicit version pinning and 100% passing tests, with logging for human review.
