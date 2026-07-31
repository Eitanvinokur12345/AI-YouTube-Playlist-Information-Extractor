# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-658` (dept) · 2026-07-31T03:20:12.500915+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with a one-time first-launch theme picker (dark/light/system) and a persistent toggle in settings—defaulting to system preference.

**Plan:**
1. Implement a first-launch modal with three theme options (Dark, Light, System) and store the choice in local storage.
2. Default to system preference if no selection is made within 5 seconds of launch.
3. Add a persistent toggle in settings (visible in the UI) to switch themes at any time.
4. Ensure the toggle updates the UI immediately without requiring a restart.
5. Test edge cases (e.g., system preference changes, toggle reversibility).
6. Document the behavior in user-facing help text.

**What changed:**
Added a reversible one-time picker + persistent toggle, defaulting to system preference.
