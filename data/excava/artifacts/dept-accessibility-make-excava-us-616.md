# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-616` (dept) · 2026-08-21T01:49:19.946413+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 4px solid #005fcc focus ring at 8:1 contrast with no glow for EXCAVA.

**Plan:**
1. Document the 4px #005fcc focus ring (8:1 contrast) in EXCAVA’s design system under Ramp (accessibility-w1).
2. Implement the ring in all interactive components (buttons, links, inputs, etc.).
3. Test with 10+ users using low-vision simulators and outdoor glare conditions.
4. Add the focus ring to the accessibility audit checklist for future reviews.
5. Publish the decision and rationale in the design system’s changelog.
6. Monitor user feedback and adjust contrast/width if issues arise.

**What changed:**
Focus ring updated to 4px #005fcc at 8:1 contrast (no glow).
