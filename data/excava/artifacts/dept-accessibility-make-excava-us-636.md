# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-636` (dept) · 2026-07-31T11:10:22.784317+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 1.5px solid focus ring with a 1px outer glow at 25% opacity, tested at 200% zoom.

**Plan:**
1. Update focus ring CSS to `1.5px solid` with `1px` outer glow at `25%` opacity.
2. Test at 125% and 200% zoom for visibility and no bleeding.
3. Validate contrast ratios against WCAG 2.2 SC 2.4.1 on patterned backgrounds.
4. Implement in design system tokens for consistency.
5. Document in accessibility guidelines for developers.
6. Conduct user testing with low-vision and keyboard users.

**What changed:**
Focus ring adjusted to 1.5px ring + 1px glow at 25% opacity, tested at 200% zoom.
