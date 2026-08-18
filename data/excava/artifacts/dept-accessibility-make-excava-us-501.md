# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-501` (dept) · 2026-08-18T02:01:21.296150+00:00
> Participants: Access, Ramp, Reader · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc ring with a 2px solid inner shadow at 4.5:1 contrast for EXCAVA’s focus indicator.

**Plan:**
1. Implement the 2px solid ring with 2px inner shadow at 4.5:1 contrast as the default focus style.
2. Ensure the inner shadow is static (no motion) to comply with reduced-motion preferences.
3. Test the focus ring with screen readers on both mobile and desktop.
4. Validate touch target clarity on mobile devices.
5. Confirm the ring remains visible against patterned backgrounds.
6. Document the focus ring component for reuse in EXCAVA.

**What changed:** Switched from dynamic glow to static inner shadow for reduced-motion compliance while maintaining high contrast.
