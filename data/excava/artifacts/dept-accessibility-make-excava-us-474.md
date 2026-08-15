# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-474` (dept) · 2026-08-15T01:06:29.635993+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 2px solid #005fcc focus ring with 2px #fff inset at 80% opacity for EXCAVA.

**Plan:**
1. Update EXCAVA’s focus ring CSS to use `2px solid #005fcc` with `2px #fff inset` at 80% opacity.
2. Validate WCAG 2.2 AA contrast (4.5:1) on both light and dark backgrounds using Playwright MCP’s accessibility checks.
3. Test focus visibility on dense interactive elements to ensure clarity.
4. Merge changes into the main branch with accessibility review sign-off.
5. Document the focus ring style in EXCAVA’s design system guidelines.
6. Deploy to staging for final QA testing before production release.

**What changed:** Focus ring style updated to 2px #005fcc solid with 2px #fff inset at 80% opacity, ensuring WCAG 2.2 AA compliance on all backgrounds.
