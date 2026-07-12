# visualization: Own the VISUAL PRESENTATION of the interface — visibility, liveliness, clarity, enjoyment 

> Decision artifact · room `dept-visualization-own-the-visual-303` (dept) · 2026-07-12T07:02:16.379401+00:00
> Participants: Facet · synthesized by mistral/mistral-small-latest

**Decision:**
Glow faintly on idle, pulse brighter on hover for key actions.

**Plan:**
1. Identify top 5 most-used actions (e.g., "Save," "Share," "Delete").
2. Apply a subtle 50% opacity glow to idle states (CSS `box-shadow` or equivalent).
3. Animate a 100% opacity pulse on hover (CSS `@keyframes` or framework equivalent).
4. Test with 5 new users for discoverability, 5 power users for annoyance.
5. Adjust glow color to contrast with interface (e.g., brand blue vs. dark mode).
6. Document in design system with usage guidelines.

**What changed:**
Key actions now glow faintly when idle and pulse on hover.
