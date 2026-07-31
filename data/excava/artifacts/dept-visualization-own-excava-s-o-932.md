# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-932` (dept) · 2026-07-31T01:54:01.913927+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Ship EXCAVA with a one-time first-launch theme picker (dark/light/system) with a "remember my choice" checkbox.
2. Default to system preference if the user closes the picker without selecting an option.
3. Log all theme toggles post-first-launch to track usage frequency.
4. If >20% of users change their theme after first launch, add a persistent top-right theme toggle.
5. Ensure the toggle state persists across sessions and respects the user’s choice.
6. Include a fallback to system preference if the user reopens the picker and selects "system."

**What changed:** First-launch picker replaces persistent default; toggle added only if >20% usage.
