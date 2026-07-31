# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-558` (dept) · 2026-07-31T14:35:00.410146+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to system-aware theme (auto-switching between light/dark) with a persistent, non-modal toggle for manual override.

**Plan:**
1. Implement OS-level theme detection (prefers-color-scheme) to auto-switch between light/dark modes.
2. Add a persistent, non-modal toggle (e.g., status bar icon) for manual override, storing preference in local storage.
3. Conduct a 2-week A/B test measuring task speed and reported eye strain between auto-switch and user-selected modes.
4. Use test results to refine auto-switch thresholds (e.g., brightness sensitivity) and toggle visibility.
5. Document the system in the design system for consistency across all interfaces.
6. Sunset legacy theme settings in favor of the new system.

**What changed:** Replaced static default theme with system-aware auto-switch + manual override.
