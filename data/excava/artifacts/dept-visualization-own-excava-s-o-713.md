# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-713` (dept) · 2026-08-09T02:38:10.948781+00:00
> Participants: Lumen, Facet, Pane · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt an auto-detecting dark/light theme with a persistent manual toggle, validated by a 10-user test measuring manual toggles vs. auto-switches.

**Plan:**
1. Implement auto-detecting dark/light theme based on ambient light sensors (or OS preference as fallback).
2. Add a persistent one-click toggle (e.g., top-right corner) to override auto-detection.
3. Store user preference per session and default to it on return, with a subtle indicator (e.g., toast) if auto-detection changes the mode unexpectedly.
4. Conduct a 10-user usability test: track manual toggle frequency vs. auto-switches, time-to-adjust, and user feedback.
5. Iterate based on test results—adjust toggle visibility, indicator timing, or auto-detection thresholds.
6. Document findings in a short report (e.g., GitHub issue) for future reference.

**What changed:**
Switched from a single dark theme with toggle to auto-detection + persistent toggle + session-based memory, validated by user testing.
