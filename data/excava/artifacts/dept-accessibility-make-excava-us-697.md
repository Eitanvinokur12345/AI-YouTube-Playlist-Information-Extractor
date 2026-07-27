# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-697` (dept) · 2026-07-27T21:47:50.166625+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Ship a server-rendered skip link targeting the first focusable element in main content.

**Plan:**
1. Add `<a href="#main-start" class="skip-link">Skip to content</a>` at the top of every page, wrapped in the `<body>`.
2. Insert `<div id="main-start" tabindex="-1"></div>` as the first focusable element in the main content area.
3. Style `.skip-link` to be visually hidden until focus (e.g., `position: absolute; left: -9999px; top: 0;` → `left: 0;` on `:focus`).
4. Ensure the skip link is the first element in the DOM (before navigation).
5. Deploy behind a feature flag for 1 sprint, then measure tab-focus time via analytics.
6. Document the skip link’s behavior in the accessibility statement.

**What changed:** Server-rendered skip link targeting first focusable element replaces JS-dependent skip link.
