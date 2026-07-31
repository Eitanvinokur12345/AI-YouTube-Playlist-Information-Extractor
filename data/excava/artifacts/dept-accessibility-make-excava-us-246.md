# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-246` (dept) · 2026-07-31T13:59:32.521445+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Set 48×48 px minimum touch targets with 2 px padding to balance WCAG compliance, density, and readability.
**Plan:**
1. Update EXCAVA's design guidelines to reflect the new minimum touch target size of 48×48 px.
2. Apply 2 px padding around labels for all interactive elements to prevent truncation and overlapping text.
3. Review and adjust the layout of tight toolbars and dense UIs to accommodate the new touch target size without compromising readability.
4. Conduct usability testing to ensure the new touch target size and padding do not introduce unintended accessibility issues.
5. Update EXCAVA's front-end code to implement the new touch target size and padding consistently across all platforms.
**What changed:** Minimum touch target size increased to 48×48 px with 2 px padding to balance accessibility, density, and readability.
