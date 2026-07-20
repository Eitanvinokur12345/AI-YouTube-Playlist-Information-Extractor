# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-898` (dept) · 2026-07-20T17:50:22.440412+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Ship a post-submit contrast gate that flags WCAG AA violations in staging, blocking releases until fixed—no live checker, no pre-submit gate.

**Plan:**
1. Integrate a contrast checker into the staging deployment pipeline to analyze all text/UI elements against WCAG AA standards.
2. Configure the gate to fail the build and block releases if any violations are detected.
3. Require manual resolution of all flagged issues before staging can proceed to production.
4. Document the process and train teams on interpreting and fixing contrast failures.
5. Monitor false positives/negatives and adjust thresholds as needed.
6. Review the gate’s impact on release velocity quarterly and refine as necessary.

**What changed:** Replaced live and pre-submit contrast checks with a post-submit staging gate.
