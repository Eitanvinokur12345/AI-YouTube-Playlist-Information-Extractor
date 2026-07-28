# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-115` (dept) · 2026-07-28T23:12:14.806478+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Gate auto-apply on two checks—first, a semantic diff against all edited files and their direct dependencies; second, a minimal full-project regression suite triggered only for high-risk edits (core logic or API changes).

**Plan:**
1. Implement a semantic diff test that runs against all edited files and their direct dependencies, blocking auto-apply if it detects regressions.
2. Define "high-risk edits" as changes to core logic or public APIs, flagged by static analysis or file path rules.
3. Trigger a minimal full-project regression suite (e.g., critical-path tests) only when high-risk edits are detected.
4. Integrate both checks into the auto-apply pipeline, with the semantic diff as the first gate and the full regression suite as the second.
5. Log and surface results of both checks to the user, including diffs and test failures, for manual review if needed.
6. Optimize the minimal regression suite to run in <30s by pre-selecting critical tests based on dependency analysis.

**What changed:**
Auto-apply now requires passing both a targeted semantic diff and a conditional full regression suite for high-risk edits.
