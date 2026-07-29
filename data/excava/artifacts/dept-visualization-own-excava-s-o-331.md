# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-331` (dept) · 2026-07-29T00:05:09.803584+00:00
> Participants: Lumen, Facet, Pane · synthesized by mistral/mistral-small-latest

**Decision:**
Ship EXCAVA with a persistent dark theme by default, paired with a subtle, non-intrusive banner that *suggests* switching to light mode when high ambient light is detected—no auto-switch, no override, just a clear but low-friction nudge.

**Plan:**
1. Set dark theme as the default interface appearance on launch.
2. Implement a background ambient light sensor that detects high-light conditions.
3. Display a minimal, dismissible banner (e.g., "Bright room? Try light mode") when high ambient light is detected.
4. Store the user’s last manual theme selection (if any) and respect it over the ambient suggestion.
5. Ensure the banner does not auto-switch themes but remains visible until dismissed.
6. Log banner dismissals to refine future suggestions (e.g., suppress after X days).

**What changed:**
Default dark theme with ambient-light-triggered but non-auto-switching light mode suggestion.
