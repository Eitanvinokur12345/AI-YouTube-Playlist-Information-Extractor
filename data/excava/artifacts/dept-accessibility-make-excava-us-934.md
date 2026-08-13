# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-934` (dept) · 2026-08-13T17:32:08.322585+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with a 1px inner #fff cutout at 50% opacity.

**Plan:**
1. Implement CSS for the 2px #005fcc focus ring with 1px inner #fff at 50% opacity.
2. Ensure live contrast checks (minimum 3:1 on light surfaces, 4.5:1 on dark).
3. Test focus visibility in both light/dark modes and high-contrast screens.
4. Validate touch target clarity on mobile without compromising desktop focus distinction.
5. Document the decision and CSS snippet in the project’s accessibility guidelines.
6. Assign Ramp as owner for implementation and future adjustments.

**What changed:**
Focus ring updated to 2px #005fcc with 1px inner #fff at 50% opacity for balanced visibility and WCAG compliance.
