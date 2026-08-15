# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-576` (dept) · 2026-08-15T22:13:42.248602+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with a 2px #fff outer stroke for improved visibility and WCAG 2.2 AA compliance.

**Plan:**
1. Update the focus ring to 2px solid #005fcc with a 2px #fff outer stroke.
2. Conduct live contrast testing against WCAG 2.2 AA guidelines for both light and dark backgrounds.
3. Validate battery impact on mobile devices with the new focus ring.
4. Document the new focus ring style in the design system.
5. Implement the updated focus ring across all components in EXCAVA.
6. Test keyboard navigation to ensure the focus ring remains visible and functional.

**What changed:**
Focus ring thickness increased to 2px with a 2px white outer stroke for better visibility and WCAG compliance.
