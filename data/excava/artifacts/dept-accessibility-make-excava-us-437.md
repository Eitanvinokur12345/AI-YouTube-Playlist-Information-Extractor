# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-437` (dept) · 2026-08-01T19:46:35.354411+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 4px #005fcc outer ring with 2px white inner ring as the default focus indicator.

**Plan:**
1. Implement the 4px #005fcc outer ring with 2px white inner ring for all interactive elements.
2. Test focus visibility on patterned/textured backgrounds at 100% zoom to ensure WCAG 2.1 AA compliance (4.5:1 contrast).
3. Validate contrast ratios in high-contrast modes to confirm no blending occurs.
4. Document the focus ring style in the design system for consistency.
5. Assign owner `a` to enforce implementation and resolve edge cases.

**What changed:** Default focus ring updated to 4px #005fcc outer + 2px white inner ring.
