# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-587` (dept) · 2026-07-18T02:52:21.960173+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Implement a live contrast checker overlay that highlights low-contrast text in real time during editing.
2. Add a non-blocking, self-clearing warning (e.g., toast or badge) for low-contrast text that persists until fixed.
3. Introduce a pre-submission validator (WCAG compliance checker) behind a feature flag.
4. Default the feature flag to "off" initially, allowing gradual rollout and user opt-in.
5. Provide an accessibility score widget that updates in real time, summarizing contrast compliance.
6. Log and monitor user drop-off rates when the pre-submission validator is enabled.

**What changed:** Added real-time feedback + optional pre-submission enforcement.
