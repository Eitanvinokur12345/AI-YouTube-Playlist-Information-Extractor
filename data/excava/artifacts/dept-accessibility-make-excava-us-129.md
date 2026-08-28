# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-129` (dept) · 2026-08-28T12:08:37.169816+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white) for EXCAVA.

**Plan:**
1. Document the 3px focus ring (7:1 contrast) with 1px white outer glow in EXCAVA’s design system.
2. Test focus visibility in monochrome, grayscale inversion, checkerboard backgrounds, and reduced-motion modes.
3. Verify WCAG AA compliance (4.5:1 minimum) and AAA where possible (7:1 for ring).
4. Add code snippets/examples for implementation in EXCAVA’s component library.
5. Assign `accessibility-w1` as owner for maintenance and updates.
6. Schedule quarterly reviews to validate focus visibility across new themes/updates.

**What changed:** Focus ring now uses 3px width at 7:1 contrast with 1px outer glow for universal visibility.
