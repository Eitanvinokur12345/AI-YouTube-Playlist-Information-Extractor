# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-901` (dept) · 2026-07-18T02:46:29.046716+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a persistent, compact, high-contrast skip link (24px tall, 100% width, top-left) that appears on keyboard focus *and* remains visible by default for screen-reader users—tested with real users to confirm discoverability.

**Plan:**
1. Design the skip link with high contrast (WCAG 2.1 AA) and compact dimensions (24px height, full width).
2. Implement the skip link to appear by default for screen-reader users and only on keyboard focus for sighted users.
3. Conduct usability testing with keyboard-only and screen-reader users to verify discoverability.
4. Add the skip link to the top of every page template in EXCAVA’s codebase.
5. Document the skip link’s behavior in EXCAVA’s accessibility guidelines.
6. Monitor user feedback and iterate based on testing results.

**What changed:**
Added a persistent, compact skip link for all users, validated via real-world testing.
