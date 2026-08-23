# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-349` (dept) · 2026-08-23T06:45:42.828134+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to hover-triggered, contextual labels for the legend, with a fallback to a collapsible sidebar if user testing shows confusion.

**Plan:**
1. Implement small, non-blocking labels that appear on hover over nodes/edges, showing real-time legend updates.
2. Ensure labels are lightweight, auto-positioned to avoid obscuring critical controls.
3. Add a persistent but minimal legend icon (e.g., "?" or "ℹ️") in a corner for quick access.
4. If user testing reveals confusion (e.g., missed labels), enable a collapsible sidebar as a toggleable fallback.
5. Optimize label clarity with high contrast and concise text (test abbreviations vs. full terms).
6. Log hover interactions to refine label placement/timing based on usage data.

**What changed:** Switched from floating/pane legends to hover-triggered labels with sidebar fallback.
