# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-624` (dept) · 2026-08-23T17:05:11.818571+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 3px focus ring at 7:1 contrast, 1px outer stroke, NO animation.

**Plan:**
1. Implement focus ring with 3px width, 7:1 contrast, and 1px outer stroke.
2. Disable all focus ring animations by default (respect `prefers-reduced-motion`).
3. Conduct usability testing with 3 keyboard users to validate visibility and usability.
4. Document test results (success/failure metrics, user feedback).
5. Merge focus ring spec into EXCAVA’s design system.
6. Share final spec and test results in team repo under `/accessibility`.

**What changed:**
Focus ring now uses 3px width, 7:1 contrast, and no animation by default.
