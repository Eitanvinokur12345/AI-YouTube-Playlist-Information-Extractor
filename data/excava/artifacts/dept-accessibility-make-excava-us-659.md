# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-659` (dept) · 2026-07-30T07:16:03.042840+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Ship a **3px solid focus ring (4.5:1 contrast), outset 1px**, tested across high-DPI/low-contrast screens.

**Plan:**
1. Implement a **3px solid focus ring** with **4.5:1 contrast ratio** against the background.
2. Position the ring **outset 1px** to avoid layout overlap.
3. Validate focus visibility on **high-DPI and low-contrast screens**.
4. Test keyboard navigation across all interactive elements.
5. Document the focus ring style in the design system.
6. Assign ownership to **accessibility-w1** for ongoing maintenance.

**What changed:** Focus ring upgraded from 2px inset to 3px outset with 4.5:1 contrast.
