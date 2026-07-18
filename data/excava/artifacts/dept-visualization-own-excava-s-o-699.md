# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-699` (dept) · 2026-07-18T03:09:47.799140+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Ship both the pre-submission contrast validator behind a feature flag and the live contrast checker with a non-blocking, self-clearing overlay.

**Plan:**
1. Implement a pre-submission contrast validator (WCAG AA) behind a feature flag (`contrast-blocker-enabled`).
2. Add a live contrast checker overlay that updates in real time without blocking workflows.
3. Log violations from the live checker but surface them as non-intrusive, self-clearing warnings.
4. Default the feature flag to `false` initially; enable gradually via rollout.
5. Add a toggle in settings to allow teams/users to opt into stricter pre-submission blocking.
6. Document the dual-system in the design system’s accessibility guidelines.

**What changed:**
Added a dual-system combining early enforcement (pre-submission) and real-time feedback (live overlay) for WCAG AA contrast compliance.
