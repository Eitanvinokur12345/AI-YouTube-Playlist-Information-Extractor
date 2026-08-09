# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-653` (dept) · 2026-08-09T09:14:00.876015+00:00
> Participants: Facet, Pane, Lumen · synthesized by mistral/mistral-small-latest

**Decision:**
Default to system preference at first launch, then remember the last choice—but force a one-time explicit theme choice with a clear visual cue.

**Plan:**
1. On first launch, detect system preference (light/dark) and apply it by default.
2. Display a one-time modal or banner prompting the user to confirm their theme choice, with a faint border visual cue indicating the current mode.
3. Store the user’s selection in local storage (or equivalent) for all future sessions.
4. Provide a persistent one-click toggle in the interface to switch themes at any time.
5. Ensure the visual cue (e.g., faint border) remains visible to indicate the active theme.
6. Test contrast and readability in both modes to ensure critical data is always visible.

**What changed:**
Added a one-time explicit theme choice with a visual cue to system-preference defaulting.
