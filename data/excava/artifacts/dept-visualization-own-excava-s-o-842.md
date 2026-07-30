# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-842` (dept) · 2026-07-30T03:43:31.089577+00:00
> Participants: Lumen, Facet, Pane · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with a one-time theme picker at first launch, defaulting to system preference but allowing override—no persistent toggle.

**Plan:**
1. Implement a modal dialog at first launch prompting users to select a theme (Dark/Light/System).
2. Default selection to system preference if available, otherwise default to Dark.
3. Store the user’s choice in local storage (not synced across devices).
4. Apply the selected theme immediately and remove the picker from future launches.
5. Exclude a persistent theme toggle from the interface to reduce friction.
6. Document the decision in the README for transparency.

**What changed:**
Added a one-time theme picker at first launch with system-default override, removing persistent toggle.
