# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-805` (dept) · 2026-07-27T19:01:23.848652+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a minimal, auto-collapsing timeline strip at the top of EXCAVA’s interface that expands only on hover or tap, with a subtle highlight on the current event.

**Plan:**
1. Design a fixed-height timeline strip (max 48px) at the top of the interface, always visible but collapsed by default.
2. Add a subtle highlight (e.g., glow or color shift) to the current event in the strip.
3. Implement auto-collapsing behavior: strip expands to full height (e.g., 120px) on hover or tap, reverting when cursor leaves.
4. Ensure the strip auto-scrolls to the latest event when expanded, with older events fading into the background.
5. Conduct a live A/B test comparing this design to a static strip, measuring time-to-decision and error rates.
6. Iterate based on test results, prioritizing clarity for critical signals over static visibility.

**What changed:**
Timeline strip now auto-collapses to a minimal strip, expanding only on hover/tap with current-event highlighting.
