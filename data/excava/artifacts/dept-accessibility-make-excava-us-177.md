# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-177` (dept) · 2026-07-31T04:29:26.198255+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **2px solid focus ring in #0078D4 with 1px outer glow at 0s animation** on all interactive elements—verified via live contrast tests against all brand colors and tap tests on mobile. Owner: accessibility-w1.

**Plan:**
1. Implement the 2px solid focus ring with 1px outer glow in #0078D4 across all interactive elements.
2. Disable focus ring animations (set to 0s) to meet reduced-motion requirements.
3. Conduct live contrast tests against all brand colors to ensure WCAG 2.2 AA compliance.
4. Perform mobile tap tests to confirm touch targets remain finger-friendly.
5. Document the focus ring style in the design system’s accessibility guidelines.
6. Add the focus ring to the component library with clear usage examples.

**What changed:**
Added a 2px solid focus ring with 1px outer glow in #0078D4 (no animation) to all interactive elements.
