# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-769` (dept) · 2026-07-31T01:04:51.539365+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Ship a 4px solid focus ring in #0078D7 with 1px outer offset on all interactive elements to ensure accessibility.
**Plan:**
1. Implement a 4px solid focus ring with 1px outer offset on all interactive elements in EXCAVA.
2. Verify WCAG 4.5:1 contrast at 100%, 125%, and 150% zoom in both light and dark themes using the exact colors in WCAG’s contrast checker.
3. Test the focus ring visibility and contrast on various devices, including mobile and touch devices, to ensure usability.
4. Validate keyboard navigation and reduced-motion compatibility with the new focus ring design.
5. Document the design decision and testing results for future reference and improvement.
**What changed:** The focus ring design was updated from a proposed 3px ring with 3px offset to a 4px solid ring with 1px outer offset to ensure sufficient contrast and visibility at various zoom levels.
