# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-115` (dept) · 2026-08-13T08:03:34.832400+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a 3px solid focus ring with a 1px inner white edge at 100% opacity, defaulting to `#005fcc` and switching to `#003366` if WCAG 2.2 contrast fails on light backgrounds.

**Plan:**
1. Implement the 3px `#005fcc` focus ring with 1px inner `#fff` at 100% opacity.
2. Test WCAG 2.2 contrast on light backgrounds; if fails, switch ring color to `#003366`.
3. Verify contrast passes in both light/dark themes (3:1 minimum).
4. Ensure ring remains visible in dense layouts without overwhelming UI.
5. Deliver final CSS artifact with test results to Ramp.
6. Document fallback logic for color switching in code comments.

**What changed:**
Default ring color switches from `#005fcc` to `#003366` if light-background contrast fails.
