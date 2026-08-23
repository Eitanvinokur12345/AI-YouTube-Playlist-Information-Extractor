# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-847` (dept) · 2026-08-23T13:12:42.709988+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 4px focus ring at 6:1 contrast, 1px outer stroke, 50ms fade-in—static fallback if vertigo reported.

**Plan:**
1. Implement focus ring with 4px width, 6:1 contrast, and 1px outer stroke.
2. Apply 50ms fade-in animation from 0% to 100% opacity.
3. Provide static focus ring as a fallback for users who report vertigo.
4. Test with screen-reader users, including those with vestibular sensitivity.
5. Ensure WCAG 2.2 AA compliance for contrast and motion preferences.
6. Document the focus ring behavior and fallback in the design system.

**What changed:**
Reduced fade duration to 50ms and adjusted contrast to 6:1 while keeping the 4px ring width.
