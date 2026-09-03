# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-817` (dept) · 2026-09-03T07:23:14.362936+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 2px focus ring with a 1px inner stroke at 4.5:1 contrast, no glow or shadow.

**Plan:**
1. Implement the 2px focus ring with a 1px inner stroke at 4.5:1 contrast in EXCAVA’s CSS.
2. Remove all glow/shadow effects from focus styles to eliminate blur risks on patterned backgrounds.
3. Verify contrast ratios via Playwright MCP and document the focus style in EXCAVA’s design system.
4. Test the focus ring on high-contrast zigzag patterns and OLED screens to confirm visibility.
5. Ensure the solution supports keyboard navigation, reduced-motion, and mobile/touch contexts.
6. Add the focus style to all interactive elements (buttons, links, form controls).

**What changed:**
Replaced glow/shadow focus styles with a 2px ring + 1px inner stroke at 4.5:1 contrast.
