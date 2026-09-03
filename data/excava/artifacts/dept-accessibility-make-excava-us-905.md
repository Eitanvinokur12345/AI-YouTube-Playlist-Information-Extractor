# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-905` (dept) · 2026-09-03T04:01:23.832130+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a user-toggleable focus ring system with two modes: solid 4px at 7:1 contrast for clean backgrounds, and 2px with 20% inner glow at 4.5:1 contrast for patterned/high-glare surfaces.

**Plan:**
1. Implement a persistent toggle in settings (e.g., "Focus visibility mode") with two options: "Solid high-contrast" and "Glow for complex backgrounds."
2. Default to "Solid high-contrast" (4px, 7:1) for all users.
3. Apply the 2px glow ring (4.5:1) when "Glow for complex backgrounds" is selected.
4. Test both modes on real patterned backgrounds (e.g., grids, gradients, busy textures) to ensure visibility.
5. Log toggle usage to gather data on user preference and edge cases.
6. Document the toggle in accessibility settings with clear labels (e.g., "Improves focus visibility on busy backgrounds").

**What changed:**
Added user-toggleable focus ring modes (solid 4px/7:1 and glow 2px/4.5:1) to address visibility on patterned/high-glare backgrounds.
