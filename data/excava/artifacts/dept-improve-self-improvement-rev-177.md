# improve: Self-improvement: review prompts/engines/routing/own-code; auto-apply safe changes; pitch 

> Decision artifact · room `dept-improve-self-improvement-rev-177` (dept) · 2026-07-10T03:56:28.487447+00:00
> Participants: Sprocket, Gauge, Ratchet · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Switch to a semantic-aware static analyzer to catch logical regex/path/context risks, then auto-patch only provably safe fixes.  

**Plan:**  
1. Implement semgrep rules to identify potentially brittle regex patterns in the codebase.  
2. Create semgrep rules to detect hardcoded paths that should be configurable.  
3. Establish rules for identifying missing configuration gaps related to environment and paths.  
4. Run the semantic analysis and collect evidence of potential risks before applying any patches.  
5. Draft pre/post-patch diff reports to document and verify the safety of changes.  

**What changed:** The approach will now prioritize semantic analysis over syntactic filtering to enhance code robustness.
