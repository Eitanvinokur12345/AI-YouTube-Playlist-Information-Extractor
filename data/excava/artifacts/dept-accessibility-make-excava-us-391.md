# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-391` (dept) · 2026-08-09T22:24:28.075696+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with a 1px solid #ffffff inner offset at 100% opacity for all interactive elements.

**Plan:**
1. Update all interactive elements’ focus styles to use `2px solid #005fcc` with `1px solid #ffffff` inner offset.
2. Ensure the focus ring renders at 100% opacity across all screen densities and lighting conditions.
3. Test focus visibility in high-DPI screens, bright light, and for colorblind users.
4. Verify no collision with adjacent elements in dense UIs.
5. Document the new focus style in the design system’s accessibility guidelines.
6. Implement and deploy via the accessibility-w1 branch.

**What changed:**
Focus ring updated to 2px #005fcc with 1px #ffffff offset at 100% opacity.
