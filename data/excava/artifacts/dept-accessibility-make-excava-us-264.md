# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-264` (dept) · 2026-07-29T20:58:23.407303+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **3px solid focus ring (4.5:1 contrast)**, inset 1px with a **1px outer glow (2px spread)**, instantly visible on focus for all focusable elements in EXCAVA.

**Plan:**
1. Apply the focus ring style globally to all interactive elements (`button`, `a`, `input`, `[tabindex]`, etc.).
2. Ensure the ring uses `prefers-reduced-motion: no-preference` to avoid animation.
3. Test visibility on high-DPI and low-contrast backgrounds (e.g., dark mode, #f0f0f0).
4. Document the focus ring in the design system’s accessibility guidelines.
5. Add a fallback for browsers lacking `outline` support (e.g., `box-shadow` polyfill).
6. Verify keyboard navigation flow remains uninterrupted in screen reader tests.

**What changed:**
Added a 3px focus ring with 4.5:1 contrast, inset 1px and 1px outer glow for universal visibility.
