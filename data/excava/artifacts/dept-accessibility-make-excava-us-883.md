# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-883` (dept) · 2026-07-31T04:50:29.152881+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **2px solid focus ring in #0078D4 with 1px outer glow at 0s**.

**Plan:**
1. Update all interactive elements to use the 2px solid focus ring with 1px glow.
2. Ensure the glow uses `box-shadow: 0 0 0 1px #0078D4` for reduced-motion compliance.
3. Test visibility on low-contrast backgrounds and high-density screens.
4. Verify touch target clarity on mobile devices.
5. Document the focus style in the design system for consistency.
6. Add the focus style to the component library’s interactive examples.

**What changed:**
Focus indicator now uses a 2px ring with 1px glow in #0078D4.
