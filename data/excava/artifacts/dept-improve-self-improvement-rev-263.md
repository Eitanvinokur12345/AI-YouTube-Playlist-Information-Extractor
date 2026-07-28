# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-263` (dept) · 2026-07-28T07:18:55.154406+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Introduce a `single-line-safe-change` flag in prompts, restricted to typo fixes and minor documentation edits.
2. Integrate static analysis (e.g., linting) and test coverage checks to validate isolation of changes.
3. Route all flagged edits through Gauge’s enforced review pipeline before auto-application.
4. Block broader context changes (e.g., variable renames, logic fixes) from auto-application.
5. Log all auto-applied changes for auditability in routing logic.
6. Gauge owns enforcement of validation rules and pipeline integration.

**What changed:** Auto-apply only `single-line-safe-change` edits validated by static analysis/test coverage.
