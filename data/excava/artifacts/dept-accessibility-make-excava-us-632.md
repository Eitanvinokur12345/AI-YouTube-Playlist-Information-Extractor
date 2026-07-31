# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-632` (dept) · 2026-07-31T12:50:01.023258+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Apply a **3px solid focus ring in #000000 at 90% opacity with 3px outer offset** to all keyboard-focusable interactive elements.
2. Ensure Playwright MCP tests confirm WCAG 2.1 AA contrast on both light and dark backgrounds.
3. Set a **24×24 px minimum touch target** for all interactive elements on mobile/touch devices.
4. Merge the CSS rule for the focus ring to the main branch.
5. Validate touch target compliance via automated testing (e.g., Playwright).
6. Document the focus ring and touch target specifications in the design system.

**What changed:** Added WCAG-compliant focus ring and touch targets to EXCAVA.
