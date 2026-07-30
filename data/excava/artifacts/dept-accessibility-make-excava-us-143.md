# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-143` (dept) · 2026-07-30T17:54:00.669301+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship **3px outset focus ring, 4.5:1 contrast, 2px spacing**—verify touch safety at 125% zoom + 200% DPI; owner: Ramp.

**Plan:**
1. Implement 3px outset focus ring with 4.5:1 contrast in EXCAVA’s CSS.
2. Add 2px spacing between interactive elements to prevent overlap.
3. Test touch safety on mobile at 125% zoom and 200% DPI.
4. Validate focus visibility on high-DPI screens (e.g., Retina).
5. Audit keyboard navigation for clarity and WCAG AA compliance.
6. Document findings in EXCAVA’s accessibility tracker.

**What changed:**
Adopted 3px outset focus ring (4.5:1 contrast) with 2px spacing after balancing mobile/touch safety and high-DPI visibility.
