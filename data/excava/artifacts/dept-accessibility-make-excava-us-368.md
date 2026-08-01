# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-368` (dept) · 2026-07-31T22:03:53.213480+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Use a 4px #005fcc focus ring with a 2px solid white inner stroke on all focusable elements—no blur.

**Plan:**
1. Implement CSS rule for focus states: `outline: 4px solid #005fcc; outline-offset: 0; outline-style: solid;` with `box-shadow: inset 0 0 0 2px #fff;`
2. Apply to all interactive elements (buttons, links, form controls, focusable containers).
3. Test on dark/patterned backgrounds to ensure 4.5:1 contrast ratio against both rings.
4. Verify keyboard navigation flow and touch target clarity.
5. Document the focus style in the design system’s accessibility guidelines.
6. Add automated tests to catch regressions in focus visibility.

**What changed:** Focus ring now uses a 4px #005fcc outer ring with a 2px solid white inner stroke (no blur) for consistent visibility.
