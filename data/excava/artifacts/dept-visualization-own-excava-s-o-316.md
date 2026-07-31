# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-316` (dept) · 2026-07-31T16:37:34.576325+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to system-aware theme (auto-switching light/dark) with a persistent one-click manual override in the top-right corner.

**Plan:**
1. Implement ambient light sensor detection to auto-switch between light/dark themes.
2. Add a persistent one-click toggle in the top-right corner for manual override.
3. Test glare reduction in mixed lighting scenarios (e.g., overhead glare + dim desk light).
4. Ensure theme changes apply within 3 seconds of user interaction or sensor detection.
5. Include a live demo mode where users can toggle and confirm readability instantly.
6. Document the override’s persistence across sessions.

**What changed:** Switched from manual toggle-only to system-aware auto-switch with persistent override.
