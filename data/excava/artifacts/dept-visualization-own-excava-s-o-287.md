# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-287` (dept) · 2026-08-03T01:56:31.739845+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use a **subtle 3-second edge glow** on active nodes when new data arrives, and a **single bright flash** on idle nodes—then test which reduces habituation without missing freshness.

**Plan:**
1. Implement edge glow (3s duration) for active nodes on new data arrival.
2. Add a single bright flash (1s) for idle nodes when new data arrives.
3. Log interaction events to track user attention to flashes/glows.
4. A/B test two variants: glow-only vs. flash-only vs. combined.
5. Measure habituation via missed freshness events and user feedback.
6. Iterate based on data, defaulting to the more effective variant.

**What changed:**
Nodes now signal freshness with brief, non-repetitive visual cues instead of constant motion.
