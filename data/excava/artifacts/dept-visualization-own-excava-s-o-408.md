# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-408` (dept) · 2026-09-01T03:20:42.322166+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Anchor the legend as a slim, high-contrast bar at the top that collapses to a single icon when unused.

**Plan:**
1. Implement a top-anchored bar with high-contrast colors (e.g., dark background, light text/icons).
2. Add a collapse toggle (single icon) that minimizes the bar to a fixed-width tab on the left/right.
3. Ensure the bar remains sticky (persistent during scrolling/zooming).
4. Test visibility by tracking user clicks to expand/collapse and time spent locating controls.
5. Measure graph space usage before/after to validate trade-offs.
6. Iterate based on user feedback and interaction data.

**What changed:**
Replaced the sidebar and full-width banner options with a hybrid top bar that balances visibility and space efficiency.
