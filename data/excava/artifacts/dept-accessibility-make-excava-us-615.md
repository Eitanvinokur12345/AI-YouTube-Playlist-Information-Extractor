# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-615` (dept) · 2026-07-30T17:31:38.111777+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a **2.5px solid focus ring, outset 1px**, with a **4.5:1 contrast ratio**.

**Plan:**
1. Implement the 2.5px outset focus ring in the design system.
2. Set the contrast ratio to 4.5:1 against all backgrounds.
3. Test in Playwright MCP at 125% zoom on a 4K screen.
4. Validate WCAG AA compliance for normal text.
5. Document the focus ring specs in the accessibility guidelines.
6. Review layout impact on dense forms and adjust spacing if needed.

**What changed:**
Focus ring adjusted to 2.5px outset with 4.5:1 contrast.
