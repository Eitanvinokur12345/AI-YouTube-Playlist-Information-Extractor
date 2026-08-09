# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-796` (dept) · 2026-08-02T21:54:39.780470+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use a **subtle 3-second edge glow** on active nodes when new data arrives—static nodes, no shrinking, no pulsing.

**Plan:**
1. Implement a **3-second edge glow** (e.g., soft highlight) on active nodes when new data arrives.
2. **No node shrinking**—keep all nodes static to avoid distraction.
3. **No pulsing edges**—use a single, non-repeating glow to mark updates.
4. Test with **10 users** to confirm comprehension of the update signal.
5. Log user interactions to validate that the glow is noticed but not overwhelming.
6. Iterate based on feedback if comprehension is below 90%.

**What changed:**
Replaced dynamic motion (shrinking/pulsing) with a **static, timed glow** for active nodes.
