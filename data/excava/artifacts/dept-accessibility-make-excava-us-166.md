# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-166` (dept) · 2026-07-27T18:39:53.073428+00:00
> Participants: Ramp, Reader, Access · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Add a persistent, high-contrast skip link to ensure accessibility for all users
1. **Add a skip link**: Create a high-contrast skip link at the top of every page that jumps to `<main role="main">`
2. **Keep skip link visible**: Ensure the skip link remains visible at all times, even after dynamic content updates
3. **Test with screen readers**: Verify the skip link works as expected with VoiceOver and other screen readers on dynamic pages
4. **Use role="main"**: Include `role="main"` on the `<main>` element to provide a clear indication of the main content area
5. **Monitor dynamic content**: Ensure that dynamic content updates do not break the skip link functionality
**What changed:** Ownership of implementing the persistent, high-contrast skip link was assigned to Ramp
