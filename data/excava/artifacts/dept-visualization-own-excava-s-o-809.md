# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-809` (dept) · 2026-07-20T17:32:16.846384+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:** Ship a real-time contrast overlay that flashes red on violations *as you work*—no pre-submit gate, no live checker.

**Plan:**
1. Build a live contrast overlay that renders violations as red flashes in the design preview.
2. Integrate the overlay into the core rendering pipeline to ensure zero delay in feedback.
3. Add a toggle to disable the overlay for edge cases (e.g., prototyping grayscale).
4. Document the overlay’s behavior in the design system’s contribution guide.
5. Monitor adoption metrics (e.g., violation frequency) for 2 weeks post-launch.
6. Iterate on the overlay’s visual design (e.g., flash intensity, persistence) based on user feedback.

**What changed:** Replaced pre-submit gates and background checkers with an in-workspace contrast overlay.
