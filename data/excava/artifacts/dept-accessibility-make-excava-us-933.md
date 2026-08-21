# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-933` (dept) · 2026-08-21T01:15:09.345230+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 4px solid #005fcc focus ring at 8:1 contrast with no glow or animation.

**Plan:**
1. Implement the 4px solid focus ring (#005fcc, 8:1 contrast) globally in EXCAVA’s CSS.
2. Remove all focus ring animations and glow effects to comply with reduced-motion preferences.
3. Test visibility on patterned/dark backgrounds, high-contrast system themes, and at 200% zoom.
4. Validate with screen-reader users on production pages to confirm usability.
5. Document the focus ring style in EXCAVA’s design system for consistency.
6. Monitor feedback and adjust if issues arise during beta testing.

**What changed:**
Focus ring updated to 4px solid #005fcc at 8:1 contrast, no glow/animation.
