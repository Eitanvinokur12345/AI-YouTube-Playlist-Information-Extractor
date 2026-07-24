# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-848` (dept) · 2026-07-24T18:01:31.948507+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a bold, full-width skip bar that appears only when focused, with high-contrast colors and no layout shift.

**Plan:**
1. Add a `<a>` skip link at the top of every page with `href="#main"` targeting the main content container.
2. Style the skip bar as a full-width, fixed-position element at the top of the viewport with `top: 0; left: 0; right: 0;`.
3. Apply high-contrast colors (e.g., `background: #000; color: #fff;`) and ensure it meets WCAG 2.1 AA contrast ratios.
4. Hide the skip bar by default with `opacity: 0; height: 0; overflow: hidden;` and reveal it on `:focus` with `opacity: 1; height: auto;`.
5. Ensure the skip bar does not cause layout shift by reserving space in the DOM (no `display: none`).
6. Test keyboard navigation to confirm the skip bar appears on `Tab` and successfully skips to `#main`.

**What changed:**
Added a full-width, high-contrast skip bar that appears only when focused, eliminating keyboard traps without visual clutter.
