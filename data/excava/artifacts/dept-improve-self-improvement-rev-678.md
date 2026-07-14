# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-678` (dept) · 2026-07-14T02:58:13.388104+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Implement a hybrid scan approach that combines exact string matching with light semantic review, ensuring it captures both exact and near-duplicates, while measuring duplicate impact based on task-relative value.

**Plan:**
1. Develop an automated system that conducts weekly scans of all prompts using exact string matching.
2. Integrate a light semantic review process to identify near-duplicates missed by exact matching.
3. Implement a task-relative value measurement framework to assess the impact of duplicates based on prompt usage in production.
4. Monitor and adjust the hybrid system to minimize false positives during the semantic review process.
5. Regularly review the effectiveness of the hybrid approach and make necessary refinements based on findings.

**What changed:** The decision incorporates a comprehensive strategy for prompt review to enhance accuracy and relevance while managing complexity effectively.
