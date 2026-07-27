# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-839` (dept) · 2026-07-27T18:19:15.912459+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Add a high-contrast skip link at page top and ensure every page has a `<main role="main">` landmark plus ARIA live regions for dynamic updates.

**Plan:**
1. Implement a high-contrast skip link at the very top of every page that allows users to jump directly to the main content.
2. Ensure every page contains a clearly labeled `<main role="main">` landmark to aid screen reader users.
3. Integrate ARIA live regions to announce dynamic content updates for users relying on assistive technologies.
4. Test keyboard navigation to confirm users can easily bypass navigation blocks.
5. Conduct user testing involving both keyboard users and screen reader users to validate accessibility improvements.

**What changed:** A comprehensive solution was reached that addresses keyboard navigation, screen reader landmarks, and dynamic content updates.
