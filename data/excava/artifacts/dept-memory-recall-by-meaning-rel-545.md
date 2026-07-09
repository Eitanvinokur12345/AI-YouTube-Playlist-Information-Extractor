# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-545` (dept) · 2026-07-09T04:00:34.442837+00:00
> Participants: Root, Graft, Prune · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit only non-WIP, text-based files for `@unembed` tags, then triage by content density before manual embedding.

**Plan:**  
1. Run `grep -R --exclude-dir={.git,.vscode,.github} -n "@unembed" . | grep -v "WIP\|draft\|temp"` to filter `@unembed` tags in non-WIP files.  
2. Generate a filtered list of `@unembed` instances including file name, line number, and snippet.  
3. Compute content density by counting lines of actual notes versus boilerplate for identified files.  
4. Use a triage rubric (e.g., "≥30% notes → embed") to prioritize files for manual embedding.  
5. Open and inspect candidate files in VS Code based on triage results to manually embed notes.  

**What changed:** Shifted focus from raw file length to content density for effective embedding strategy.
