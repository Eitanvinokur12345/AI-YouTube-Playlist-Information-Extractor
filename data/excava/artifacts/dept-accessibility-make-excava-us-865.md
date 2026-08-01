# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-865` (dept) · 2026-07-31T21:20:44.107574+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Use a 3px solid system accent ring (#007AFF/macOS, #0066CC/Windows) with a 1px white inset (total 4px) for focus indicators.

**Plan:**
1. Implement the 3px focus ring with 1px white inset in the design system.
2. Test contrast ratios on live UI samples across light, dark, semi-transparent, and patterned backgrounds.
3. Validate with screen readers and keyboard navigation for visibility and usability.
4. Document the focus ring style in the accessibility guidelines.
5. Update component libraries and design tokens to reflect the new focus indicator.
6. Conduct user testing with participants who rely on keyboard navigation.

**What changed:** Focus ring style updated to a 3px system accent with 1px white inset for consistent visibility.
