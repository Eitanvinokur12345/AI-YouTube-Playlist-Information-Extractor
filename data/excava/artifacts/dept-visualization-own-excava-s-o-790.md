# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-790` (dept) · 2026-07-27T19:21:02.529591+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Fixed-height timeline strip at the top of EXCAVA, always visible with a subtle "now" line—no collapsing.

**Plan:**
1. Implement a fixed-height (e.g., 48px) timeline strip at the top of the interface.
2. Add a subtle vertical line marking the current moment ("now") with a distinct color (e.g., blue).
3. Ensure the strip remains visible at all times, even when scrolling the main view.
4. Log user interactions to measure event visibility under pressure (target: <5% missed key events).
5. Conduct a live A/B test comparing fixed-height vs. collapsible timeline, tracking decision speed and accuracy.
6. Finalize the fixed-height design if test results meet the <5% threshold; otherwise, iterate.

**What changed:** Timeline is now a fixed-height strip at the top with a "now" marker, prioritizing clarity over density.
