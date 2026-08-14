# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-705` (dept) · 2026-08-14T13:56:36.319983+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with 1px inner #fff at 95% opacity for ≥4.5:1 contrast on light backgrounds.

**Plan:**
1. Implement the CSS rule for the focus ring: `outline: 2px solid #005fcc; outline-offset: 2px; box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.95);`
2. Conduct live contrast tests on 10 light backgrounds to verify ≥4.5:1 contrast.
3. Ensure the design remains crisp on high-DPI screens by testing at 2x and 3x scaling.
4. Document the focus ring specs in the design system’s accessibility guidelines.
5. Share the final CSS rule and test results with the team by EOD.

**What changed:**
Focus ring updated to 2px #005fcc with 1px #fff inner at 95% opacity for improved contrast and clarity.
