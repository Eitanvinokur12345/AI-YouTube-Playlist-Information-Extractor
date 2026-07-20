# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-371` (dept) · 2026-07-20T23:16:22.417177+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Implement a high-contrast, always-visible skip button styled like a button in the top-left corner of every page.

**Plan:**
1. Add a `<button>` skip link in the top-left corner of every page with high-contrast styling (e.g., dark background, light text).
2. Ensure the button is always visible but subtly integrated (e.g., small size, low opacity when inactive).
3. Test with keyboard users to confirm recognition and bypass effectiveness.
4. Include `aria-label="Skip to main content"` for screen readers.
5. Add CSS to ensure the button remains visible during focus states.
6. Document the skip button in the accessibility guidelines for future updates.

**What changed:**
Added a high-contrast, always-visible skip button styled like a button in the top-left corner.
