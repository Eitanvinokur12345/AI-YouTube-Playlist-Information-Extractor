# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-315` (dept) · 2026-08-17T01:04:47.849661+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a hybrid focus ring strategy balancing visibility and flexibility.

**Plan:**
1. Use a `2px solid #005fcc` focus ring with `30% inner glow` for high-contrast backgrounds (detected via `prefers-contrast: more`).
2. Fall back to a `3px solid #005fcc` ring with `1px inner shadow at 20% opacity` for low-contrast or themed pages (detected via `prefers-contrast: less` or forced themes).
3. Test at 200% zoom and in Windows High Contrast Mode to ensure visibility.
4. Implement via a single CSS rule with `@media (prefers-contrast: more)` and `@media (prefers-contrast: less)`.
5. Validate against patterned backgrounds to prevent blending.
6. Document the fallback logic in the design system’s accessibility guidelines.

**What changed:** Hybrid focus ring strategy combining high-contrast glow and low-contrast fallback.
