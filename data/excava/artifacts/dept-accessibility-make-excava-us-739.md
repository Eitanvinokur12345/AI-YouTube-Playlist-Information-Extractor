# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-739` (dept) · 2026-08-13T23:14:23.497998+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the 2px solid #005fcc focus ring with 2px inner #fff at 90% opacity for EXCAVA, with dynamic adjustment to 3px ring on light surfaces.

**Plan:**
1. Implement the 2px focus ring (#005fcc + 2px inner #fff at 90% opacity) as the default style.
2. Add a media query or JavaScript to detect light surfaces (e.g., background contrast < 4.5:1) and dynamically switch to a 3px ring.
3. Ensure the dynamic adjustment maintains WCAG 2.2 contrast ratios (4.5:1 minimum).
4. Test focus ring visibility on mobile, high-contrast, and low-contrast backgrounds.
5. Document the focus ring behavior in EXCAVA’s accessibility guidelines.
6. Assign Ramp as the owner for implementation and maintenance.

**What changed:**
Dynamic focus ring size adjustment (2px default, 3px on light surfaces)
