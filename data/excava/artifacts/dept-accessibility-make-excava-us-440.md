# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-440` (dept) · 2026-07-17T23:26:37.308417+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a small, high-contrast skip link that collapses into a thin line when not focused, fully visible when keyboard-focused.

**Plan:**
1. Add a skip link at the top of every page with `position: fixed`, `top: 0`, and `left: 0` (or similar).
2. Style it as a small, high-contrast element (e.g., 24px tall, high-contrast colors) when not focused.
3. On keyboard focus, expand it to full visibility (e.g., 48px tall, full label) with a smooth transition.
4. Ensure it collapses to a thin line (e.g., 2px height) when not focused to minimize mobile clutter.
5. Test with screen readers (NVDA/JAWS) and keyboard-only navigation for usability.
6. Document the skip link’s purpose in the accessibility statement.

**What changed:** Added a collapsible skip link for keyboard/screen-reader users without disrupting mobile layouts.
