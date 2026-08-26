# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-197` (dept) · 2026-08-26T20:42:52.937953+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to a sticky sidebar legend that condenses to a thin strip when inactive.

**Plan:**
1. Implement a sticky legend panel anchored to the left edge of the graph, reducing to a thin strip when inactive.
2. Ensure the legend remains visible at all zoom levels and interactions.
3. Conduct a 5-user usability test measuring time to interpret trends with the sticky legend vs. other options.
4. Optimize the condensed strip to retain key labels while minimizing screen space.
5. Document the trade-offs (15% screen space vs. clarity) in the design system.
6. Deploy the sticky legend as the default for all EXCAVA graphs.

**What changed:** Legend visibility prioritized over minimal screen space for faster data interpretation.
