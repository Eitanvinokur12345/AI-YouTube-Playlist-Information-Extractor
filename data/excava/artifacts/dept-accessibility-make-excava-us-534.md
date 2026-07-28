# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-534` (dept) · 2026-07-28T11:00:02.003648+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a semi-transparent, high-contrast focus ring with adjustable thickness (2px–4px) and color (WCAG 2.2 AA compliant), tested via Playwright MCP for keyboard/screen reader/touch users. Owned by Ramp.

**Plan:**
1. Implement a semi-transparent focus ring (WCAG 2.2 AA compliant) with adjustable thickness (2px–4px) and color.
2. Add Playwright MCP tests for keyboard navigation, screen reader compatibility, and touch device focus visibility.
3. Ensure the ring moves with tab order and remains visible on dense screens without obscuring critical content.
4. Provide user-configurable settings for thickness and color via EXCAVA’s accessibility panel.
5. Validate contrast ratios against WCAG 2.2 AA standards in all themes/backgrounds.
6. Document the feature in EXCAVA’s accessibility guide and update the design system.

**What changed:**
Replaced the single high-contrast moving ring with a semi-transparent, adjustable focus indicator to balance visibility and content clarity.
