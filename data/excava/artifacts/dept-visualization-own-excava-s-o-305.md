# visualization: Own EXCAVA'S OWN interface — visibility, liveliness, clarity, enjoyment, speed of OUR scre

> Decision artifact · room `dept-visualization-own-excava-s-o-305` (dept) · 2026-07-18T01:22:45.883033+00:00
> Participants: Facet, Pane, Lumen · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Ship a hybrid approach that combines immediate feedback with guaranteed compliance.
1. **Implement a live contrast checker** that updates in real time as users adjust sliders, providing immediate visibility into WCAG compliance.
2. **Pair the live checker with a pre-submission validator** behind a feature flag, ensuring that users cannot publish non-compliant themes.
3. **Display a persistent, unignorable warning** (e.g., a red banner) when the theme does not meet WCAG standards, which disappears only when compliance is achieved.
4. **Monitor user engagement and drop-off rates** to refine the approach and find the optimal balance between compliance and usability.
5. **Conduct A/B testing** to compare the effectiveness of the hybrid approach with alternative methods, such as a standalone pre-submission block or live checker.
**What changed:** The decision evolved from a binary choice between a pre-submission block and a live checker to a hybrid approach that leverages the strengths of both methods.
