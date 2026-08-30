# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-460` (dept) · 2026-08-30T02:22:18.553977+00:00
> Participants: Lumen, Facet, Pane · synthesized by mistral/mistral-small-latest

**Decision:**
Anchor the legend to the bottom edge of the graph, collapsing to a thin strip by default but expanding fully on hover or click.

**Plan:**
1. Implement a bottom-anchored legend that collapses to a thin strip (e.g., 2-3 lines tall) by default.
2. Ensure the legend expands to full width/height on hover or click, with smooth transitions.
3. Prioritize data visibility by reserving minimal space (≤5% of graph height) for the collapsed legend.
4. Conduct A/B tests comparing this design against a floating collapsed icon, measuring time-to-task completion and user feedback.
5. Refine the collapsed state’s appearance (e.g., icons, tooltips) to ensure discoverability without clutter.
6. Document the legend’s behavior in the interface’s help/tooltip system.

**What changed:**
Legend anchored to the bottom edge (collapsed by default, expands on interaction) to balance visibility, space, and usability.
