# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-374` (dept) · 2026-07-20T18:27:39.733997+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a pre-submit contrast gate that blocks publishing until WCAG 2.1 AA contrast passes, paired with a live checker that trains designers to spot issues early—not as a gate, but as a habit.

**Plan:**
1. Implement a pre-submit CI gate that fails builds with any WCAG 2.1 AA contrast violations.
2. Integrate a live contrast checker into the design tool (Figma/Sketch) that highlights issues in real time.
3. Add a "contrast training mode" in the live checker to surface issues without blocking workflows.
4. Document contrast best practices and embed them in design system templates.
5. Run weekly contrast audits on published releases to catch regressions.
6. Measure and share contrast compliance metrics in team dashboards.

**What changed:**
Pre-submit gates enforce accessibility standards, while live feedback builds habits to prevent violations early.
