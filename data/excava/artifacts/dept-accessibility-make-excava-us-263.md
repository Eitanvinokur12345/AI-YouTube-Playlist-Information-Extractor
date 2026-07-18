# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-263` (dept) · 2026-07-18T03:42:47.162967+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a persistent, high-contrast skip link that expands on keyboard focus.

**Plan:**
1. Add a skip link at the top of every page, visible by default but compact (e.g., small, high-contrast text).
2. Style the skip link to expand to full visibility (e.g., larger size, bold) when keyboard focus reaches it.
3. Ensure the skip link is programmatically focusable and skips to the main content.
4. Test with screen readers (VoiceOver, NVDA) and keyboard navigation (Tab key).
5. Document the skip link’s behavior in the accessibility statement.
6. Owner: accessibility-w1 to implement and validate.

**What changed:** Added a persistent, high-contrast skip link that expands on keyboard focus.
