# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-525` (dept) · 2026-07-31T17:26:53.973480+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005FCC focus ring at 20% opacity with no glow for interactive elements.

**Plan:**
1. Update focus ring styling to `3px solid #005FCC` at `20% opacity` for all interactive elements.
2. Remove glow effects from focus indicators.
3. Test WCAG 2.2 AA contrast compliance on light/dark backgrounds using Playwright MCP.
4. Validate visibility in high-contrast modes and zoomed views (up to 400%).
5. Document the change in the accessibility guidelines.
6. Deploy changes to staging for final review.

**What changed:**
Focus ring updated to 3px solid #005FCC at 20% opacity (no glow) for WCAG 2.2 AA compliance.
