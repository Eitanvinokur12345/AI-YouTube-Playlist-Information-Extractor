# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-936` (dept) · 2026-08-07T00:56:24.255740+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use a single high-contrast dark theme with adjustable saturation and font size for all users—no system toggle.

**Plan:**
1. Implement a single high-contrast dark theme as the default interface.
2. Add adjustable saturation controls (0-100%) and font size (S/M/L/XL) sliders.
3. Preload user preferences locally (browser/localStorage) to retain settings across sessions.
4. Conduct a 2-week A/B test with 10% of users to validate accessibility and performance.
5. Document the theme’s accessibility compliance (WCAG 2.1 AA) in the repo’s README.
6. Sunset all light/auto-toggle features and related code branches.

**What changed:** Removed system toggle, enforced dark theme, added granular user controls.
