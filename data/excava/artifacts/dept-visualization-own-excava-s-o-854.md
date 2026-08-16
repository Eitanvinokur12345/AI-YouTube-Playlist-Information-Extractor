# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-854` (dept) · 2026-08-16T22:51:12.486919+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Default to a user-toggleable "error-highlight mode" (red flash on misaligned nodes) with a persistent one-click dark/light toggle—both modes start high-contrast.

**Plan:**
1. Implement a persistent UI toggle (top-right) switching between dark/light themes while preserving high-contrast accents in both.
2. Add a "Highlight Errors" toggle (default off) that flashes misaligned nodes in red when enabled.
3. Pre-render error states with high-contrast outlines (no latency) for instant visibility.
4. Include a 5-minute user test to validate error-highlight clarity in mixed-lighting rooms.
5. Optimize rendering to ensure toggles and error flashes complete in <100ms.
6. Document theme/contrast behavior in the first-run tutorial.

**What changed:** Replaced adaptive contrast with a toggleable error-highlight mode to eliminate latency while ensuring errors are unmissable.
