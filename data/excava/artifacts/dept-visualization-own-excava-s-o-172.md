# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-172` (dept) · 2026-08-27T14:32:34.808551+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Anchor the legend to the bottom edge, visible by default but collapsible to a thin strip when unused.

**Plan:**
1. Implement a bottom-anchored legend panel with a default height of 10% of screen space.
2. Add a collapsible toggle (e.g., chevron or "Collapse" button) to shrink the legend to a 30px-high strip when unused.
3. Ensure the legend remains fully visible during scroll/zoom but auto-collapses after 5 seconds of inactivity.
4. Test with 20% of users to validate legend usage frequency and adjust collapse timing if needed.
5. Add a subtle hover tooltip ("Click to expand") on the collapsed strip for discoverability.
6. Log interaction data to confirm legend access rates and refine default collapse behavior.

**What changed:**
Legend moved from left-edge sticky to bottom-anchored collapsible panel.
