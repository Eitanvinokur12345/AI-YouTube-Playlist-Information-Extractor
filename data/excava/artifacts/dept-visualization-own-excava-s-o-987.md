# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-987` (dept) · 2026-08-03T01:37:19.625032+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a single bright flash (500ms) on idle nodes when new data arrives.
2. Add a subtle 3-second edge glow (low opacity, soft color) to active nodes.
3. Disable node shrinking or color shifts to avoid visual fatigue.
4. Ensure flashes are high-contrast but brief to prevent habituation.
5. Test with users to confirm signals are noticeable but not overwhelming.
6. Log user interactions to refine flash timing/color if needed.

**What changed:** Replaced dynamic sizing/color with a single flash + edge glow for clarity and liveliness.
