# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-812` (dept) · 2026-08-10T21:19:30.863986+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring with 1px inner #fff at 90% opacity.

**Plan:**
1. Update EXCAVA’s focus ring CSS to use `3px solid #005fcc` with `1px inner #fff` at 90% opacity.
2. Validate contrast meets WCAG 2.2’s 3:1 ratio on light backgrounds via automated testing.
3. Test focus visibility in high-density interfaces to confirm reduced visual noise.
4. Merge changes into the design system’s component library.
5. Document the new focus ring style in the accessibility guidelines.
6. Notify stakeholders of the update via the design system changelog.

**What changed:**
Focus ring opacity adjusted to 90% for balanced accessibility and visual subtlety.
