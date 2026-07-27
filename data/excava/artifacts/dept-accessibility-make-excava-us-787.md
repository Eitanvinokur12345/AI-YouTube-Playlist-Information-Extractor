# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-787` (dept) · 2026-07-27T19:01:08.323622+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Add a high-contrast skip link at the very top of every page that jumps to `<main role="main">` and remains visible at all times.
2. Implement a programmatic focus trap that forces focus into `<main role="main">` on every route change or dynamic content injection.
3. Include an ARIA live region (`aria-live="polite"`) to announce content updates when `<main>` changes.
4. Ensure the skip link and focus trap are tested with screen readers and keyboard navigation in SPAs/lazy-loaded content.
5. Document the behavior in the accessibility guidelines for developers.
6. Deliver the solution by the next Sprint Review.

**What changed:** Added skip link, focus trap, and live region for consistent accessibility.
