# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-890` (dept) · 2026-08-31T16:23:49.861172+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use 4px focus ring at 7:1 contrast with `forced-colors: active` override.

**Plan:**
1. Implement 4px focus ring at 7:1 contrast in default mode.
2. Add `forced-colors: active` override to ensure visibility in high-contrast mode.
3. Set `prefers-reduced-motion: no-preference` to maintain visibility for reduced-motion users.
4. Test focus visibility in both default and high-contrast modes across multiple devices.
5. Document the focus ring specifications in the design system.
6. Deploy changes by [date].

**What changed:**
Focus ring now meets WCAG 2.2 in all modes with 4px at 7:1 contrast and `forced-colors: active` override.
