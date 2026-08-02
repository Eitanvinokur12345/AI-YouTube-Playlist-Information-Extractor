# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-415` (dept) · 2026-08-02T17:49:27.643603+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 4px #005fcc outer ring with a 2px white inner ring for focus indicators.

**Plan:**
1. Implement the 4px #005fcc outer ring with a 2px white inner ring for all interactive elements.
2. Validate contrast ratios against actual patterned backgrounds to ensure 3:1 minimum contrast.
3. Test visibility on light, dark, and patterned backgrounds across devices and browsers.
4. Document the focus ring style in the design system for consistency.
5. Update the accessibility audit checklist to include focus ring contrast verification.
6. Assign worker-5301 to oversee implementation and validation.

**What changed:** Focus indicator style updated to 4px #005fcc outer ring with 2px white inner ring.
