# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-626` (dept) · 2026-07-30T21:12:51.445014+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Ship a 5px solid focus ring with 3px outer offset in #0078D4
**Plan:**
1. Implement a 5px solid focus ring with 3px outer offset in #0078D4 across all EXCAVA components
2. Verify the contrast ratio of #0078D4 on dark backgrounds, including #121212, to ensure a minimum of 6.3:1
3. Conduct usability testing with 10 keyboard-only users on 5 live pages to gauge user preference and identify potential issues
4. Measure and document the contrast ratios and user feedback from the testing
5. Refine the focus ring design based on the test results, if necessary, to ensure optimal accessibility and usability
**What changed:** The focus ring design was updated from a proposed 4px solid ring with 4px offset in #005FCC to a 5px solid ring with 3px offset in #0078D4 to improve contrast and accessibility.
