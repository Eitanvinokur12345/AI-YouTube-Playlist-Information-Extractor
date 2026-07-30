# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-897` (dept) · 2026-07-30T19:52:59.334727+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with ambient-light detection auto-switching between dark and light themes by default, plus a one-time theme picker at first launch for users who override the system choice.

**Plan:**
1. Implement ambient-light detection (e.g., via device sensors or OS API) to auto-switch themes based on environment.
2. Add a one-time theme picker at first launch (defaulting to system preference) with options: "System," "Dark," or "Light."
3. Ensure the persistent interactive graph remains high-contrast in all themes.
4. Conduct A/B testing on a subset of users to validate retention and satisfaction.
5. Provide a persistent one-click toggle in the top-right corner for manual overrides.
6. Document accessibility compliance (WCAG contrast ratios) for both themes.

**What changed:**
Auto-adaptive themes with user override, replacing static default choices.
