# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-407` (dept) · 2026-09-02T17:54:06.708210+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px focus ring at 4.5:1 contrast by default, with a 2px at 3:1 fallback in high-contrast mode.

**Plan:**
1. Update EXCAVA style guide with focus ring specs (3px/4.5:1 default, 2px/3:1 high-contrast).
2. Implement focus ring logic to dynamically adjust to user's high-contrast mode.
3. Test with screen readers toggling reduced motion and high contrast to validate edge cases.
4. Audit all interactive elements to ensure consistent focus ring application.
5. Document testing results in the accessibility-w1 repository.
6. Monitor feedback and adjust focus ring behavior if new edge cases emerge.

**What changed:**
Default focus ring reduced to 3px at 4.5:1 contrast, with high-contrast fallback.
