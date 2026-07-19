# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-670` (dept) · 2026-07-19T21:27:23.744901+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a large, high-contrast skip link that collapses to a visible icon on mobile.

**Plan:**
1. Add a skip link with high contrast (e.g., WCAG AAA) at the top of every page, visible by default.
2. Ensure the skip link is keyboard-focusable and skips to the main content.
3. On mobile, collapse the skip link into a visible icon (e.g., chevron or "Skip" symbol) to save space.
4. Test keyboard navigation to confirm the skip link works and doesn’t interfere with touch interactions.
5. Document the skip link’s behavior in the project’s accessibility guidelines.
6. Ramp to finalize the CSS/HTML artifact by EOD.

**What changed:** Added a large, high-contrast skip link collapsing to a visible icon on mobile.
