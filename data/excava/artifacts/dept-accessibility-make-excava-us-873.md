# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-873` (dept) · 2026-07-30T19:52:42.615303+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship **3px outset focus ring, 4.5:1 contrast, 2px spacing**—verify via Playwright MCP on 10 live interactive elements across 3 devices. Owner: Ramp.

**Plan:**
1. Implement 3px-wide focus ring with 4.5:1 contrast ratio and 2px offset on all interactive elements.
2. Run Playwright MCP tests on 10 live interactive elements across 3 devices (desktop, tablet, mobile).
3. Measure visibility in high-contrast, patterned, and low-contrast UI contexts.
4. Adjust ring width/offset if any element fails visibility checks.
5. Document test results and finalize implementation.
6. Assign Ramp as owner for post-ship monitoring and adjustments.

**What changed:**
Focus ring reduced to 3px width with 2px offset while maintaining 4.5:1 contrast.
