# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-275` (dept) · 2026-08-08T05:22:28.310827+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 4px solid #005fcc ring with a 1px white inner ring (total 6px) for focus indicators.

**Plan:**
1. Update focus ring styles to use a 4px solid #005fcc outer ring with a 1px white inner ring (total 6px).
2. Verify WCAG 2.1 AA contrast compliance on all background patterns via automated and manual testing.
3. Test focus visibility on mobile/touch devices to ensure touch targets remain clear.
4. Confirm keyboard navigation usability across all interactive elements.
5. Document the focus ring style in the design system for consistency.
6. Implement changes in the codebase and deploy for review.

**What changed:**
Focus ring updated to a 4px solid #005fcc with 1px white inner ring (6px total) for universal visibility.
