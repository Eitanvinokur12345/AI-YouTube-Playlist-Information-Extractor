# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-386` (dept) · 2026-07-14T19:53:28.854892+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a small, always-visible skip link icon that expands to a full link on focus/hover.

**Plan:**
1. Design a minimal skip link icon (e.g., "Skip to content" symbol) placed at the top-left of every page.
2. Ensure the icon expands to a full text link ("Skip to main content") on focus or hover.
3. Add `aria-label="Skip to main content"` for screen reader clarity.
4. Test keyboard navigation to confirm the link works with and without JavaScript.
5. Verify screen reader compatibility (e.g., NVDA, VoiceOver) and slow-connection scenarios.
6. Document the skip link’s behavior in the project’s accessibility guidelines.

**What changed:** Added a hybrid skip link (icon + expandable text) for minimal footprint and guaranteed keyboard access.
