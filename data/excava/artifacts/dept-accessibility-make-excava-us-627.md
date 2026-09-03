# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-627` (dept) · 2026-09-03T03:44:19.937674+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px focus ring at 6:1 contrast with a 1px inner glow at 10% opacity.

**Plan:**
1. Implement the 3px focus ring at 6:1 contrast in EXCAVA’s design system.
2. Add a 1px inner glow at 10% opacity to ensure visibility on patterned/high-contrast backgrounds.
3. Test keyboard navigation across all backgrounds (solid, patterned, high-contrast).
4. Verify reduced-motion compatibility (glow opacity respects `prefers-reduced-motion`).
5. Document the component in the design system with usage guidelines.
6. Assign ownership to `accessibility-w1` for maintenance and updates.

**What changed:**
Focus ring updated from 4px/7:1 to 3px/6:1 with 1px/10% inner glow.
