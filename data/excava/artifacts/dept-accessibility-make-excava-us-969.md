# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-969` (dept) · 2026-07-18T23:29:14.485234+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a persistent, subtle skip link (1px by 1px underline) at the top of every page, visible only when keyboard-focused, with high contrast on focus.

**Plan:**
1. Add a skip link (`<a href="#main">Skip to content</a>`) as the first element in the `<body>` of every page.
2. Style the skip link with `position: absolute; left: -9999px; opacity: 0;` by default, and `left: 0; opacity: 1;` on `:focus` (with high-contrast focus styles).
3. Ensure the skip link targets the main content container (e.g., `<main id="main">`).
4. Test keyboard navigation flow to confirm the skip link works in all major browsers and screen readers.
5. Document the skip link’s behavior in the project’s accessibility guidelines.
6. Ramp to deploy the changes by EOD Friday.

**What changed:**
Added a persistent, subtle skip link visible only on keyboard focus.
