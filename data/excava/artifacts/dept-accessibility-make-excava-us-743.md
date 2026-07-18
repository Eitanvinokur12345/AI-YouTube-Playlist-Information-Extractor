# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-743` (dept) · 2026-07-18T01:28:46.007977+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Implement a compact, high-contrast skip link that’s always visible but collapses to a small icon when focused—with a subtle focus hint on the first element.

**Plan:**
1. Add a compact skip link (high-contrast, minimal footprint) at the top of every page.
2. Style it to collapse into a small icon when focused (e.g., via CSS `:focus` state).
3. Include a subtle focus hint (e.g., faint outline) on the first focusable element to indicate skip link availability.
4. Ensure the skip link bypasses repetitive navigation blocks in one click for keyboard users.
5. Test across mobile/touch, reduced-motion, and keyboard navigation scenarios.
6. Document the skip link’s behavior in EXCAVA’s accessibility guidelines.

**What changed:** Added a compact, always-visible skip link with focus-based icon collapse and subtle hint for keyboard navigation.
