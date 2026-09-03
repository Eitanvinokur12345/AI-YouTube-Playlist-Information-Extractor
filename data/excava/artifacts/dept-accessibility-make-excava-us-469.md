# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-469` (dept) · 2026-09-03T00:34:57.124485+00:00
> Participants: Access, Ramp, Reader · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 4px focus ring at 7:1 contrast with no glow, validated by live contrast testing.

**Plan:**
1. Implement a 4px focus ring with 7:1 contrast ratio across all interactive elements.
2. Conduct live contrast tests on varied backgrounds (patterned, high-contrast, reduced-motion).
3. Ensure visibility persists without glow effects in all tested scenarios.
4. Document test results in the accessibility audit.
5. Apply the ring uniformly to buttons, links, and form controls.
6. Verify keyboard navigation and touch target clarity.

**What changed:**
Finalized 4px ring at 7:1 contrast after testing, removing glow dependency.
