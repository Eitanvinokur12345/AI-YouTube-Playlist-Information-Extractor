# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-823` (dept) · 2026-08-09T23:02:44.386019+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with a 1px inner #ffffff offset for all interactive elements.

**Plan:**
1. Update focus ring styles globally to `2px solid #005fcc` with `1px inner #ffffff offset`.
2. Ensure all interactive elements (buttons, links, form controls) inherit the new focus ring.
3. Test contrast ratios on light/dark backgrounds to confirm WCAG 2.2 AA compliance (4.5:1 minimum).
4. Verify no collisions with adjacent elements in dense UIs (e.g., tables, grids).
5. Document the change in the design system’s focus indicator guidelines.
6. Deploy changes via the component library and update affected live components.

**What changed:**
Focus ring reduced to 2px solid #005fcc with 1px inner offset for WCAG 2.2 AA compliance.
