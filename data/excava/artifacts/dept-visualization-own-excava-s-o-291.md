# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-291` (dept) · 2026-08-09T11:28:49.658390+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to system preference at first launch, then remember the user’s last choice with a one-click toggle between dark/light modes.

**Plan:**
1. Implement system preference detection on first launch.
2. Store user’s last theme choice (dark/light) in local storage.
3. Add a persistent one-click toggle in the interface header.
4. Ensure muted alerts/errors remain visible in both themes.
5. Conduct a 2-week A/B test measuring error detection accuracy.
6. Refine theme persistence logic based on A/B test results.

**What changed:** Defaults to system preference, remembers user choice, and prioritizes visibility of critical data.
