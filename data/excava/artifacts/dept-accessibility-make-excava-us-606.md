# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-606` (dept) · 2026-08-03T02:44:29.345640+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Adopt the 3px #fff inner ring with a 1px #005fcc outer outline for focus indicators.
**Plan:**
1. Implement the 3px #fff inner ring with a 1px #005fcc outer outline as the new focus indicator style.
2. Conduct WCAG 2.2 AA compliance testing on various backgrounds, including light and dark patterned backgrounds.
3. Verify that the new focus indicator style meets contrast requirements and remains visible for keyboard users and users with low vision.
4. Refine the focus indicator style as needed based on testing results to ensure accessibility and minimal visual noise.
5. Update the EXCAVA UI to incorporate the new focus indicator style, ensuring consistency across all elements.
**What changed:** The focus indicator style was updated from a proposed 4px or 5px ring to a 3px #fff inner ring with a 1px #005fcc outer outline to better meet WCAG 2.2 AA contrast requirements on various backgrounds.
