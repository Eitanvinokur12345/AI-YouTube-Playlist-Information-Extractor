# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-957` (dept) · 2026-09-03T19:06:50.675560+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 2px focus ring at 4.5:1 contrast with a 1px outer glow at 3:1 contrast on interactive elements.

**Plan:**
1. Apply the 2px focus ring (4.5:1 contrast) to all interactive elements.
2. Add a 1px outer glow (3:1 contrast) to enhance visibility on patterned/mid-tone backgrounds.
3. Test with a 10-person keyboard user group on live EXCAVA pages to validate focus tracking.
4. Ensure the focus indicator meets WCAG 2.2 AA requirements for visibility.
5. Document the focus ring specifications in the design system for consistency.
6. Monitor user feedback and adjust glow thickness/contrast if issues arise.

**What changed:**
Focus indicator now uses a 2px ring + 1px glow (4.5:1 + 3:1 contrast) instead of a 3px ring at 7:1 contrast.
