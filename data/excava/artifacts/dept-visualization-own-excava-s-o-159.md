# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-159` (dept) · 2026-07-31T00:15:02.926507+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to dark mode based on system preference with a persistent, dismissible toggle in settings—no one-time picker.

**Plan:**
1. Implement system preference detection for dark/light mode on first launch.
2. Default EXCAVA to dark mode if system preference is dark; otherwise, use light mode.
3. Add a persistent theme toggle in settings (e.g., top-right corner) that persists across sessions.
4. Ensure the toggle is dismissible (e.g., auto-hides after 3 seconds if unused).
5. Conduct A/B testing: 50% of users see dark default + toggle; 50% see one-time picker (control).
6. Measure retention, engagement, and theme-switching behavior post-launch.

**What changed:**
Dark mode defaults to system preference with a persistent toggle; one-time picker removed.
