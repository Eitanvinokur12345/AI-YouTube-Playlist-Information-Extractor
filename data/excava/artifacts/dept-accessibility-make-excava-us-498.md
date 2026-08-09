# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-498` (dept) · 2026-08-09T11:34:45.627875+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 2px solid #005fcc focus ring with a 1px outer glow (#005fcc, 0.5px blur) for keyboard navigation.

**Plan:**
1. Replace all existing focus ring implementations with the 2px solid #005fcc ring + 1px outer glow (#005fcc, 0.5px blur).
2. Test contrast ratios on patterned backgrounds to ensure WCAG 2.2 AA compliance.
3. Audit mobile/touch targets to confirm the focus ring does not feel visually heavy.
4. Update design system documentation with the new focus ring specifications.
5. Implement the change in the component library and verify across browsers/devices.
6. Conduct user testing with keyboard-only and screen reader users to validate usability.

**What changed:** Focus ring updated to 2px solid + 1px outer glow for balanced accessibility and visual clarity.
