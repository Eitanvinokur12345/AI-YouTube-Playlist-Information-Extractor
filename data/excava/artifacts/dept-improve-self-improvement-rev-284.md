# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-284` (dept) · 2026-08-16T14:10:26.260596+00:00
> Participants: Sprocket, Gauge, Overhaul, Ratchet · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Run PR-Agent in shadow mode on merged PRs only for two weeks to validate edge cases without polluting active review signals.
1. **Implement PR-Agent in shadow mode**: Run PR-Agent on merged PRs to start collecting data.
2. **Monitor and analyze results**: Track the performance and output of PR-Agent for two weeks to identify edge cases and patterns.
3. **Refine PR-Agent based on findings**: Use the insights gathered to refine PR-Agent's autofeedback and reduce potential noise.
4. **Assess impact on reviewer behavior**: Evaluate whether reviewers are effectively utilizing autofeedback without being desensitized to it.
5. **Review and adjust the approach**: After the two-week period, review the effectiveness of the approach and adjust as necessary to optimize results.
**What changed:** The PR-Agent is now running in shadow mode on merged PRs only, ensuring a clean signal and avoiding noise in active reviews.
