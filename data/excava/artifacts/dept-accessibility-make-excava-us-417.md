# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-417` (dept) · 2026-07-27T07:25:35.221268+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Use a single high-contrast "Skip to main content" link at the top of every page.

**Plan:**
1. Implement a single high-contrast skip link at the top of every page, targeting the main content area.
2. Ensure the skip link is keyboard-navigable and screen-reader-friendly with clear focus states.
3. Add the skip link to EXCAVA’s design system for consistency across all pages.
4. Conduct user testing to identify pages with complex structures (e.g., dashboards, forms) that may need additional skip links.
5. If testing reveals section-hopping needs, add context-aware skip links in a future update.
6. Document the skip link’s behavior and usage in EXCAVA’s accessibility guidelines.

**What changed:** Added a single high-contrast "Skip to main content" link to all pages.
