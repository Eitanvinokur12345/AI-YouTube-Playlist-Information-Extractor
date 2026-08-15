# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-333` (dept) · 2026-08-15T01:41:23.199970+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 2px solid #005fcc focus ring with 2px #fff inset at 80% opacity.

**Plan:**
1. Update EXCAVA’s focus ring style to `2px solid #005fcc` with `2px #fff inset` at 80% opacity.
2. Verify WCAG 2.2 AA contrast compliance on both light and dark backgrounds.
3. Test keyboard navigation across all interactive elements to ensure visibility.
4. Audit component edges to confirm focus state remains distinct from borders.
5. Document the change in EXCAVA’s accessibility guidelines.
6. Merge updates into the main branch with accessibility-w1 as owner.

**What changed:** Focus ring updated to 2px #005fcc with 2px #fff inset at 80% opacity for WCAG 2.2 AA compliance.
