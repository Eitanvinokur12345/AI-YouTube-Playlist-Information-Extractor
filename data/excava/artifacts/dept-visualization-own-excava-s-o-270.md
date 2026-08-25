# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-270` (dept) · 2026-08-25T17:08:45.571402+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
A hybrid legend that balances speed, clarity, and adaptability.

**Plan:**
1. Implement hover-triggered contextual labels for the legend, appearing instantly on data point hover.
2. Add a sticky, collapsible legend anchor on the left edge of the graph, toggled by a single click.
3. Include a pause-to-stick feature: the legend sticks when the user pauses interaction, fading if they scroll away.
4. Ensure the legend dynamically repositions to avoid dead zones near dense data clusters.
5. Provide a user preference to toggle between hover-only and sticky modes.
6. Optimize rendering to maintain speed even with dense data.

**What changed:** Added a hybrid legend system with hover-triggered labels, a sticky collapsible anchor, and pause-to-stick behavior.
