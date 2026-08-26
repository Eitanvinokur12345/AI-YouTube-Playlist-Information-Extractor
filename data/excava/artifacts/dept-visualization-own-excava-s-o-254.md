# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-254` (dept) · 2026-08-26T09:25:22.610906+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Make the legend a sticky sidebar that condenses to a thin strip when zoomed.

**Plan:**
1. Implement a sticky left-aligned sidebar for the legend that remains visible at all times.
2. Add a responsive condensation feature: when users zoom into dense data, the sidebar shrinks to a thin vertical strip (e.g., 30px wide) with collapsed labels/icons.
3. Ensure the condensed strip expands to full width on hover or click, revealing the full legend.
4. Test label overlap in dense views and adjust condensation behavior (e.g., auto-collapse on zoom, manual expand).
5. Optimize spacing to prevent crowding while maintaining readability in both states.
6. Validate with user tests to confirm the condensed mode is discoverable and non-intrusive.

**What changed:**
Legend shifts from floating/collapsible to a sticky sidebar that condenses dynamically during zoom.
