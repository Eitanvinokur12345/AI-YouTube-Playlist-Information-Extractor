# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-125` (dept) · 2026-07-09T04:00:27.722821+00:00
> Participants: Ratchet, Sprocket, Gauge · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit prompts.js routing with full branch coverage (lcov.info) before any refactor.  

**Plan:**  
1. Run `npm test -- --coverage --collectCoverageFrom='src/routing/prompts.js'` to obtain the comprehensive coverage report.  
2. Extract the exact branch coverage percentage for `prompts.js` from `lcov.info`.  
3. Identify and list all untested conditional branches within `prompts.js` (e.g., `env==='prod'`).  
4. Confirm that no side effects exist in the production routing logic before proceeding with any refactor.  
5. Consolidate redundant handlers based on the findings from steps 2 and 3, ensuring to apply only safe changes.  

**What changed:** The plan explicitly prioritizes obtaining complete branch coverage information and verifying side effects before any code modifications.
