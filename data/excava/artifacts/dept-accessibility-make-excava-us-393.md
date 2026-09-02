# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-393` (dept) · 2026-09-02T17:04:22.840202+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt a consistent 3px focus ring at 7:1 contrast for all interactive elements, with a switch to 3px at 4.5:1 when `prefers-contrast: high` is active.

**Plan:**
1. Set default focus ring style to `3px solid` with `7:1` contrast.
2. Add CSS media query to override focus ring to `3px solid` with `4.5:1` contrast when `prefers-contrast: high` is active.
3. Ensure no other focus ring styles override these rules (e.g., `prefers-reduced-motion` does not alter focus ring size or contrast).
4. Test in both normal and high-contrast modes across browsers (Chrome, Firefox, Safari, Edge).
5. Validate focus visibility against WCAG 2.2 SC 2.4.7 (Focus Visible) and SC 1.4.11 (Non-text Contrast).
6. Document the decision in the project’s accessibility guidelines.

**What changed:**
Focus ring now consistently uses 3px at 7:1 contrast, switching to 3px at 4.5:1 in high-contrast mode only.
