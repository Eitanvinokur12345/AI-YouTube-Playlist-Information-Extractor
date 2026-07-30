# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-842` (dept) · 2026-07-30T23:37:32.466139+00:00
> Participants: Lumen, Facet, Pane · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with a one-time theme picker at first launch, defaulting to system preference but allowing override—no persistent toggle.

**Plan:**
1. Implement a one-time theme picker at first launch with three options: "System," "Light," and "Dark."
2. Default selection to the system theme (light/dark) if detectable; otherwise, default to "Dark."
3. Store the user’s choice in local storage (e.g., `localStorage`) and apply it immediately.
4. Skip the picker for subsequent launches; retain the stored theme.
5. Exclude a persistent UI toggle to reduce recurring friction.
6. Document the behavior in onboarding and settings (e.g., "Theme set at first launch").

**What changed:**
Added a one-time theme picker with system-default fallback, removing persistent toggle complexity.
