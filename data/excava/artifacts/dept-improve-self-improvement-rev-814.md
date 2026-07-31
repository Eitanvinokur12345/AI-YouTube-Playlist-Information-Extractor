# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-814` (dept) · 2026-07-31T07:58:35.977691+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply whitespace-only patches to own generated code and third-party dependencies (excluding minified/obfuscated files) after Prettier `--check` validation.

**Plan:**
1. Configure Prettier to run `--check` in CI for all modified files (own code + third-party dependencies).
2. Add a pre-commit hook to auto-format own generated code with `--write` if `--check` passes.
3. For third-party dependencies, auto-apply `--write` patches via a CI post-processing step *only* if `--check` succeeds.
4. Exclude minified/obfuscated files (e.g., `*.min.js`, `vendor/`) from auto-formatting.
5. Log all auto-applied changes in CI for auditability.
6. Document the policy in `CONTRIBUTING.md` and team onboarding.

**What changed:**
Whitespace-only auto-formatting now applies to safe targets (own code + formatted third-party deps) with CI validation.
