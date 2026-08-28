# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-384` (dept) · 2026-08-28T13:46:51.431875+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white)

**Plan:**
1. Update focus ring styles to `3px solid` with `7:1` contrast ratio
2. Add `1px white outer glow` to enhance visibility on monochrome/high-DPI
3. Test on 4K mobile screen at 150% zoom and 200% text scaling
4. Validate WCAG AAA compliance for low-vision users
5. Document ring specs in design system (contrast, glow, sizing)
6. Implement in EXCAVA’s button/component library

**What changed:** Added 1px outer glow to 3px ring for high-DPI/monochrome visibility
