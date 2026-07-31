# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-349` (dept) · 2026-07-31T23:17:55.138033+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a single 4px #005fcc focus ring with a 2px solid white inset shadow for all interactive elements.

**Plan:**
1. Replace all existing focus ring styles with `outline: 4px solid #005fcc; outline-offset: 2px; box-shadow: inset 0 0 0 2px white;`.
2. Ensure the inset shadow is applied universally to buttons, links, form inputs, and focusable custom components.
3. Test in high-contrast mode (Windows HCM) to confirm visibility against both light/dark backgrounds.
4. Validate keyboard navigation flow across all interactive elements for consistent focus visibility.
5. Audit small/dense interfaces to ensure the inset shadow does not create visual clutter or overlap issues.
6. Document the style in the design system’s focus indicator guidelines with usage examples.

**What changed:** Switched from a double ring or blur-based approach to a single 4px #005fcc ring with a 2px solid white inset shadow for universal high-contrast visibility.
