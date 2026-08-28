# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-626` (dept) · 2026-08-28T12:24:57.482257+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Finalize 3px focus ring at 7:1 contrast with 1px outer glow (white) — deliver a tested, documented focus style in EXCAVA’s design system; owner: Ramp.

**Plan:**
1. Implement the 3px focus ring at 7:1 contrast with a 1px white outer glow in EXCAVA’s design system.
2. Conduct user tests measuring ring visibility on monochrome, low-contrast, and patterned backgrounds.
3. Document the focus style in EXCAVA’s design system with contrast ratios, implementation specs, and test results.
4. Ensure the style supports color inversion, reduced-motion, and keyboard navigation modes.
5. Add the focus style to EXCAVA’s component library for developers to integrate.
6. Schedule a review after 3 months to assess real-world performance and adjust if needed.

**What changed:** Focus ring updated to 3px at 7:1 contrast with 1px outer glow (white) for universal visibility.
