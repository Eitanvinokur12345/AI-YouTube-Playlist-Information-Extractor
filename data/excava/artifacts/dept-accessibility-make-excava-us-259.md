# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-259` (dept) · 2026-07-30T19:10:05.676126+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship **3px outset focus ring, 4.5:1 contrast, 2px spacing**—verify touch/mobile visibility and keyboard nav. Owner: Ramp.

**Plan:**
1. Implement a 3px-wide focus ring with 4.5:1 contrast and 2px offset on all interactive elements.
2. Test visibility on high-contrast image backgrounds and mobile screens with glare.
3. Validate keyboard navigation flow across all components.
4. Audit touch targets for mobile usability (minimum 48x48px).
5. Ensure reduced-motion support (no flashing focus indicators).
6. Document focus ring styles in the design system.

**What changed:** Focus ring upgraded to 3px outset, 4.5:1 contrast, 2px spacing.
