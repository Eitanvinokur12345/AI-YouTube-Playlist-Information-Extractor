# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-500` (dept) · 2026-08-03T03:35:10.608886+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Adopt the 2px #fff inner ring with a 1px #000 outer outline for focus indicators.
**Plan:**
1. Implement the 2px #fff inner ring with a 1px #000 outer outline for focus indicators across all elements in EXCAVA.
2. Conduct thorough testing on various high-contrast patterned backgrounds, including zebra-striped grids at 200% zoom.
3. Verify that the new focus indicator design meets WCAG 2.2 AA contrast requirements and survives reduced-motion tests.
4. Update the EXCAVA style guide to reflect the new focus indicator design.
5. Ensure that the new design is consistent across all platforms, including mobile and touch devices.
**What changed:** The focus indicator design was updated to a 2px #fff inner ring with a 1px #000 outer outline to guarantee visibility and compliance with WCAG 2.2 AA on all backgrounds and scenarios.
