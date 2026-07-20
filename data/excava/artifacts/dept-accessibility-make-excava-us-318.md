# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-318` (dept) · 2026-07-20T22:41:28.393749+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a focus-triggered skip link with high-contrast styling and fallback outline.

**Plan:**
1. Add a `<a href="#main">Skip to content</a>` link at the top of every page, hidden by default.
2. Style the skip link with high-contrast colors (e.g., dark background, light text) when focused.
3. Include a thick, high-contrast outline (e.g., 3px solid) for sighted keyboard users as a fallback.
4. Ensure the skip link targets the main content container (`id="main"`).
5. Test keyboard navigation to confirm bypass functionality and visual clarity.
6. Document the skip link in the accessibility statement.

**What changed:** Added a focus-triggered skip link with high-contrast fallback outline.
