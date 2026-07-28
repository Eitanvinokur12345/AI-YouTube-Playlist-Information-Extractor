# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-821` (dept) · 2026-07-28T23:25:54.015947+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Add a single, high-contrast focus ring that appears immediately on keyboard focus with no delay.
2. Ship a server-rendered skip link (first 100 bytes) targeting the first focusable element in main content.
3. Include Playwright MCP tests to confirm no keyboard traps with the skip link.
4. Ensure the skip link is non-negotiable and loads at the top of every page.
5. Maintain flexibility by targeting the first focusable element rather than a fixed ID.

**What changed:** Added server-rendered skip link with immediate focus ring and Playwright tests.
