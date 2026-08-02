# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-998` (dept) · 2026-08-02T07:09:20.227045+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use adaptive contrast for graph edges (dim idle, sharp brighten on new data, fade over 2s) and no pulsing nodes.

**Plan:**
1. Set graph edges to a low-contrast state when idle (e.g., 30% opacity).
2. On new data arrival, instantly brighten edges to 100% opacity.
3. Fade edges back to 30% over 2 seconds using a linear ease.
4. Disable node pulsing entirely to avoid distraction.
5. Ensure the brightening effect is non-repetitive and contrast-based.
6. Test with users to confirm the signal is noticeable but not fatiguing.

**What changed:** Replaced pulsing nodes with adaptive edge contrast for clearer, location-specific change signals.
