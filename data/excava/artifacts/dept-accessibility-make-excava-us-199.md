# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-199` (dept) · 2026-08-15T06:38:00.052599+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 4px solid #005fcc focus ring with a 1px #fff outer stroke at 100% opacity.

**Plan:**
1. Update focus ring styles in `global.css` to use `4px solid #005fcc` with `1px solid #fff` outer stroke.
2. Ensure the focus ring meets WCAG 2.2 AA contrast on both light and dark backgrounds.
3. Test focus visibility on small touch targets (e.g., buttons, links) for clarity.
4. Verify keyboard navigation works with the new focus ring across all components.
5. Document the change in the accessibility guidelines for future reference.
6. Deploy changes and monitor user feedback for any visual issues.

**What changed:** Focus ring updated to 4px solid #005fcc with 1px #fff outer stroke for WCAG 2.2 AA compliance.
