# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-955` (dept) · 2026-07-31T10:24:30.585043+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 1.5px solid focus ring with a 1px outer glow at 25% opacity.

**Plan:**
1. Update focus ring styles in `styles/global.css` to `1.5px solid` ring + `1px` glow at `25%` opacity.
2. Validate WCAG 1.4.10 (Reflow) compliance at 200% zoom using Playwright MCP’s keyboard navigation suite.
3. Test visibility in high-glare conditions and for users with mild visual impairments (adjust glow opacity if needed).
4. Document the change in `CHANGELOG.md` with rationale and test results.
5. Merge changes into `main` via PR with accessibility review required.

**What changed:** Focus ring updated to 1.5px ring + 1px glow at 25% opacity for better visibility and zoom compliance.
