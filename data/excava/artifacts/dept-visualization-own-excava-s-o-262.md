# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-262` (dept) · 2026-08-21T01:43:39.021483+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to a manual dark/light toggle with persistent error-highlight mode.

**Plan:**
1. Set dark theme with high-contrast accents (bright orange/red) as default.
2. Add a persistent manual toggle (top-right) for light/dark mode.
3. Implement a red flash on validation failures (error-highlight mode) that persists until resolved.
4. Conduct A/B tests for 2 weeks measuring error rates and user fatigue between adaptive vs. manual toggle.
5. After testing, finalize toggle placement and error-highlight behavior based on data.
6. Document the theme system in the UI style guide.

**What changed:** Added manual toggle + persistent error-highlight mode to dark theme.
