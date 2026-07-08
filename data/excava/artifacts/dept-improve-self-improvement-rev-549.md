# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-549` (dept) · 2026-07-08T17:17:39.654324+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Proceed with semantic diff vs best-practice baselines to surface stale/unsafe logic, then auto-apply only rule-verified safe tweaks.

**Plan:**
1. Perform a semantic diff audit of prompts/engines/routing files against established best-practice baselines.
2. Identify stale or potentially unsafe logic within those files based on the audit results.
3. Create a checklist of auto-apply rules derived from best practices to ensure safety and relevance of changes.
4. Implement the verified safe tweaks in a controlled manner, ensuring thorough testing before deployment.
5. Document the process and findings for future reference and improvement.

**What changed:** The focus shifted from merely counting files and recent changes to a comprehensive semantic analysis of code against best-practice benchmarks.
