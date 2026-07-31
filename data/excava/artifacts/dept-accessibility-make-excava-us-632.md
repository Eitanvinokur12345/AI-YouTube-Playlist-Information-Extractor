# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-632` (dept) · 2026-07-31T00:25:03.872001+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Ship a 3px solid focus ring in #000000 at 90% opacity with 3px outer offset on all keyboard-focusable interactive elements.
**Plan:**
1. Implement a 3px solid focus ring with a 3px outer offset on every interactive element that receives keyboard focus.
2. Use the color #000000 at 90% opacity for the focus ring to ensure sufficient contrast on both light and dark backgrounds.
3. Test the focus ring implementation using Playwright MCP to confirm WCAG 2.1 AA contrast compliance.
4. Merge the CSS rule for the focus ring to the main branch for deployment.
5. Verify that the focus ring is clearly visible and does not obscure adjacent content on various backgrounds and devices.
6. Monitor user feedback and accessibility test results to ensure the focus ring meets the needs of all users.
**What changed:** The opacity of the focus ring color was increased to 90% to meet the 4.5:1 contrast requirement on dark backgrounds.
