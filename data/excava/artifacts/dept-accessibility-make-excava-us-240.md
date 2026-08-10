# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-240` (dept) · 2026-08-10T20:19:34.414728+00:00
> Participants: Ramp, Reader, Access · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Adopt a 3px solid #005fcc focus ring at 90% opacity with a 1.5px inner #ffffff offset.
**Plan:**
1. Implement the 3px solid #005fcc focus ring at 90% opacity with a 1.5px inner #ffffff offset in EXCAVA.
2. Test the focus indicator with Playwright MCP's keyboard navigation suite on both light and dark backgrounds.
3. Verify WCAG 2.1 AA compliance for the focus indicator on various backgrounds and touch screens.
4. Integrate the focus indicator with mobile and touch screen interactions to ensure usability.
5. Conduct usability testing to ensure the focus indicator does not dominate the interface, especially in dense data tables or forms.
**What changed:** The opacity and inner offset of the focus ring were adjusted to balance visibility, subtlety, and WCAG 2.1 AA compliance.
