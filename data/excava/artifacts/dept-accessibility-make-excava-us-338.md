# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-338` (dept) · 2026-08-28T12:41:21.274403+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white) — deliver a tested, high-contrast focus style for EXCAVA and own it.

**Plan:**
1. Implement 3px focus ring with 7:1 contrast ratio across all interactive elements.
2. Add 1px white outer glow (or equivalent background-aware glow) for grayscale/high-contrast modes.
3. Test focus visibility in monochrome, patterned, and high-contrast modes (Windows HCM, macOS grayscale, forced colors).
4. Validate touch target clarity on mobile (avoid overlap with adjacent elements).
5. Document focus styles in design system with fallback rules for edge cases.
6. Ship with automated focus ring testing in CI/CD pipeline.

**What changed:** Switched from 4px/7:1 to 3px/7:1 + glow for balance between visibility and UI density.
