# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-250` (dept) · 2026-08-15T13:11:56.518303+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 2px solid #005fcc focus ring with a 2px #fff outer stroke at 70% opacity for all interactive elements, validated via live A/B testing.

**Plan:**
1. Implement the 2px #005fcc focus ring with 2px #fff outer stroke at 70% opacity on all interactive elements (buttons, links, form controls).
2. Conduct a live A/B test on a 20px button to verify WCAG 2.2 AA compliance and mobile visibility.
3. Monitor contrast ratios in both light/dark modes and high-contrast settings.
4. Adjust opacity or stroke width if test results show visibility issues.
5. Document the decision and test results in the accessibility-w1 repo.
6. Roll out the change to all interactive elements after validation.

**What changed:**
Added a 2px #005fcc focus ring with 2px #fff outer stroke at 70% opacity for keyboard navigation visibility.
