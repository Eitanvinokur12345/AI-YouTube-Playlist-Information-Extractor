# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-358` (dept) · 2026-07-31T12:20:16.989200+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2-pixel solid focus ring with WCAG 2.1 AA contrast (no glow).

**Plan:**
1. Set focus ring to 2px solid with color meeting WCAG 2.1 AA contrast.
2. Remove outer glow effect entirely.
3. Apply focus ring to all interactive elements (buttons, links, inputs).
4. Test keyboard navigation and mobile/touch targets for clarity.
5. Verify contrast via automated checker (e.g., Stark, axe).
6. Document ring style in shared CSS variables for consistency.

**What changed:**
Focus ring reduced to 2px with WCAG 2.1 AA contrast, glow removed.
