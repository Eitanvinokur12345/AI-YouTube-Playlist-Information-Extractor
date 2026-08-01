# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-538` (dept) · 2026-07-30T19:31:49.310588+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with ambient-light detection auto-switching between dark and light themes by default, plus a one-time theme picker at first launch—defaulting to the detected theme.

**Plan:**
1. Implement OS-level ambient-light detection to auto-switch between dark/light themes.
2. Add a one-time theme picker at first launch, defaulting to the detected theme.
3. Include a persistent but non-intrusive theme toggle in the top-right for manual overrides.
4. Conduct A/B testing on glare complaints and task completion metrics for 2 weeks post-launch.
5. Iterate on contrast ratios and interactive element visibility based on user feedback.
6. Document the adaptive theme logic in the developer guide for future contributors.

**What changed:**
Replaced static theme selection with an adaptive, auto-switching system that respects user preference and ambient conditions.
