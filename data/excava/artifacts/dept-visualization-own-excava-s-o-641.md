# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-641` (dept) · 2026-07-28T23:05:29.584645+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Ship EXCAVA with a dark-first interface, user-controlled toggle, and opt-in ambient light switching.

**Plan:**
1. Default to dark theme for all users.
2. Add a one-click toggle (persistent across sessions) to switch between dark/light modes.
3. Include an optional onboarding prompt asking users if they want auto-switching based on ambient light.
4. Implement the auto-switch feature only if users explicitly opt in during onboarding.
5. Conduct A/B testing to measure toggle usage and auto-switch adoption rates.
6. Refine based on telemetry data (e.g., if <30% opt into auto-switch, deprecate the prompt).

**What changed:** Added user control (toggle) + optional opt-in auto-switching to balance flexibility and reduced friction.
