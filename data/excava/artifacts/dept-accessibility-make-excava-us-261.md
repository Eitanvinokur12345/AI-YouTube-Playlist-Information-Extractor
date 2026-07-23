# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-261` (dept) · 2026-07-23T03:38:29.526985+00:00
> Participants: Access, Ramp, Reader · synthesized by sambanova/Meta-Llama-3.3-70B-Instruct

**Decision:** Implement a high-contrast, always-visible skip button to ensure discoverability and usability for all users.
**Plan:**
1. Add a single high-contrast skip link at the top of every page, styled to look like a functional element.
2. Ensure the skip link is always visible, allowing sighted keyboard users to discover it without relying on focus alone.
3. Pair the skip link with a visible focus indicator to maintain benefit for screen readers.
4. Use a bright focus ring to highlight the skip link when focused, avoiding visual clutter.
5. Implement a small extra CSS rule to control the visibility and styling of the skip link.
**What changed:** The decision shifted from a focus-dependent skip link to an always-visible, styled skip button to balance discoverability and usability for all users.
