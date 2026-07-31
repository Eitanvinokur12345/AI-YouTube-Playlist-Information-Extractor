# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-350` (dept) · 2026-07-31T22:57:27.859309+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a single 4px `#005fcc` focus ring with a 2px solid white outer stroke at 80% opacity on all focusable elements.

**Plan:**
1. Implement the composite focus ring (4px `#005fcc` + 2px white @80% outer stroke) on all interactive elements.
2. Test visibility in normal, high-contrast, and 200% zoomed modes using Windows High Contrast Mode and browser zoom.
3. Ensure the ring remains intact during pinch-zoom and does not misalign or break into segments.
4. Validate keyboard navigation across touch, mouse, and screen reader contexts.
5. Document the focus ring style in the design system for consistency.
6. Conduct user testing with participants using high-contrast mode and screen readers.

**What changed:**
Replaced the blurred white shadow with a solid white outer stroke to ensure visibility in high-contrast and zoomed modes without misalignment.
