# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-800` (dept) · 2026-08-23T17:39:28.649541+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 1px solid focus ring at 7:1 contrast with 2px transparent offset, no blur—deliver live-tested CSS in EXCAVA’s component library, owned by Ramp.

**Plan:**
1. Implement `focus-ring: 1px solid currentColor` with `outline-offset: 2px` in EXCAVA’s focus styles.
2. Set `currentColor` to ensure 7:1 contrast against all backgrounds (tested via WCAG contrast checker).
3. Add `outline-style: solid` and `outline-width: 1px` to override default browser focus styles.
4. Publish the CSS in EXCAVA’s component library under `components/focus-ring.css`.
5. Assign Ramp as the owner for maintenance and updates.
6. Verify crisp rendering at 200% zoom on 4K screens via automated visual regression tests.

**What changed:**
Focus ring now uses 1px solid at 7:1 contrast with 2px transparent offset (no blur).
