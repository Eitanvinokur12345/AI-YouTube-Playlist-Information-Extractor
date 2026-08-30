# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-120` (dept) · 2026-08-30T02:58:27.866962+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Anchor the legend as a thin, persistent sidebar that collapses to a tab when unused.

**Plan:**
1. Implement a thin vertical sidebar (e.g., 40px width) anchored to the graph’s right edge.
2. Default state: Sidebar is visible with legend items in a compact, high-contrast list.
3. Collapse to a tab (e.g., a vertical "≡" icon) when users interact with the graph or after 5 seconds of inactivity.
4. Hovering the tab expands the sidebar instantly; clicking pins it open.
5. Ensure the sidebar’s position is fixed relative to the graph container, not the viewport.
6. Test with users to confirm visibility and minimize screen space trade-offs.

**What changed:**
Replaced floating collapsed legend with a persistent, collapsible sidebar to balance visibility and space efficiency.
