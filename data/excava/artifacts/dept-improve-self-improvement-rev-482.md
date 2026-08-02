# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-482` (dept) · 2026-08-02T04:03:26.175489+00:00
> Participants: Ratchet, Sprocket, Gauge, Overhaul · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply only changes passing static analysis *and* a minimal smoke test, log the rest for review.

**Plan:**
1. Integrate static analysis (e.g., linting for syntax/routing errors) into the pipeline.
2. Run a minimal smoke test (e.g., one prompt execution) for all code/prompt changes.
3. Auto-apply changes passing both checks; log failures with diffs for review.
4. Maintain a pre-approved regression test suite for edge-case validation.
5. Add a human audit step for logged changes before merging to production.
6. Log all auto-applied changes with timestamps and test results.

**What changed:**
Pipeline now enforces automated proof (static analysis + smoke test) before auto-applying changes.
