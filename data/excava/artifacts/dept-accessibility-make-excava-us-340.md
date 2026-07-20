# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-340` (dept) · 2026-07-20T22:58:48.755471+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a focus-triggered skip link with a 100ms delay—high-contrast, full-width, keyboard-only visible.

**Plan:**
1. Add a `<a href="#main-content">Skip to main content</a>` at the top of every page, positioned off-screen initially.
2. Style the skip link with high contrast (WCAG 2.1 AA) and full-width layout for visibility on focus.
3. Hide the skip link by default (`opacity: 0; position: absolute; left: -9999px`).
4. Reveal it on `:focus-visible` with a 100ms delay (via CSS `transition-delay`).
5. Ensure the skip link targets the main content container (`id="main-content"`).
6. Test with screen readers (NVDA/JAWS) and keyboard-only navigation to verify timing and bypass functionality.

**What changed:**
Added a focus-triggered, high-contrast skip link with 100ms delay to ensure accessibility for keyboard and screen-reader users without visual clutter.
