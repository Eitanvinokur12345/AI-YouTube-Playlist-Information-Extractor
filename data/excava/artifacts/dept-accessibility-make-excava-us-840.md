# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-840` (dept) · 2026-07-27T05:21:11.381806+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a **bold, full-width skip bar** that’s always visible but styled off-screen until focus arrives; test with screen-reader users navigating by virtual cursor—if they still miss it, add a brief ARIA live announcement on first tab press.

**Plan:**
1. Add a `<a class="skip-link">Skip to content</a>` at the top of every page, styled with `position: absolute; left: -9999px; top: 0;` (off-screen).
2. On `:focus-within` or `:focus-visible`, transition the skip bar into view (e.g., `left: 0; top: 0; background: #000; color: #fff; padding: 0.5rem 1rem;`).
3. Ensure the skip bar spans full width (`width: 100vw`) to avoid layout shifts.
4. Test with screen-reader users navigating via virtual cursor; if skip link is missed, add `aria-live="polite"` to announce "Skip link available" on first `Tab` press.
5. Confirm mobile/touch users can ignore it (no hover interference) and keyboard users get immediate bypass.
6. Document the skip bar’s behavior in the accessibility statement.

**What changed:** Skip link now works for screen-reader users (via virtual cursor) while remaining unobtrusive for sighted users.
