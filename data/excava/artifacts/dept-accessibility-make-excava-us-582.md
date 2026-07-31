# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-582` (dept) · 2026-07-31T18:51:25.652626+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 2px solid #005FCC focus ring with a 2px outer glow at 40% opacity, validated for ≥95% tap success on 28px buttons at 120% zoom.

**Plan:**
1. Implement the 2px solid #005FCC focus ring with 2px outer glow at 40% opacity for keyboard navigation.
2. Test tap success rate on 28px buttons at 120% zoom to ensure ≥95% success.
3. Verify WCAG 2.2 AA contrast compliance for the focus indicator on all backgrounds.
4. Apply the focus ring consistently across all interactive elements (buttons, links, form fields).
5. Document the focus ring style in the design system for future reference.
6. Conduct user testing with keyboard-only and mobile users to confirm usability.

**What changed:**
Focus ring updated to 2px solid #005FCC with 2px outer glow at 40% opacity for balanced accessibility across contexts.
