# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-862` (dept) · 2026-07-30T23:57:00.153311+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **4px solid focus ring in #0078D4 with 3px outer offset** on every interactive element.

**Plan:**
1. Audit all interactive elements (buttons, links, inputs, etc.) for keyboard focus styles.
2. Apply the 4px solid focus ring in #0078D4 with 3px outer offset via CSS.
3. Verify 4.5:1 contrast ratio in both light and dark modes using a contrast checker.
4. Test keyboard navigation across devices to ensure visibility and non-overlap.
5. Document the focus ring style in the design system for future components.
6. Add a regression test to prevent future contrast or offset regressions.

**What changed:**
Added a 4px #0078D4 focus ring with 3px outer offset to all interactive elements.
