# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-638` (war) · 2026-07-10T06:58:15.181068+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Reject all prior plans; artifact must contain a task-relative link impact map (critical vs. trivial) with proof that patching low-coverage files moves the bus task forward.  
**Plan:**  
1. Generate a comprehensive link impact map categorizing links as critical or trivial across all relevant files.  
2. Analyze the current coverage metrics and identify which files contribute to the 31.6% missing coverage, focusing on high-impact files outside `docs/guides/*.md`.  
3. Conduct a manual audit on the identified low-coverage files to assess their content and necessity for additional links.  
4. Validate that changing low-coverage files will have a meaningful impact on overall link coverage towards the 100% goal.  
5. Present findings and justifications for any proposed link additions or changes based on the analysis.  
**What changed:** The decision underscores the need for a more structured and evidence-based approach to link coverage improvement rather than arbitrary patching.
