# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-435` (dept) · 2026-08-13T16:50:23.654171+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 3px solid #005fcc focus ring with a 1px inner #fff at 100% opacity.

**Plan:**
1. Implement the 3px #005fcc focus ring with 1px inner #fff at 100% opacity.
2. Run Playwright MCP’s accessibility scan to verify WCAG 2.2 3:1 contrast compliance.
3. Test across light/dark themes and high-contrast modes for visual clarity.
4. Audit keyboard navigation to ensure focus indicators remain distinct.
5. Document the decision in the design system’s accessibility guidelines.
6. Schedule a follow-up review after 2 weeks of real-world usage.

**What changed:**
Focus ring updated to 3px #005fcc with 1px inner #fff at 100% opacity for WCAG compliance.
