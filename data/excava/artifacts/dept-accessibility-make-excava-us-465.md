# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-465` (dept) · 2026-07-31T03:10:28.948794+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **4px solid focus ring in #0078D4 at 100% opacity with a 3px outer offset** on all interactive elements.

**Plan:**
1. Audit all interactive elements to ensure consistent focus ring styling.
2. Implement the 4px #0078D4 focus ring with 3px outer offset in the design system.
3. Verify 4.5:1 contrast ratio on dark gray (#111) using a contrast checker.
4. Test keyboard navigation across all components to confirm visibility.
5. Document the focus ring specs in the accessibility guidelines.
6. Deploy changes in the next release cycle.

**What changed:**
Added a 4px #0078D4 focus ring with 3px outer offset to all interactive elements.
