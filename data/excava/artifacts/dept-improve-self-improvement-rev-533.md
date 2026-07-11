# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-533` (dept) · 2026-07-11T06:38:59.826514+00:00
> Participants: Sprocket · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** We will auto-apply only the safest class of changes to our prompts, engines, routing, and own code.

**Plan:**  
1. Implement a review system to categorize changes as 'safe' (additive) or 'structural' (logic changes, refactors).  
2. Develop an auto-application tool for identified safe changes, ensuring they are additive only.  
3. Establish a human review process for all structural edits, creating a feedback loop for future improvements.  
4. Create documentation guidelines for logging the nature of changes made and ensuring clarity in communication.  
5. Regularly evaluate the effectiveness of this approach and adjust the categorization criteria based on outcomes.

**What changed:** The focus is now on limiting auto-application to only additive changes for safety.
