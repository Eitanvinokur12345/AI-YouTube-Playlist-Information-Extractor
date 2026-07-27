# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-323` (dept) · 2026-07-27T22:11:24.011316+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Fixed-height timeline strip at the top of EXCAVA, always visible, with a single "Focus Mode" toggle to collapse it when users need vertical space for dense data.

**Plan:**
1. Implement a fixed-height timeline strip at the top of EXCAVA’s interface, spanning the full project duration.
2. Ensure the strip is always visible unless "Focus Mode" is toggled.
3. Add a single "Focus Mode" button to collapse the timeline strip, reclaiming vertical space for other panels.
4. Test the toggle’s usability with real users, focusing on Manus’s dark-themed graphs to validate clarity and speed.
5. Optimize the strip’s rendering for performance, ensuring it remains responsive even with dense data.
6. Document the toggle’s behavior and edge cases (e.g., auto-collapse on full-screen modes).

**What changed:** Timeline strip is now fixed-height and always visible, with a single "Focus Mode" toggle to collapse it.
