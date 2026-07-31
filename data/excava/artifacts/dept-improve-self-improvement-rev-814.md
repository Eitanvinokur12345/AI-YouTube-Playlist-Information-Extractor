# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-814` (dept) · 2026-07-31T09:27:34.762505+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Auto-apply whitespace-only patches to our own generated code and tests, not third-party dependencies, using Prettier’s `--write` mode after `--check` in CI.
1. **Implement Prettier**: Integrate Prettier into our codebase with `--write` mode for whitespace-only changes.
2. **CI Setup**: Configure CI to run Prettier with `--check` mode before applying changes with `--write` mode.
3. **Pre-commit Hook**: Set up a pre-commit hook to auto-apply Prettier formatting to our own codebase.
4. **Exclude Third-party Dependencies**: Ensure that Prettier is configured to exclude third-party dependencies from auto-formatting.
5. **Test and Verify**: Conduct thorough testing to verify that the formatting changes do not introduce logic breaks.
**What changed:** We will now maintain clean, consistent formatting in our own codebase without manual review overhead, while avoiding potential risks associated with formatting third-party dependencies.
