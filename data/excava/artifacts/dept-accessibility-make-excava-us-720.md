# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-720` (dept) · 2026-08-21T06:51:47.159762+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Set focus ring to **3px wide** with **6:1 contrast** and **1px outer stroke**, no glow.
2. Implement **100ms fade-in** from 0% to 100% opacity.
3. Add to EXCAVA’s stylesheet under `accessibility-w1` class.
4. Test with screen reader users for low vision and vestibular sensitivity.
5. Validate WCAG AAA compliance for reduced motion and large text.
6. Document trade-offs (e.g., visibility on high-contrast backgrounds) in repo notes.

**What changed:** Focus ring width increased from 2px/6px to 3px with 100ms fade-in at 6:1 contrast.
