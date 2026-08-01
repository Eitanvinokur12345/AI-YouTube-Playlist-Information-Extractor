# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-762` (dept) · 2026-07-31T18:02:06.694165+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to a single dark theme with a manual brightness slider.

**Plan:**
1. Implement a dark theme as the default interface for Excava.
2. Add a persistent, visible brightness slider (0–100%) that overrides the dark theme’s contrast.
3. Remove all auto-switching logic (light/dark or brightness) to prevent jarring shifts.
4. Store user brightness preferences in local storage for persistence across sessions.
5. Conduct a 1-week A/B test comparing task completion speed vs. the debated manual toggle.
6. Refine slider UX based on A/B test feedback (e.g., granularity, visibility).

**What changed:** Replaced light/dark toggle and auto-switching with a single dark theme + manual brightness slider.
