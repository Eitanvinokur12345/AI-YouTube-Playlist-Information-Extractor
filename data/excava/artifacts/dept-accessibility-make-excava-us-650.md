# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-650` (dept) · 2026-07-30T19:31:33.394359+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Ship a **3px outset focus ring, 4.5:1 contrast, 2px spacing**—verify on patterned backgrounds. Owner: accessibility-w1.

**Plan:**
1. Implement a 3px solid focus ring with 4.5:1 contrast on all interactive elements.
2. Apply a 2px offset from the element’s edge to ensure visibility.
3. Test focus ring visibility on high-contrast patterned backgrounds (e.g., gradients, photos).
4. Add focus ring styles to the design system’s global CSS variables.
5. Audit keyboard navigation paths to confirm ring visibility in all states (hover, focus, active).
6. Document the focus ring specs in the accessibility guidelines for future updates.

**What changed:** Focus ring upgraded from 2px/3:1 to 3px/4.5:1 contrast with 2px spacing.
