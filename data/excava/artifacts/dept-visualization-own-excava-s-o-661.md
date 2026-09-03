# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-661` (dept) · 2026-09-03T19:36:16.186641+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use a minimal, auto-hiding top banner that pulses briefly on updates, then retracts.

**Plan:**
1. Implement a thin, sticky top strip for critical alerts (high contrast, bright color).
2. Add auto-hide behavior: banner appears on data change, pulses briefly, then retracts.
3. Ensure the banner does not obscure the graph’s top edge when retracted.
4. Test with users: compare sudden data changes in both sticky and auto-hiding designs.
5. Optimize pulse animation for visibility without distraction.
6. Finalize banner dimensions to balance alert clarity and screen space.

**What changed:** Replaced sticky top strip with auto-hiding top banner to preserve graph visibility while ensuring liveliness.
