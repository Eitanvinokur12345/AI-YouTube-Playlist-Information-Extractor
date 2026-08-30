# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-754` (dept) · 2026-08-30T02:40:23.435427+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Anchor the legend to the bottom edge with a micro-interaction—hover or single click to summon it, then auto-hide after 3 seconds.

**Plan:**
1. Implement a thin, anchored legend strip at the bottom edge of the graph, collapsed by default.
2. Trigger legend visibility on hover *or* single click (toggle if clicked, auto-show if hovered).
3. Auto-hide legend after 3 seconds of inactivity (reset timer on hover/click).
4. Test both hover and click interactions with 5 users, measuring discovery time and perceived intrusiveness.
5. Refine interaction based on test results (e.g., adjust auto-hide duration or add a subtle fade-in).
6. Ensure legend content remains readable and interactive (e.g., clickable items) even when visible.

**What changed:**
Legend now appears via micro-interaction at the bottom edge instead of a permanent panel or hidden icon.
