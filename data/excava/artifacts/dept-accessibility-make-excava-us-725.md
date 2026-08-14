# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-725` (dept) · 2026-08-14T08:00:10.096050+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 2.5px solid #005fcc focus ring with 1.5px inner #fff at 85% opacity.

**Plan:**
1. Document the focus ring style in EXCAVA’s design system with contrast ratios verified (WCAG 2.1 AA) on light/dark backgrounds and high-DPI screens.
2. Implement the ring in all interactive components (buttons, links, form fields) with CSS variables for consistency.
3. Test keyboard navigation across browsers/devices to ensure visibility and no clipping.
4. Add reduced-motion support (e.g., `prefers-reduced-motion`) to disable animations for the focus ring.
5. Create a Figma/Storybook component for the focus ring with usage guidelines.
6. Assign Ramp as owner for maintenance and updates.

**What changed:** Focus ring thickness adjusted to 2.5px with 1.5px inner white at 85% opacity.
