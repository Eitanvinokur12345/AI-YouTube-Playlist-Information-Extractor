# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-804` (dept) · 2026-08-18T07:23:22.431841+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring with a 100ms fade-in at 7:1 contrast, tested at 150% zoom and on high-DPI screens.

**Plan:**
1. Update focus ring styles to `3px solid #005fcc` with `100ms fade-in` animation.
2. Ensure focus ring meets 7:1 contrast ratio for all interactive elements.
3. Test at 150% zoom to confirm visibility on mobile/touch devices.
4. Validate on high-DPI screens to prevent visibility issues.
5. Document reduced-motion compliance (no abrupt animations).
6. Assign `accessibility-w1` as owner for implementation and delivery.

**What changed:**
Focus ring increased from 2px/4px to 3px with 100ms fade-in and 7:1 contrast.
