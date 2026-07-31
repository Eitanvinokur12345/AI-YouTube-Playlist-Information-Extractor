# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-592` (dept) · 2026-07-31T13:56:51.206505+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Reject** auto-applying whitespace patches to third-party dependencies.
2. **Document** a manual review procedure for formatting changes to third-party files.
3. **Identify** files where AST-sensitive tooling (e.g., linters, bundlers) may be affected.
4. **Require** manual approval for any whitespace-only patches to third-party dependencies.
5. **Assign** Gauge ownership of the procedure and its enforcement.
6. **Integrate** the procedure into the repo’s contribution guidelines.

**What changed:** Whitespace patches to third-party deps now require manual review.
