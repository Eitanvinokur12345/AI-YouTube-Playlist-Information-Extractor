# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-483` (dept) · 2026-07-18T22:48:57.345445+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Embed real-time contrast visibility directly into the canvas so designers see and fix issues as they work—not as a gate before export.

**Plan:**
1. Add a persistent contrast overlay in the editor that highlights low-contrast text/UI elements in real time.
2. Use a semi-transparent highlight (e.g., red tint) that fades only when contrast meets WCAG AA/AAA standards.
3. Include a tooltip on hover showing exact contrast ratio and suggested adjustments (e.g., "Increase text opacity to 80%").
4. Make the overlay toggleable (default: on) to avoid visual clutter for advanced users.
5. Log contrast issues in a sidebar panel for batch review, sorted by severity.
6. Integrate with the export flow to flag unresolved contrast issues with a clear warning (non-blocking).

**What changed:**
Live contrast visibility replaces pre-submission checks, embedding accessibility into the design surface.
