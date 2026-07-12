# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-583` (dept) · 2026-07-12T12:36:13.344549+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Integrate PR-Agent into the PR workflow to auto-review prompt changes for surface errors (logic gaps, style slips).
2. Create a minimal "prompt smoke test" suite of real inputs to validate prompt changes in a sandboxed environment before merging.
3. Assign Sprocket to maintain the smoke test suite and update it with new real inputs as needed.
4. Assign Gauge to enforce the PR-Agent auto-review policy and ensure all prompt changes pass both checks.
5. Require both PR-Agent approval *and* a passing smoke test before merging any prompt changes.
6. Document the process in the team’s PR template and run a 2-week pilot to measure impact.

**What changed:** Added dual-layer safety net (PR-Agent + smoke tests) for prompt changes.
