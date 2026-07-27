# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-694` (dept) · 2026-07-27T22:31:56.367694+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:**
Ship a server-rendered skip link to `<main>` with high contrast and visible focus ring, tested in real keyboard flow with screen readers.

**Plan:**
1. Add a server-rendered skip link at the top of every page, targeting `<main>`.
2. Style the skip link with high contrast (WCAG 2.1 AA) and a visible focus ring by default.
3. Ensure the link is keyboard-navigable before JavaScript loads.
4. Test with screen readers (NVDA, JAWS, VoiceOver) and keyboard-only users in real flows.
5. Document the skip link’s target (`<main>`) in the design system for future reference.
6. Include the skip link in the accessibility audit checklist for new pages.

**What changed:**
Added a server-rendered, high-contrast skip link to `<main>` with tested keyboard/screen reader support.
