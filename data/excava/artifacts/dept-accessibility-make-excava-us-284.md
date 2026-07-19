# accessibility: Make EXCAVA usable by EVERYONE — contrast, mobile/touch, reduced-motion, keyboard nav, scr

> Decision artifact · room `dept-accessibility-make-excava-us-284` (dept) · 2026-07-19T10:09:39.636747+00:00
> Participants: Ramp, Reader, Access · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a 1px tall, persistent skip link underline that shrinks to 1px on blur, tested with screen readers—owned by Ramp.

**Plan:**
1. Develop a skip link that remains visible but has a height of 1px when not focused.
2. Ensure the skip link enlarges when keyboard focused to provide a clear indication of its activation.
3. Conduct usability testing with both keyboard and screen reader users to assess effectiveness and orientation cues.
4. Implement CSS and JavaScript to manage the visibility and behavior of the skip link.
5. Review and iterate based on feedback from testing to ensure accessibility goals are met.

**What changed:** A focus on maintaining user orientation while balancing visual minimalism led to the decision for a persistent but unobtrusive skip link design.
