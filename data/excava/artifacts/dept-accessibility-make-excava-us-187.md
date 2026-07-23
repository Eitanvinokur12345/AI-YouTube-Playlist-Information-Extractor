# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-187` (dept) · 2026-07-23T03:56:11.288672+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Add a high-contrast skip button at the top of every page, styled as a small button (e.g., 24x24px with a visible border).
2. Ensure the button is always visible but unobtrusive (e.g., positioned off-screen initially, sliding into view on focus or hover).
3. Label the button clearly (e.g., "Skip to content" or "Skip navigation").
4. Test keyboard navigation to confirm the button is reachable via `Tab` and triggers immediate skip functionality.
5. Verify contrast meets WCAG 2.1 AA (4.5:1 for text, 3:1 for buttons).
6. Document the skip button’s behavior in the accessibility statement.

**What changed:** Added a high-contrast, always-visible skip button to ensure immediate recognition for all users.
