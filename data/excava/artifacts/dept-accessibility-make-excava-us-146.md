# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-146` (dept) · 2026-08-17T03:29:55.789330+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2.5px solid #005fcc focus ring with 15% opacity glow at 2px spread for EXCAVA.

**Plan:**
1. Implement the 2.5px solid #005fcc focus ring with 15% opacity glow at 2px spread in EXCAVA’s CSS.
2. Test focus visibility on patterned backgrounds, high-contrast modes, and at 200% zoom.
3. Validate keyboard navigation across touch and mobile devices for clarity.
4. Ensure reduced-motion compatibility (glow should not trigger animations).
5. Document the focus style in EXCAVA’s accessibility guidelines.
6. Review feedback after 2 weeks of deployment and adjust if needed.

**What changed:**
Focus ring updated from 2px/3px solid to 2.5px solid with subtle glow for balanced accessibility.
