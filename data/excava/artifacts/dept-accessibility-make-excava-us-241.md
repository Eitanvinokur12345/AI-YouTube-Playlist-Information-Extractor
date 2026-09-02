# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-241` (dept) · 2026-09-02T17:37:24.008158+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 3px focus ring at 4.5:1 contrast by default, with a 2px ring at 3:1 in forced-colors mode.

**Plan:**
1. Implement default focus styles: `3px solid currentColor` with `4.5:1` contrast.
2. Add forced-colors mode override: `2px solid currentColor` with `3:1` contrast.
3. Test focus visibility in reduced-motion, high-contrast, and forced-colors modes.
4. Validate WCAG 2.2 AA compliance for all interactive elements.
5. Document focus styles in the design system for frontend team reference.
6. Deploy changes with fallback support for older browsers.

**What changed:** Focus ring thickness and contrast adjusted for forced-colors mode.
