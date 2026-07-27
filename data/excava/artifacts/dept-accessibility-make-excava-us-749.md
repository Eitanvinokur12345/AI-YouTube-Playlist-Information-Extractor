# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-749` (dept) · 2026-07-27T06:15:11.501529+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Add **bold, full-width skip bars** at the top and bottom of every page—one for jumping to main content, one for returning to top.

**Plan:**
1. Implement a **top skip bar** with a single high-contrast button labeled "Skip to main content" that jumps directly to the `<main>` element.
2. Add a **bottom skip bar** with a high-contrast button labeled "Return to top" that scrolls to the top of the page.
3. Ensure both skip bars are **full-width** and **keyboard-focusable** (visible on `:focus`).
4. Test with keyboard-only users to validate speed and clarity of navigation.
5. Document the skip bars in the accessibility style guide and component library.
6. Owner: `accessibility-w1` to implement and verify compliance.

**What changed:** Added bold, full-width skip bars (top/bottom) for faster keyboard navigation.
