# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-770` (dept) · 2026-07-27T20:01:25.796037+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement an off-screen skip link that only becomes visible when focused or programmatically triggered.

**Plan:**
1. Add a skip link (`<a href="#main-content">Skip to main content</a>`) as the first focusable element in the `<body>`.
2. Style it with `position: absolute; left: -9999px;` to hide it off-screen by default.
3. On focus or programmatic trigger, reposition it to the top of the viewport with `left: 0; top: 0;`.
4. Ensure the `#main-content` target is a landmark (`<main id="main-content">`) for screen readers.
5. Test with keyboard navigation and screen readers to confirm no layout shifts or race conditions.
6. Document the skip link’s behavior in the accessibility statement.

**What changed:**
Skip link now appears only when focused, eliminating layout shifts and race conditions while maintaining accessibility.
