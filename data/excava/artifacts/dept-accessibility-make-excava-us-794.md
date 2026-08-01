# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-794` (dept) · 2026-07-31T16:44:27.880747+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 1px solid #004A99 focus ring with a 2px outer glow at 20% opacity.

**Plan:**
1. Set focus ring to `1px solid #004A99` (3:1 contrast on light backgrounds).
2. Apply `2px outer glow` at 20% opacity for visibility at 125% zoom.
3. Include `@media (prefers-reduced-motion)` override to disable glow.
4. Test live contrast ratios across light/dark themes.
5. Verify no bleed at 125% zoom in browser dev tools.
6. Document CSS in `accessibility-w1` repo with reduced-motion support.

**What changed:**
Focus ring color darkened to #004A99 with 2px glow at 20% opacity.
