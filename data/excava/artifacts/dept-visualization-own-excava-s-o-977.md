# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-977` (dept) · 2026-08-23T09:00:26.224094+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Embed the legend as a semi-transparent overlay on the graph canvas, fading on idle but reappearing instantly on hover or click—balancing visibility, context, and control without sacrificing screen space.

**Plan:**
1. Render the legend as a semi-transparent overlay directly on the graph canvas.
2. Fade the overlay to near-invisibility after 3 seconds of idle time.
3. Restore full opacity instantly on hover or click anywhere in the graph area.
4. Ensure the overlay is positioned to avoid obscuring critical controls (e.g., buttons, axes).
5. Test with edge cases (e.g., small screens, dense data points) to confirm non-blocking behavior.
6. Add a toggle in settings to disable fading for users who prefer persistent visibility.

**What changed:**
Legend now overlays the graph canvas as a semi-transparent, idle-fading element that never blocks controls.
