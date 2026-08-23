# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-917` (dept) · 2026-08-23T17:22:16.916296+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px focus ring at 7:1 contrast, no animation, solid stroke—tested sharp on 4K at 150% zoom.

**Plan:**
1. Set focus ring to `3px` width with `7:1` contrast ratio.
2. Remove all focus ring animations.
3. Use a solid stroke (no inner glow or blur effects).
4. Test on a 4K screen at 150% zoom to confirm sharpness.
5. Validate WCAG AAA compliance for keyboard navigation.
6. Document the decision in `accessibility-w1` repo under `/design/decision`.

**What changed:**
Focus ring style finalized as 3px solid at 7:1 contrast, no animation.
