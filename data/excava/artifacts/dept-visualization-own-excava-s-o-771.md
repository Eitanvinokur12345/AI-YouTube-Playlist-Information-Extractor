# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-771` (dept) · 2026-08-01T21:27:52.553444+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Make EXCAV’s graph the dominant visual element with adaptive contrast and a manual brightness slider.

**Plan:**
1. Center the graph as the primary UI element, with controls, legends, and tooltips minimized and secondary.
2. Implement a deep indigo dark theme by default for the graph.
3. Add a brightness slider for manual override, accessible but unobtrusive.
4. Integrate an ambient-light sensor to auto-adjust graph contrast and brightness in real time.
5. Use Manus’ adaptive contrast algorithm for stable ambient light conditions.
6. Fall back to the manual slider when ambient light is unstable or sensor data is unreliable.

**What changed:**
Added a fixed dark theme with both dynamic brightness sensor and manual slider for flexibility.
