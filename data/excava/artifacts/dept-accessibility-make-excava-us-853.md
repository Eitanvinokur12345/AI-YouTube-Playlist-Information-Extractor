# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-853` (dept) · 2026-08-01T14:08:41.864687+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 4px solid #005fcc focus ring with a 1px solid white inner ring for interactive elements.

**Plan:**
1. Implement the 4px #005fcc outer ring with 1px white inner ring in EXCAVA’s CSS.
2. Test visibility at 200% zoom on light gray and patterned backgrounds.
3. Validate keyboard navigation and contrast compliance with Playwright.
4. Ensure the focus ring remains visible across light/dark themes.
5. Document the focus ring style in EXCAVA’s accessibility guidelines.
6. Merge changes via `accessibility-w1` with peer review.

**What changed:**
Focus ring updated to 4px #005fcc with 1px white inner ring.
