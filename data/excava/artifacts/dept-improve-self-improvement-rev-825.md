# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-825` (dept) · 2026-08-01T19:46:40.978576+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:** Auto-apply only changes that pass a pre-approved, audited test suite (no logic changes, no new dependencies, no model access tweaks) and log the rest for review.

**Plan:**
1. Define a minimal, audited test suite (e.g., linting, formatting, dependency version checks) with explicit pass/fail criteria.
2. Establish a review process for adding new "safe" change types to the auto-apply list (requires maintainer approval + test coverage).
3. Implement logging for all auto-applied changes with diffs and test results.
4. Route all other changes (including typo fixes beyond formatting) to manual review.
5. Publish the policy in a `SAFE_CHANGES.md` file with examples and approval workflows.
6. Add a pre-commit hook to enforce the policy before changes are applied.

**What changed:** Policy now requires audited test suite validation for auto-applied changes.
