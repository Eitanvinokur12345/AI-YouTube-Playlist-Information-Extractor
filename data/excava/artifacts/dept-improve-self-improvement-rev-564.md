# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-564` (dept) · 2026-07-31T03:11:33.897397+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run a blind A/B test to compare the effectiveness of 7-day hard decay and 30-day tiered decay in improving self-improvement.
1. **Split System**: Divide the system into two equal halves, with one half implementing a 7-day hard decay rule and the other half implementing a 30-day tiered decay rule.
2. **Tagging and Tracking**: Ensure that both halves of the system have the capability to tag prompts as "legacy" or "experimental" for manual renewal, but do not apply this tagging in the 7-day decay half.
3. **Measurement**: Measure misroute rates and prompt churn in both halves of the system over one full cycle.
4. **Comparison**: Compare the results from both halves to determine which decay rule is more effective in cutting clutter without losing edge cases.
5. **Implementation**: Implement the more effective decay rule system-wide based on the results of the A/B test.
**What changed:** The approach to improving self-improvement shifted from immediately implementing a decay rule to testing and comparing different decay rules through a blind A/B test.
