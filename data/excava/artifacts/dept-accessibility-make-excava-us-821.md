# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-821` (dept) · 2026-07-27T22:11:28.982044+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a server-rendered skip link (first 100 bytes) targeting the first focusable element in main content, with Playwright MCP tests confirming no keyboard traps—owned by Ramp.

**Plan:**
1. Implement a server-rendered skip link at the top of every page, loading within the first 100 bytes of the HTML.
2. Target the first focusable element inside the main content region (e.g., `<main>` or `<div id="main">`).
3. Add Playwright MCP tests to verify the skip link works without keyboard traps, including late JavaScript scenarios.
4. Ensure the skip link is hidden until JavaScript confirms functionality (e.g., via `aria-hidden="true"` initially, then removed on load).
5. Document the skip link’s behavior and ownership (Ramp) in the project’s accessibility guidelines.
6. Conduct user testing with screen reader and keyboard-only users to validate usability.

**What changed:**
Added a server-rendered skip link targeting the first focusable element in main content, enforced by Playwright MCP tests.
