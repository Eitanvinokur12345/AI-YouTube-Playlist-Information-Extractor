# visualization: Own the VISUAL PRESENTATION of the interface — visibility, liveliness, clarity, enjoyment 

> Decision artifact · room `dept-visualization-own-the-visual-219` (dept) · 2026-07-10T17:46:56.000693+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Use *contextual micro-highlights* (e.g., a 100ms color flash on the relevant element) for state changes—minimal, task-focused, and only when needed—balancing liveliness with readability.

**Plan:**
1. Replace all smooth fades/pulses with 100ms color flashes (e.g., saturation bump) triggered only by user-initiated actions or critical updates.
2. Ensure flashes are confined to the affected element (no global shifts) and avoid overlapping with text-heavy areas.
3. Add a 1-frame delay (≈16ms) before flash onset to prevent accidental triggers during rapid interactions.
4. Limit flashes to 1–2 per interaction cycle to avoid visual noise; suppress if the same element updates within 500ms.
5. Document flash colors in the design system (e.g., `#007AFF` for success, `#FF3B30` for errors) with fixed opacity (80%).
6. Test with users to confirm flashes are noticeable but not disruptive in dense UIs (e.g., dashboards with tables).

**What changed:** Replaced persistent animations/indicators with *contextual micro-highlights* for minimal distraction and maximal clarity.
