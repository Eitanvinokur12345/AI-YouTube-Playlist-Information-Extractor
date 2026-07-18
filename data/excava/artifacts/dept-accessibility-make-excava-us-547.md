# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-547` (dept) · 2026-07-18T21:26:44.314217+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a persistent, subtle skip link component.

**Plan:**
1. Create a skip link component with default styles: 1px by 1px underline, positioned off-screen (e.g., `top: -40px`).
2. On keyboard focus, animate the skip link to expand to 2px underline and move to `top: 0` (visible but minimal).
3. Ensure the skip link jumps to the main content container (`#main-content`) with one keystroke.
4. Write Playwright MCP tests to verify:
   - Skip link is visible by default (even if subtle).
   - Skip link expands on keyboard focus.
   - Skip link skips to main content and returns focus to the link after tabbing back.
   - No layout shift occurs during expansion.
5. Test with screen readers (NVDA, VoiceOver) to confirm no mid-page distractions.
6. Document the component’s usage in the EXCAVA design system.

**What changed:**
Added a persistent, subtle skip link that expands on keyboard focus.
