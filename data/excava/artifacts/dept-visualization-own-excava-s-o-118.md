# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-118` (dept) · 2026-07-27T18:40:08.826282+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use a fixed-height live timeline strip at the top of EXCAVA with a high-contrast badge for the newest event only—older events shrink to half-height but remain scannable.

**Plan:**
1. Implement a fixed-height (e.g., 64px) timeline strip at the top of the interface.
2. Display the newest event in a high-contrast badge (e.g., bold color, subtle pulse animation).
3. Shrink older events to half-height (e.g., 32px) while maintaining readability.
4. Add a subtle glow behind the newest event badge for additional visibility.
5. Conduct user tests with high-volume event streams to validate event detection rates.
6. Iterate on badge contrast and animation based on test feedback.

**What changed:**
Timeline strip now uses a fixed-height with shrinking older events and a high-contrast badge for the newest event.
