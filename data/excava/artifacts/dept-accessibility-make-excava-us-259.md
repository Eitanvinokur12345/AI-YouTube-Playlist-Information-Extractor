# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-259` (dept) · 2026-07-30T22:05:47.608467+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Ship a 4px solid focus ring with a 2px outer offset, colored #005FCC, delivering 4.5:1 contrast against all backgrounds.
**Plan:**
1. Implement a 4px solid focus ring with a 2px outer offset on every interactive element.
2. Ensure the focus ring color #005FCC provides a 4.5:1 contrast ratio against all backgrounds.
3. Verify the focus ring's visibility on various backgrounds, including dark, patterned, and image-heavy screens.
4. Test the focus ring on mobile devices with keyboard-only navigation to ensure visibility despite screen glare.
5. Review and refine the focus ring design to balance visibility and subtlety.
**What changed:** The focus ring width was increased from 3px to 4px to guarantee visibility on dark, patterned, or glare-prone mobile screens.
