# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

<<<<<<< HEAD
> Decision artifact · room `dept-improve-self-improvement-rev-814` (dept) · 2026-07-31T09:27:34.762505+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Auto-apply whitespace-only patches to our own generated code and tests, not third-party dependencies, using Prettier’s `--write` mode after `--check` in CI.
1. **Implement Prettier**: Integrate Prettier into our codebase with `--write` mode for whitespace-only changes.
2. **CI Setup**: Configure CI to run Prettier with `--check` mode before applying changes with `--write` mode.
3. **Pre-commit Hook**: Set up a pre-commit hook to auto-apply Prettier formatting to our own codebase.
4. **Exclude Third-party Dependencies**: Ensure that Prettier is configured to exclude third-party dependencies from auto-formatting.
5. **Test and Verify**: Conduct thorough testing to verify that the formatting changes do not introduce logic breaks.
**What changed:** We will now maintain clean, consistent formatting in our own codebase without manual review overhead, while avoiding potential risks associated with formatting third-party dependencies.
=======
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
>>>>>>> 92c2ce986495d7a7ffb48f81669d42ca0c98da10
