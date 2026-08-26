# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-871` (dept) · 2026-08-26T13:38:16.812524+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Make the legend a sticky sidebar that collapses to a thin strip when users zoom or scroll, with a clear toggle to expand it—balancing visibility and space.

**Plan:**
1. Implement a left-edge sticky sidebar for the legend that remains visible during scrolling/zooming.
2. Add a collapse/expand toggle that shrinks the legend to a thin vertical strip when users zoom into dense data.
3. Ensure the collapsed strip includes a visible handle (e.g., a small arrow or icon) to reopen the legend.
4. Test user intuitiveness with a prototype to confirm the toggle is discoverable without obscuring data.
5. Optimize the sidebar’s width to minimize crowding while maintaining readability of legend items.
6. Include a subtle animation for collapsing/expanding to reinforce the toggle’s purpose.

**What changed:**
Legend shifted from a static sticky panel to a collapsible sidebar with a toggle, optimizing space and visibility.
