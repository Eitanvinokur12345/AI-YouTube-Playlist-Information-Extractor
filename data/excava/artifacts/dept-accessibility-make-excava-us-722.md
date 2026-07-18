# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-722` (dept) · 2026-07-18T22:42:23.452778+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a persistent, subtle skip link (1px by 1px underline, high contrast on focus) placed before the first interactive element in the DOM.

**Plan:**
1. Add a `<a href="#main-content">Skip to main content</a>` link at the very top of every page’s DOM, before any navigation or headers.
2. Style the link with `position: absolute; left: -9999px;` by default and `left: 0; top: 0;` on `:focus-visible` to ensure it’s only visible when keyboard-focused.
3. Apply `font-size: 1.5rem; padding: 1em; background: #000; color: #fff;` to the focused state for high contrast and large touch target.
4. Ensure the link’s `href` points to an `id="main-content"` on the page’s primary content container.
5. Test with screen readers (NVDA/JAWS) and keyboard-only navigation to confirm immediate announcement and no cognitive overload.
6. Document the skip link’s purpose and behavior in the project’s accessibility guidelines.

**What changed:** Switched from conditional visibility to persistent, subtle skip link with high-contrast focus state.
