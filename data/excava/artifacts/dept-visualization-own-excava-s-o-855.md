# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-855` (dept) · 2026-09-01T04:13:03.554149+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Use a thin, collapsible top banner (4% height) for critical alerts that pulses when urgent, paired with a persistent left sidebar for navigation and context—balancing visibility and space.

**Plan:**
1. Implement a top banner (4% of screen height) for critical alerts that auto-collapses after 5 seconds unless interacted with.
2. Add a pulse animation to the banner when alerts are urgent (e.g., red flash for errors, yellow for warnings).
3. Design a persistent left sidebar (20% width) for primary navigation, filters, and contextual data.
4. Ensure the sidebar remains visible across all screens but allows dynamic resizing.
5. Test vertical space allocation to confirm data density isn’t compromised.
6. Add a toggle in user settings to expand/collapse the top banner manually.

**What changed:**
Top banner (4%) + collapsible left sidebar (20%) replaces full-height sidebar and static banner.
