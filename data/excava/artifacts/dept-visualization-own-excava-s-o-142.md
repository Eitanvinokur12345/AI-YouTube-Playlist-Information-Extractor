# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-142` (dept) · 2026-07-31T15:10:37.966173+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to system-aware theme with manual brightness slider override.

**Plan:**
1. Implement auto-switching between light/dark themes based on ambient light sensors (default: dark).
2. Add a manual brightness slider controlled via hotkey (e.g., `Ctrl+Shift+B`).
3. Build glare detection logic to prioritize readability in bright rooms.
4. Conduct a 5-user hallway test to measure squint time and adjust slider sensitivity.
5. Document the system toggle’s behavior and hotkey usage in the interface.
6. Assign Facet as the owner for glare detection and slider control implementation.

**What changed:** Added manual brightness slider override to system-aware theme.
