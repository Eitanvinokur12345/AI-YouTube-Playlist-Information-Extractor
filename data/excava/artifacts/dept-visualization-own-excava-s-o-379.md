# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-379` (dept) · 2026-07-27T08:04:15.208712+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to system preference for dark mode, but override to high-contrast dark when graph data density exceeds a threshold—with a one-time manual override that persists until the next system preference change.

**Plan:**
1. Implement system preference detection for dark mode (default).
2. Add a contrast threshold for graph data density (e.g., >80% density triggers high-contrast dark).
3. Include a one-time manual override toggle (persists until next system preference change).
4. Test both defaults (system preference vs. manual override) in A/B trials.
5. Log habituation failures (e.g., toggles in bright rooms without reverting).
6. Refine threshold and persistence logic based on test data.

**What changed:**
System dark mode default with adaptive high-contrast override and persistent manual toggle.
