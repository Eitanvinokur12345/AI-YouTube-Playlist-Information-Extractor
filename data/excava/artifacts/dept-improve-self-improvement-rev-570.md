# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-570` (dept) · 2026-07-10T07:21:57.422293+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit prompts/engines/routing via runtime validation (unit tests + dry runs) to expose unsafe auto-apply candidates.  
**Plan:**  
1. Audit all files in the `/prompts/`, `/engines/`, and `/routing/` directories against the quality checklist.  
2. Implement unit tests to validate prompt-engine mapping in the `/routing/` layer, ensuring all mappings are correctly linked.  
3. Execute dry runs through the routing layer to capture output and identify any mapping discrepancies or silent failures.  
4. Review the last 50 commits in the `/engines/` directory to identify candidates for auto-apply, ensuring they align with validated mappings.  
5. Establish criteria for auto-apply safety that includes semantic checks to ensure no deprecated prompts or dead engines are used.  
**What changed:** Added a runtime validation focus to ensure all mappings are validated before applying changes.
