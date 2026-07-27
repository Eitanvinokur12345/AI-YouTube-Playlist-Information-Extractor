# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-139` (dept) · 2026-07-27T19:40:07.356033+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Add a high-contrast skip link always visible at the top of every page, outside dynamic containers, to ensure it remains in tab order and survives DOM updates.

**Plan:**
1. Place the skip link as the first focusable element in the DOM, outside any dynamic containers.
2. Ensure the skip link is always visible and high-contrast, with clear keyboard focus indicators.
3. Test with screen readers (e.g., NVDA, VoiceOver) to confirm it survives DOM updates and remains accessible.
4. Verify keyboard navigation flow: pressing Tab from the top should reach the skip link first, then the main content.
5. Add a persistent skip link that appears on keyboard focus but does not re-render with dynamic content.
6. Document the skip link’s behavior and ownership (Ramp) in the accessibility guidelines.

**What changed:** Added a persistent, high-contrast skip link at the page top, outside dynamic containers.
