# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-878` (dept) · 2026-09-03T20:10:26.998119+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use a collapsible top strip—shrinking to a 1-line banner when idle, expanding to full height on hover or alert—for unobstructed visualization clarity and instant navigation.

**Plan:**
1. Prototype both fixed-height and collapsible top strips in a live demo with identical datasets.
2. Test alert visibility in dark theme—ensure critical alerts "scream" when expanded (e.g., red glow, bold text).
3. Implement auto-hide for non-alert navigation, triggered by scroll or idle timeout.
4. Add smooth CSS transitions (150ms) for strip expansion/collapse to avoid jarring UX.
5. Validate with 5 users: measure time-to-alert detection and data clarity (label visibility).
6. Freeze design after passing 90% user comprehension in tests.

**What changed:**
Replaced fixed-height top bar with a collapsible strip to preserve vertical space while ensuring alert visibility.
