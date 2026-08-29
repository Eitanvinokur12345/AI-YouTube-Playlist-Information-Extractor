# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-392` (dept) · 2026-08-29T04:30:31.656774+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 5px focus ring at 7:1 contrast with `prefers-reduced-motion` and `forced-colors: active` overrides.

**Plan:**
1. Implement 5px focus ring with 7:1 contrast ratio.
2. Add `prefers-reduced-motion: no-preference` override for standard contrast.
3. Add `forced-colors: active` override to ensure visibility in high-contrast modes.
4. Conduct user testing to measure task completion for screen-reader and motor-impaired users.
5. Document overrides in the accessibility style guide.
6. Update EXCAVA’s design system with the finalized focus ring specifications.

**What changed:**
Focus ring width increased to 5px with dual overrides for reduced-motion and high-contrast modes.
