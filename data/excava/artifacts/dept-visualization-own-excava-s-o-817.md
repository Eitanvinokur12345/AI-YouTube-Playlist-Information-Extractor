# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-817` (dept) · 2026-08-21T03:32:07.106656+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Auto-switch to a high-contrast light theme only when validation warnings appear, then revert to dark mode—no toggle, no user action required.

**Plan:**
1. Set dark theme as the default interface mode.
2. Detect validation warnings via Excava’s error-handling system.
3. Auto-switch to a high-contrast light theme *only* when warnings are present.
4. Revert to dark mode immediately after warnings are resolved or dismissed.
5. Ensure the transition is instantaneous to maintain "speed of our screen."
6. Test edge cases (e.g., rapid warnings, multiple errors) to confirm visibility.

**What changed:** Errors are now always visible without user intervention or interface clutter.
