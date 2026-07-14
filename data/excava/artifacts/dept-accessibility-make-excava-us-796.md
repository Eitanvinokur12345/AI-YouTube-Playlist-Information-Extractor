# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-796` (dept) · 2026-07-14T23:27:32.456116+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a hidden skip link that appears only after keyboard focus, tested for contrast and reduced motion.

**Plan:**
1. Add a skip link element (`<a href="#main-content">Skip to main content</a>`) at the top of every page, initially hidden via CSS (`display: none`).
2. Use JavaScript to detect the first `keydown` or `focus` event on the document and toggle the skip link’s visibility (`display: block`).
3. Ensure the skip link meets WCAG contrast requirements and respects `prefers-reduced-motion` by using a smooth transition.
4. Test keyboard navigation to confirm the skip link appears immediately on first tab press and jumps to `#main-content`.
5. Verify no visual clutter for mouse users and no dependency on JavaScript for functionality.
6. Document the change in the project’s accessibility guidelines.

**What changed:** Hidden skip link appears only after keyboard focus, improving accessibility without visual noise.
