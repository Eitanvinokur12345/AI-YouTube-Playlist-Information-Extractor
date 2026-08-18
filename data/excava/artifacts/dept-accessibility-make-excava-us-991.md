# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-991` (dept) · 2026-08-18T20:53:47.151546+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 2px dashed #005fcc focus ring at 4.5:1 contrast with no glow or animation.

**Plan:**
1. Implement a 2px dashed focus ring with #005fcc at 4.5:1 contrast ratio.
2. Remove all glow/animation effects to comply with reduced-motion requirements.
3. Test visibility in dark mode, high-contrast mode, and on touch screens.
4. Ensure the ring remains visible on patterned and dark backgrounds without relying on color alone.
5. Document the decision in the accessibility-w1 repository.
6. Validate compliance with WCAG 2.2 AA for keyboard navigation.

**What changed:** Focus ring updated to 2px dashed, 4.5:1 contrast, no glow.
