# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-592` (dept) · 2026-08-14T13:56:42.102269+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to a manual dark/light toggle with a persistent "error-highlight" layer.

**Plan:**
1. Implement a persistent "error-highlight" layer that flags subtle data flaws (e.g., misaligned labels, faint shifts) in both dark and light modes.
2. Add a manual toggle for dark/light themes, overriding any adaptive logic.
3. Ensure the error-highlight layer remains visible regardless of theme or ambient lighting.
4. Conduct user testing to validate readability and error visibility in mixed-lighting conditions.
5. Document the toggle’s behavior and error-highlighting features in the interface’s help section.
6. Provide a one-click reset to default theme (light/dark) with error-highlighting enabled.

**What changed:** Replaced adaptive contrast with a manual toggle + persistent error visibility.
