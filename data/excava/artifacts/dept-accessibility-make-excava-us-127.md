# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-127` (dept) · 2026-08-15T06:21:25.353711+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with 2px #fff inset at 80% opacity.

**Plan:**
1. Update all interactive components in EXCAVA to use the 2px #005fcc focus ring with 2px #fff inset at 80% opacity.
2. Test the focus ring on both light and dark backgrounds to ensure visibility and clarity.
3. Verify WCAG compliance for contrast and focus visibility at 100% and 400% zoom levels.
4. Document the focus ring style in the design system for consistency across the project.
5. Implement the focus ring style in the component library and update existing components accordingly.
6. Conduct a QA review to confirm the focus ring meets accessibility requirements without visual clutter.

**What changed:**
Focus ring style updated to 2px #005fcc with 2px #fff inset at 80% opacity.
