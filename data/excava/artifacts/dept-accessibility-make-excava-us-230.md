# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-230` (dept) · 2026-09-03T03:08:15.787509+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px focus ring at 4.5:1 contrast with no glow.

**Plan:**
1. Implement a 3px focus ring with 4.5:1 contrast ratio.
2. Remove glow effect entirely.
3. Test on 100px checkerboard at 50% gray and 20% gray for visibility.
4. Validate keyboard navigation visibility in both light and dark modes.
5. Document the focus ring specs in the design system.
6. Add the focus ring artifact to the shared component library.

**What changed:**
Focus ring increased from 2px to 3px with 4.5:1 contrast and glow removed.
