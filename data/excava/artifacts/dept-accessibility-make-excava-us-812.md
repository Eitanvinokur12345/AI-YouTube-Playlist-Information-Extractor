# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-812` (dept) · 2026-07-17T17:40:34.672556+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a small, high-contrast skip link that collapses into a visible icon on keyboard focus.

**Plan:**
1. Add a skip link element (`<a href="#main-content">Skip to content</a>`) positioned off-screen by default.
2. Style it as a small, high-contrast button (e.g., 24x24px with bold text or icon) that remains hidden until keyboard focus.
3. On focus, animate it into view (e.g., slide from top-right) with sufficient contrast (WCAG 2.1 AA).
4. Ensure the link targets the main content container (`id="main-content"`).
5. Test with screen readers (NVDA/JAWS) and keyboard-only navigation for discoverability and functionality.
6. Document the skip link’s behavior in the project’s accessibility guidelines.

**What changed:** Added a small, high-contrast skip link visible only on keyboard focus, balancing space efficiency and accessibility.
