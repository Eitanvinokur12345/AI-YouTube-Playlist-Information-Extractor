# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-467` (dept) · 2026-07-31T11:35:34.209482+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt a 1-pixel solid focus ring with a 3-pixel outer glow at 10% opacity.

**Plan:**
1. Update focus ring styles to `1px solid` with `3px` outer glow at `10%` opacity.
2. Test at `125%` and `150%` zoom levels for stability.
3. Validate on high-contrast patterned backgrounds.
4. Ensure compatibility with keyboard navigation.
5. Document changes in the accessibility design system.
6. Deploy updates to all relevant components.

**What changed:** Focus ring updated to `1px solid + 3px 10% glow` for stability at all zoom levels and backgrounds.
