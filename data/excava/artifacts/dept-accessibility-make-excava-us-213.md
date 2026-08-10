# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-213` (dept) · 2026-08-10T21:00:46.438824+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring at 90% opacity with a 1px inner #ffffff.

**Plan:**
1. Implement the 3px #005fcc focus ring at 90% opacity with a 1px inner #ffffff across all interactive elements.
2. Validate WCAG 2.2 3:1 contrast on both light and dark backgrounds for keyboard navigation.
3. Ensure the focus ring fits within 48px touch targets without visual clutter.
4. Test the focus ring at 125% zoom to confirm clarity and usability.
5. Document the decision in the design system’s focus ring guidelines.
6. Assign Ramp as the owner for implementation and maintenance.

**What changed:**
Focus ring adjusted to 3px at 90% opacity (was 4px/80% or 2px/100%) to balance visibility, accessibility, and density.
