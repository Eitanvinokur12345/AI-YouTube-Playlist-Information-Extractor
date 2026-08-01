# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-737` (dept) · 2026-07-30T21:13:07.747236+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default the "Live Refresh" toggle to ON with a small, persistent indicator—users can pause it anytime, balancing CPU load with visibility.

**Plan:**
1. Implement a small, non-intrusive "Live" indicator (e.g., a pulsing dot) in the top-right corner of the interface.
2. Add a single toggle button labeled "Pause" (default state: "Live" is active) to control continuous playback.
3. Ensure the toggle defaults to ON (live mode) but allows users to pause at any time without mode commitment.
4. Test user awareness via A/B testing: compare static default vs. live default to measure feature discovery.
5. Optimize CPU usage by throttling refresh rate (e.g., 100ms intervals) when live mode is active.
6. Add a tooltip or brief onboarding hint explaining the "Live" indicator and pause functionality.

**What changed:**
Live mode now defaults to ON with a persistent indicator and pause control, improving visibility while maintaining user control.
