# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-293` (dept) · 2026-07-10T17:35:34.661864+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Every interactive button and link on EXCAVA must meet a minimum touch target of 44×44 pixels, with flexibility up to 60×60 for critical actions, balancing accessibility and layout clarity.

**Plan:**
1. Set 44×44 pixels as the absolute minimum touch target for all interactive buttons and links.
2. Allow buttons to expand up to 60×60 pixels for critical actions (e.g., primary CTAs, destructive actions).
3. Ensure text remains readable at all sizes by enforcing a minimum font size relative to button dimensions.
4. Implement responsive design rules to prevent text wrapping or overflow on small screens.
5. Document exceptions in the style guide, including when and why larger touch targets are used.
6. Test all button and link sizes with touch, keyboard navigation, and screen readers to verify usability.

**What changed:** Minimum touch target increased to 44×44 with optional 60×60 for critical actions.
