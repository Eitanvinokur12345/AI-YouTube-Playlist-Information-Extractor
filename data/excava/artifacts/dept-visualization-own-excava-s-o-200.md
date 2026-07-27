# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-200` (dept) · 2026-07-27T05:46:14.414539+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to system theme on first load, with a one-time prompt offering permanent override in settings.

**Plan:**
1. Set dark theme as default high-contrast option for new users.
2. Detect system preference on first load and apply it automatically.
3. Display a one-time modal: *"Use system theme? [Keep] or [Set dark mode permanently]."*
4. Store user override in local storage/settings for future sessions.
5. Allow manual toggling in settings at any time.
6. A/B test system-default vs. dark-default with 50/50 split for 2 weeks.

**What changed:**
Default theme now respects system preference with a one-time override prompt.
