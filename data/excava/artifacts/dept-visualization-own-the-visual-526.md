# visualization: Own the VISUAL PRESENTATION of the interface — visibility, liveliness, clarity, enjoyment 

> Decision artifact · room `dept-visualization-own-the-visual-526` (dept) · 2026-07-10T23:32:32.822875+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Anchor the interface’s visual priority to a single, live-updated metric.

**Plan:**
1. Introduce a **team-selectable priority metric** (e.g., "daily active users" or "checkout conversion") via a dropdown or API call.
2. Apply a **vivid accent color (e.g., teal)** exclusively to the selected metric’s display (charts, cards, or headers).
3. Ensure the accent updates **instantly** when the team lead changes the priority, with a subtle transition (e.g., fade or pulse).
4. Keep all other data in neutral grays/whites to maintain contrast and avoid visual noise.
5. Log priority changes in a lightweight audit trail (e.g., timestamped entries) for transparency.
6. Test with teams to confirm the signal is **learned and trusted**, not ignored.

**What changed:** The accent color now reflects the team’s *current* top priority, not a fixed weekly goal.
