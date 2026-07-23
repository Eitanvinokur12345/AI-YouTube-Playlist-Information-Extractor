# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-755` (dept) · 2026-07-23T23:30:12.363831+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement a one-time onboarding hint to inform users about the skip link.
**Plan:**
1. Design a subtle onboarding hint (e.g., “Press Tab to skip headers”) that appears on the first visit.
2. Implement the onboarding hint to fade after the first visit to avoid visual clutter.
3. Add a high-contrast skip link at the top of every page that becomes visible on keyboard focus.
4. Conduct A/B testing to track and compare skip link usage with and without the onboarding hint.
5. Analyze A/B testing results to validate the effectiveness of the onboarding hint.
**What changed:** The approach to informing users about the skip link shifted from a persistent or focus-based skip link to a one-time onboarding hint.
