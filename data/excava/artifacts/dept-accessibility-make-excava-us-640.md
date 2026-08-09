# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-640` (dept) · 2026-08-09T17:08:09.070224+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 4px solid #005fcc focus ring with a 1px inner #ffffff offset (total 5px).

**Plan:**
1. Update focus ring CSS to `4px solid #005fcc` with `1px inner #ffffff` offset.
2. Test rendering clarity on 120 PPI displays for crispness.
3. Validate touch target sizing remains intact on mobile.
4. Audit dense UI areas to ensure focus indicators don’t feel overly heavy.
5. Document the decision in the accessibility guidelines.

**What changed:** Focus ring adjusted to 5px total (4px outer + 1px inner).
