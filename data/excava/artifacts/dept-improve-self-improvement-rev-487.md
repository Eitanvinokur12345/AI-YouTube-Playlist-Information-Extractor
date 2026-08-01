# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-487` (dept) · 2026-07-31T21:07:04.713245+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply formatting-only patches to our own generated code and prompt files, excluding logic-bearing code, to avoid masking decay while keeping the repo clean.

**Plan:**
1. Identify and tag generated code and prompt files in the repo (e.g., via `.generated` suffix or directory).
2. Implement a CI rule to auto-apply formatting-only patches (spaces, line breaks, indentation) to tagged files.
3. Exclude logic-bearing files (e.g., core logic, engines) from auto-formatting to prevent false cleanliness.
4. Add a pre-commit hook to validate formatting changes before allowing merges.
5. Document the rule in `CONTRIBUTING.md` and notify the team.
6. Assign the lead to own the pipeline and review edge cases quarterly.

**What changed:**
Auto-formatting now targets only generated code/prompts, excluding logic-bearing files.
