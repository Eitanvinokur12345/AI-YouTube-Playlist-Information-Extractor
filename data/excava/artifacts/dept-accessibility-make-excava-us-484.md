# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-484` (dept) · 2026-08-28T13:14:11.489552+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white).

**Plan:**
1. Set focus ring to 3px width with 7:1 contrast ratio.
2. Add 1px white outer glow to enhance visibility on high-DPI mobile screens.
3. Test on real high-DPI mobile devices to confirm visibility.
4. Validate WCAG 2.2 AA compliance for low-vision and mobile users.
5. Document the decision and rationale in the project’s accessibility guidelines.
6. Implement the change in the next EXCAVA release.

**What changed:** Focus ring adjusted to 3px at 7:1 contrast with outer glow for universal visibility.
