# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-786` (dept) · 2026-08-26T05:08:44.794061+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to a sticky sidebar legend that shrinks to a thin strip when zoomed.

**Plan:**
1. Implement a sticky sidebar legend anchored to the left edge of the graph.
2. Design the legend to automatically shrink into a thin vertical strip when users zoom into dense data clusters.
3. Ensure the shrunk strip retains a visible icon for quick expansion, maintaining accessibility.
4. Test user interactions to confirm the legend remains discoverable during zooming and panning.
5. Optimize the transition animation between expanded and collapsed states for smoothness.
6. Document the behavior in the interface’s help/tooltip system.

**What changed:** Legend transitions from expanded sidebar to thin strip on zoom, keeping it always visible.
