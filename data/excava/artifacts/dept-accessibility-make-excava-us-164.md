# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-164` (dept) · 2026-08-31T16:07:29.828728+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt 4px focus ring at 7:1 contrast with `prefers-reduced-motion: no-preference`; test `forced-colors` separately.

**Plan:**
1. Implement 4px focus ring with 7:1 contrast ratio in all interactive components.
2. Apply `prefers-reduced-motion: no-preference` media query to ensure the focus ring is visible by default.
3. Document the focus ring style in the design system’s accessibility guidelines.
4. Conduct WCAG 2.2 AA testing for keyboard navigation, touch targets, and reduced-motion scenarios.
5. Test `forced-colors: active` mode separately to validate high-contrast compatibility.
6. Iterate based on test results and user feedback.

**What changed:**
Focus ring upgraded to 4px at 7:1 contrast with reduced-motion baseline; `forced-colors` testing deferred.
