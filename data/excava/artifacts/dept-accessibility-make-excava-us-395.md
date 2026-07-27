# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-395` (dept) · 2026-07-27T17:58:21.166216+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Add a high-contrast, first-tab skip link that appears after the first tab press, directing to a named `<main role="main">` landmark.

**Plan:**
1. Implement a hidden skip link (high-contrast) that appears only after the first `Tab` press.
2. Ensure the skip link targets a `<main role="main">` landmark with a descriptive `aria-label` (e.g., "Skip to main content").
3. Style the skip link to be visually distinct (e.g., bold, contrasting background) but unobtrusive when inactive.
4. Test keyboard navigation to confirm the link appears at the correct time and skips directly to `<main>`.
5. Validate with screen readers to ensure the landmark is announced properly.
6. Document the implementation in the accessibility guidelines for future reference.

**What changed:** Added a dynamic, first-tab skip link targeting a named `<main>` landmark.
