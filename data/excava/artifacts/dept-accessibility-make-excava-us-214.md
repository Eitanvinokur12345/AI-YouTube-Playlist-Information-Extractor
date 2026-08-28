# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-214` (dept) · 2026-08-28T11:19:14.067704+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Finalize 4px solid focus ring at 7:1 contrast, static design, validated with keyboard-only users at 200% zoom.

**Plan:**
1. Implement 4px solid focus ring with 7:1 contrast ratio across all interactive elements.
2. Ensure static design (no dynamic scaling) for consistency across resolutions.
3. Conduct keyboard-only user testing at 200% zoom to validate visibility and spacing.
4. Audit mobile/touch layouts to confirm no overlap with small interactive elements.
5. Document focus ring specs in design system for future components.
6. Add focus ring to high-contrast/monochrome display test cases.

**What changed:**
Switched from 5px/3px to 4px ring at 7:1 contrast for balanced visibility, space efficiency, and high-DPI resilience.
