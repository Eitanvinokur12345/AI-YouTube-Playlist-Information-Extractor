# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-893` (dept) · 2026-08-05T17:36:02.666624+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 4px outer ring in #005fcc with a 2px white inner ring and a 1px black outer border for focus indicators.

**Plan:**
1. Document the focus style in EXCAVA’s style guide with exact specifications (colors, dimensions, and use cases).
2. Implement the focus style in EXCAVA’s component library (e.g., buttons, inputs, links) with Playwright-compatible selectors.
3. Test focus visibility on dark, light, and patterned backgrounds using Playwright MCP (screenshots + contrast checks).
4. Add fallback styles for high-DPI screens to ensure ring clarity.
5. Verify WCAG 2.1 AA contrast ratios for all focus states.
6. Merge changes into the main branch and notify the team via PR.

**What changed:**
Focus indicator now uses a 4px #005fcc outer ring, 2px white inner ring, and 1px black outer border for guaranteed visibility across all backgrounds.
