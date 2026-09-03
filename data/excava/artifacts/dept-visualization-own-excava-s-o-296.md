# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-296` (dept) · 2026-09-03T19:18:46.487863+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a thin, sticky top strip (bright, high-contrast) for critical alerts, ensuring instant visibility.
2. Design a collapsible left sidebar that collapses to an icon-only strip on hover, matching the dark theme.
3. Ensure the top strip remains sticky even when the sidebar is collapsed.
4. Test alert visibility in both expanded and collapsed sidebar states.
5. Optimize sidebar expansion speed to minimize delay.
6. Validate that alerts do not fragment the interface or blend into the dark theme.

**What changed:** Split alerts into a dedicated top strip while keeping navigation in a collapsible sidebar.
