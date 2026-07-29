# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-971` (dept) · 2026-07-29T20:58:38.708678+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with dark mode defaulting to system preference on first launch, but expose a visible toggle in the top-right corner of the interface at all times—no forced sync after initial detection.

**Plan:**
1. Set dark theme as default on first launch.
2. Detect system preference and apply it automatically on first run.
3. Add a persistent toggle (top-right corner) for manual override.
4. Store user’s toggle choice in local storage for future sessions.
5. Ensure toggle is clearly labeled (e.g., "Dark Mode" / "Light Mode").
6. Test toggle visibility with a small subset of users for clarity.

**What changed:**
Default sync on first launch + persistent manual toggle.
