# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-935` (dept) · 2026-08-14T19:32:37.847178+00:00
> Participants: Ramp, Reader, Access · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the 3px solid #005fcc focus ring with 1px inner #fff at 70% opacity.

**Plan:**
1. Implement the CSS snippet for the focus ring across all interactive elements.
2. Test WCAG 2.1 AA compliance in high-contrast mode and dark/light backgrounds.
3. Capture screenshots in high-contrast, dark, and light modes for validation.
4. Deploy changes to staging and verify keyboard navigation with screen readers.
5. Gather feedback from QA on visual clutter and mobile/touch usability.
6. Finalize and merge into main branch by EOD today.

**What changed:** Focus ring updated to 3px #005fcc with 1px #fff inset at 70% opacity.
