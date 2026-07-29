# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-961` (dept) · 2026-07-29T21:19:25.527535+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with system preference as the default theme, paired with a persistent, dismissible banner that lets users lock in their choice permanently—no toggle, no modal, just a single action that sticks.

**Plan:**
1. Set system preference as the default theme on first launch.
2. Display a persistent, non-modal banner at the top of the interface with two buttons: "Keep system theme" and "Set light theme".
3. If users click "Set light theme", apply the light theme and store the preference in local storage.
4. If users click "Keep system theme", dismiss the banner permanently and continue using system preference.
5. Remove the banner entirely for subsequent sessions if a preference was previously set.
6. Measure session length and glare complaints via A/B testing to validate the approach.

**What changed:**
Default theme now follows system preference with a one-time override prompt.
