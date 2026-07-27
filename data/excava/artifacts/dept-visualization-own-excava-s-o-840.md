# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-840` (dept) · 2026-07-27T06:56:13.745515+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a task-driven theme system with persistent override.

**Plan:**
1. Set dark theme as default for analysis tasks (e.g., data exploration, coding).
2. Set light theme as default for editing/presenting tasks (e.g., slide creation, report drafting).
3. Implement a persistent one-click toggle (e.g., top-bar switch) that overrides the task-based theme until manually reset.
4. Log theme changes in user settings for transparency and quick recovery.
5. Add a subtle indicator (e.g., small icon) showing the active theme source (task/override).
6. Test with 10% of users for 2 weeks, measuring override frequency and task completion time.

**What changed:**
Theme defaults now align with task type, with a sticky override to prevent habituation lock-in.
