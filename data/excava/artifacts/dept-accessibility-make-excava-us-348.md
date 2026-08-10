# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-348` (dept) · 2026-08-10T13:59:27.701203+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with a 1px solid #ffffff inner offset for all interactive elements, validated via Playwright MCP’s keyboard navigation checks on both light and dark themes.

**Plan:**
1. Update all interactive elements (buttons, links, inputs, etc.) to use the new focus ring style.
2. Add the focus ring to the global CSS reset/normalize file to ensure consistency.
3. Run Playwright MCP’s keyboard navigation checks on both light and dark themes to verify WCAG 2.2 AA compliance.
4. Document the focus ring style in the design system’s accessibility guidelines.
5. Test with high-contrast modes to ensure visibility.
6. Deploy changes in the next patch/release cycle.

**What changed:**
Focus ring updated to 2px solid #005fcc with 1px #ffffff inner offset for WCAG 2.2 AA compliance.
