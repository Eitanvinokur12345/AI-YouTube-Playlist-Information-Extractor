# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-460` (dept) · 2026-07-30T18:22:22.783169+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt ambient-light detection with auto-switching between dark/light themes by default, plus a manual override toggle.

**Plan:**
1. Implement ambient-light detection (e.g., via OS API or camera sensor) to auto-switch themes.
2. Add a persistent manual toggle in the top-right corner for user override.
3. Test glare-readability with 10 screencast users under both auto and manual modes.
4. Optimize theme transition speed to minimize perceived lag.
5. Default to dark theme for low-light screencasts, light theme for bright glare.
6. Document toggle discovery in a tooltip or first-run guide.

**What changed:** Auto-switching replaces static theme choice, with manual override retained.
