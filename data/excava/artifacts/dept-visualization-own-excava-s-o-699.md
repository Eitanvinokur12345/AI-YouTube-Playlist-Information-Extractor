# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-699` (dept) · 2026-07-30T14:45:09.335865+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with a one-time theme picker at first launch (defaulting to system preference) and persist the user’s choice thereafter.

**Plan:**
1. Implement a one-time theme picker at first launch, defaulting to system preference.
2. Store the user’s choice in local storage/session to persist across sessions.
3. Include a one-click toggle in the settings panel to switch themes at any time.
4. Conduct a 2-week A/B test comparing:
   - Dark default + persistent toggle
   - Light default + persistent toggle
   - System default + persistent toggle
5. Measure theme-switch frequency and user satisfaction via analytics.
6. Refine based on A/B test results and ship the winning configuration.

**What changed:**
Replaced default dark mode with system preference + one-time picker + persistence.
