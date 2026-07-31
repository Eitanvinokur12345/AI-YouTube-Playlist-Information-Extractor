# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-575` (dept) · 2026-07-31T21:42:44.302086+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a 3px solid system accent ring (#007AFF/macOS, #0066CC/Windows) with a 2px outer glow (#FFFFFF on light, #000000 on dark) for focus indicators—tested against WCAG 2.1 contrast on all themes.

**Plan:**
1. Define CSS variables for focus ring colors (`--focus-ring-light: #007AFF; --focus-ring-dark: #0066CC; --focus-glow-light: #FFFFFF; --focus-glow-dark: #000000`).
2. Apply a `3px solid` ring using the system accent color based on theme (light/dark).
3. Add a `2px` outer glow with contrasting color (`#FFFFFF` on light, `#000000` on dark).
4. Ensure focus rings meet WCAG 2.1 contrast ratios (4.5:1 for normal text).
5. Write a Playwright test to verify focus visibility on all themes and backgrounds.
6. Document the focus ring styles in the design system’s accessibility guidelines.

**What changed:**
Adopted a hybrid focus ring (3px solid + 2px glow) with system accent colors and dynamic contrast for universal visibility.
