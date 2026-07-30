# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-198` (dept) · 2026-07-30T20:50:44.305331+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a 3px outset focus ring with 4.5:1 contrast, 2px spacing, colored #007AFF, tested via Playwright MCP on light/dark modes and dynamic backgrounds.

**Plan:**
1. Implement a 3px solid focus ring with 2px outer spacing, colored #007AFF.
2. Ensure 4.5:1 contrast ratio against both light and dark backgrounds.
3. Add Playwright MCP tests to verify focus ring visibility in light/dark modes.
4. Test focus ring visibility on dynamic backgrounds (e.g., gradients, images).
5. Document focus ring behavior in design system guidelines.
6. Conduct user testing with keyboard-navigating participants for validation.

**What changed:**
Replaced static 2px ring with dynamic 3px ring (#007AFF, 4.5:1 contrast, 2px spacing) and added Playwright MCP testing for all modes.
