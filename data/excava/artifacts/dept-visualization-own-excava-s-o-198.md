# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-198` (dept) · 2026-07-20T17:13:43.584613+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a real-time contrast overlay that flashes red on violations *while designers work*, paired with a pre-submit gate that blocks merges only if the overlay was ignored.

**Plan:**
1. Implement a real-time contrast checker in the design tool (Figma/Sketch/etc.) that overlays AA/AAA scores on elements.
2. Flash red on elements failing WCAG AA contrast when hovered or selected.
3. Log all violations in a persistent panel (e.g., "Contrast Issues") with quick-fix suggestions.
4. Add a pre-submit Git hook that checks the design file’s contrast log—blocks merges if unresolved violations exist.
5. Document the overlay’s behavior and gate’s rules in the team’s design system guidelines.
6. Monitor false positives/negatives for 2 weeks, adjust thresholds as needed.

**What changed:**
Replaced live build-time checker and strict gate with a real-time overlay + conditional pre-submit gate.
