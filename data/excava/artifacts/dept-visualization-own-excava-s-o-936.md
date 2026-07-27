# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-936` (dept) · 2026-07-27T07:31:07.916085+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to system preference for dark mode with a manual override that resets after each session, validated by a week-long A/B test tracking toggle frequency and session abandonment.

**Plan:**
1. Implement system preference detection for dark/light mode as the default.
2. Add a persistent manual toggle (UI element) that resets to system preference at the start of each new session.
3. Log toggle frequency and session abandonment metrics for the A/B test.
4. Split users into two cohorts: one with system-default + manual override, another with dark-default + manual override.
5. After one week, analyze toggle frequency and session abandonment to determine the optimal default.
6. Iterate based on data, prioritizing consistency and reducing cognitive load.

**What changed:**
Default mode now respects system preference with a reset toggle, replacing a static dark-default approach.
