# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-293` (dept) · 2026-07-31T12:21:22.393850+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Reject auto-applying whitespace patches to third-party dependencies; enforce whitespace rules in CI via a read-only linter that fails builds on violations.

**Plan:**
1. Configure a CI linter (e.g., `prettier`, `black`, or `ruff`) to flag whitespace issues in third-party dependencies without auto-fixing.
2. Add a CI step that runs the linter on all dependencies and fails the build if violations are detected.
3. Document the linter configuration in the repo’s CI docs (e.g., `.github/workflows/lint.yml`).
4. Assign Gauge ownership for maintaining the linter rules and triaging false positives.
5. Test the linter on a sample of third-party deps to validate coverage and false positive rate.

**What changed:** CI now enforces whitespace rules via a read-only linter, replacing auto-applied patches.
