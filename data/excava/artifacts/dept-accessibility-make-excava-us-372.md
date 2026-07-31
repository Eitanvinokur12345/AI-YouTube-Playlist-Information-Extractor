# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-372` (dept) · 2026-07-31T20:59:33.526024+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Use a high-contrast, system-agnostic focus ring with a subtle inset shadow for consistent visibility.

**Plan:**
1. Apply a **3px solid focus ring** using system accent colors (`#007AFF` for macOS, `#0066CC` for Windows).
2. Add a **1px inset shadow** (darker than the ring) to enhance contrast on all backgrounds.
3. Ensure the ring meets **WCAG 2.2 AA** (3:1 contrast) on light, dark, and textured surfaces.
4. Test focus visibility in **Playwright** with EXCAVA’s interactive elements.
5. Document the CSS in `accessibility-w1` for implementation.
6. Validate compliance via automated and manual checks.

**What changed:**
Replaced layered focus rings with a single, high-contrast system accent ring + inset shadow.
