# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-589` (dept) · 2026-07-29T21:19:08.582386+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Ship a 3px solid focus ring (4.5:1 contrast), inset 1px, tested via Playwright MCP keyboard suite and validated with screen-reader users. Owner: Ramp.

**Plan:**
1. Implement the 3px solid focus ring (4.5:1 contrast) with 1px inset in the design system.
2. Update all interactive elements (buttons, links, inputs) to use the new focus ring.
3. Run Playwright MCP’s keyboard navigation suite to verify WCAG compliance.
4. Conduct user testing with screen-reader users to confirm visibility and usability.
5. Document the change in the accessibility changelog and update design tokens.
6. Monitor feedback post-release and iterate if issues arise.

**What changed:** Focus ring updated to 3px solid (4.5:1 contrast), inset 1px.
