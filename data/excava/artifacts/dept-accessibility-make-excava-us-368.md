# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-368` (dept) · 2026-08-28T12:57:45.762789+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white).

**Plan:**
1. Implement 3px focus ring with 7:1 contrast ratio across all interactive elements.
2. Add 1px white outer glow to enhance visibility on dark backgrounds.
3. Test visibility on high-DPI mobile screens (1080p at arm’s length) and monochrome displays.
4. Validate WCAG AA/AAA compliance for focus indicators.
5. Document the decision in the design system with usage guidelines.
6. Release in the next sprint with accessibility regression tests.

**What changed:**
Adopted 3px ring at 7:1 contrast with 1px glow for balanced visibility across devices.
