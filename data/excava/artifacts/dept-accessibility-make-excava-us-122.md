# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-122` (dept) · 2026-08-17T01:38:54.131450+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with a 2px inner glow at 30% opacity.

**Plan:**
1. Implement the 2px solid #005fcc focus ring with 2px inner glow at 30% opacity.
2. Test visibility on checkerboard backgrounds at 200% zoom.
3. Validate at 125% system zoom to ensure no overlap with adjacent touch targets.
4. Confirm keyboard navigation clarity across patterned backgrounds.
5. Document the focus ring style in the design system for consistency.
6. Conduct user testing with keyboard-dependent participants for feedback.

**What changed:**
Focus ring updated from 3px solid with inner shadow to 2px solid with 2px inner glow at 30% opacity.
