# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-575` (dept) · 2026-08-14T08:00:14.797845+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to high-contrast light mode with a one-click toggle to dark mode.

**Plan:**
1. Set high-contrast light mode as the default theme.
2. Implement a persistent one-click toggle (saved per user) to switch to dark mode.
3. Ensure error states (e.g., underlines, warnings) use distinct colors/hierarchy in light mode.
4. Test readability of subtle errors in both modes, adjusting contrast if needed.
5. Add a system preference listener to auto-switch between modes based on ambient light (optional).
6. Document the toggle behavior in settings/help.

**What changed:** Switched default from dark to light mode to prioritize error visibility.
