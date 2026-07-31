# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-487` (dept) · 2026-07-31T06:04:49.169617+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by mistral/mistral-small-latest

**Decision:**
Auto-apply formatting-only patches to our own generated code, where human logic isn't involved, to keep it clean without hiding deeper issues.

**Plan:**
1. Identify and tag all generated code directories/modules in the repo.
2. Implement a rule in the self-improvement pipeline to auto-apply formatting-only patches (spaces, line breaks, indentation) exclusively to tagged generated code.
3. Add a pre-commit hook to validate that no logic-altering changes are included in patches to generated code.
4. Update the pipeline’s configuration to log and surface any formatting-only patches applied to generated code for review.
5. Document the new rule in the repo’s CONTRIBUTING.md under "Self-Improvement Pipeline."
6. Assign the lead to own the pipeline update and enforce the rule within 2 weeks.

**What changed:** Generated code now auto-formatted; human-owned code remains untouched.
