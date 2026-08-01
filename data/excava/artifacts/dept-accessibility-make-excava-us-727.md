# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-727` (dept) · 2026-07-31T18:30:06.569536+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 2px solid #005FCC focus ring with a 2px outer glow at 30% opacity, validated on the smallest interactive element at 120% zoom.

**Plan:**
1. Implement `outline: 2px solid #005FCC` for all focusable elements.
2. Add `box-shadow: 0 0 0 2px rgba(0, 95, 204, 0.3)` for the outer glow.
3. Test contrast compliance (4.5:1) on light, dark, and patterned backgrounds.
4. Validate visibility on mobile touch targets ≥32px and at 120% zoom.
5. Document CSS rule in `accessibility-w1` repo with test report.
6. Include fallback for browsers with limited `box-shadow` support.

**What changed:**
Focus ring updated to 2px solid + 2px glow at 30% opacity for WCAG compliance and visibility.
