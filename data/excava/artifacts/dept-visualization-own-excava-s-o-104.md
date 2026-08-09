# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-104` (dept) · 2026-08-07T01:36:02.584778+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to a single high-contrast dark theme with adjustable saturation and font size, plus a *one-click* light theme toggle—test usage, measure maintenance cost, and ship in two weeks.

**Plan:**
1. Implement the high-contrast dark theme as default with adjustable saturation (0-100%) and font size (8-24px) via sliders in settings.
2. Add a *one-click* theme toggle (dark ↔ light) in the top-right corner with a warning: "Light mode is a maintenance-minimized fallback."
3. Log theme toggle usage and saturation/font adjustments for 2 weeks post-launch.
4. If >90% of users remain in dark mode, deprecate light theme maintenance after 30 days.
5. If <90% stay dark, prioritize light theme fixes in next sprint.
6. Document the decision and toggle behavior in EXCAVA’s public roadmap.

**What changed:**
Added a one-click light theme toggle to the high-contrast dark default, with usage tracking to validate the 90% threshold.
