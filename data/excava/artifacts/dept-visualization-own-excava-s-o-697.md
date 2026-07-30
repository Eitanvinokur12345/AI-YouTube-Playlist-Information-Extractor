# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-697` (dept) · 2026-07-30T17:46:56.928223+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with a one-time theme picker at first launch—defaulting to dark mode but remembering the user’s choice thereafter.

**Plan:**
1. Implement a first-run modal dialog at initial launch asking users to select a theme (Dark/Light).
2. Default selection to "Dark" but allow users to toggle to "Light" before confirming.
3. Store the user’s choice in `localStorage` under a key like `excavaTheme`.
4. On subsequent launches, read `localStorage` and apply the stored theme without showing the picker again.
5. Remove the theme toggle from the interface entirely—no persistent UI element remains.
6. Add a fallback to dark mode if `localStorage` is unavailable or unset.

**What changed:**
One-time theme picker replaces persistent toggle, defaulting to dark but respecting user choice thereafter.
