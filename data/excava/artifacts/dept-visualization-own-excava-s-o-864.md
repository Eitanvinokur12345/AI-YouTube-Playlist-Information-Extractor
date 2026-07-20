# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-864` (dept) · 2026-07-20T23:04:38.224003+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a live contrast checker inside the design tool with real-time red flashes on violations, paired with a pre-commit hook that blocks merges only after the designer confirms they’ve seen the warning.

**Plan:**
1. Integrate a live contrast checker into the design tool that flags WCAG AA violations with red flashes during editing.
2. Add a confirmation dialog when violations persist after a set delay (e.g., 5 seconds), requiring the designer to acknowledge the issue.
3. Implement a pre-commit hook that blocks merges only if contrast failures remain *after* the designer has confirmed the warning.
4. Log all violations and confirmations for auditability in the design tool’s history.
5. Optimize the checker to minimize performance impact during rapid prototyping.
6. Document the behavior in the design tool’s help system and onboarding flow.

**What changed:**
Added real-time visual feedback *inside* the design tool with a confirmation-required pre-commit hook for unresolved contrast violations.
