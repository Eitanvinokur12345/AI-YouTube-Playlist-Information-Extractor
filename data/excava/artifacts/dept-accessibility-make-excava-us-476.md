# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-476` (dept) · 2026-08-17T22:23:12.775885+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid #005fcc focus ring with a 2px outer glow at 6:1 contrast.

**Plan:**
1. Implement CSS rule for focus ring: `outline: 3px solid #005fcc; box-shadow: 0 0 2px 2px rgba(0, 95, 204, 0.7);`
2. Ensure focus ring meets 6:1 contrast ratio on all interactive elements.
3. Test on real patterned backgrounds at 125% zoom across devices.
4. Validate keyboard navigation flow with focus ring visibility.
5. Document changes in design system with usage examples.
6. Merge PR and deploy with rollback plan.

**What changed:**
Focus ring updated to 3px solid #005fcc with 2px outer glow at 6:1 contrast.
