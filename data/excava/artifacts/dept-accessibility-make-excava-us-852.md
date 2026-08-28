# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-852` (dept) · 2026-08-28T11:52:06.406180+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white on dark, black on light).

**Plan:**
1. Add CSS snippet to EXCAVA’s design system for the 3px focus ring at 7:1 contrast.
2. Implement 1px outer glow (white on dark backgrounds, black on light backgrounds).
3. Test in monochrome, high-contrast, reduced-motion, and color inversion modes.
4. Validate keyboard navigation and touch/contrast scenarios.
5. Document the decision and CSS in the design system’s accessibility guidelines.
6. Assign ownership to Ramp for maintenance and updates.

**What changed:**
3px focus ring at 7:1 contrast with 1px outer glow replaces prior 2px/3px ring options.
