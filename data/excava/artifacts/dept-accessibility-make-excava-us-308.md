# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-308` (dept) · 2026-08-09T11:04:54.380867+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring with a 1px #ffffff outer ring to meet WCAG 2.2 contrast on patterned backgrounds while balancing visual prominence.

**Plan:**
1. Implement the 3px #005fcc solid focus ring with a 1px #ffffff outer ring in EXCAVA’s focus styles.
2. Test visibility against high-contrast checkerboard patterns at 200% zoom.
3. Validate 3:1 contrast ratio against both light and dark patterned surfaces.
4. Ensure the ring remains visible without relying on inner/outer gaps.
5. Document the decision in the design system’s accessibility guidelines.
6. Assign Ramp to finalize implementation and conduct cross-browser testing.

**What changed:**
Added a 1px #ffffff outer ring to the 3px #005fcc focus ring for improved visibility on patterned backgrounds.
