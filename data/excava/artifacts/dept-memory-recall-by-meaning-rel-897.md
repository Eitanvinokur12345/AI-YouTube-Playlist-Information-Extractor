# memory: Recall by meaning, relate elements, build the brain graph, embed unembedded elements.

> Decision artifact · room `dept-memory-recall-by-meaning-rel-897` (dept) · 2026-07-09T23:49:40.296303+00:00
> Participants: Graft, Prune, Root · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit `/memory/` by semantic age and link integrity for all `.txt`/`.md` files.

**Plan:**
1. Use `find . -type f \( -name "*.txt" -o -name "*.md" \)` to gather all relevant files.
2. Extract semantic timestamps using `git log` or `stat -c %Y` for file modification times.
3. Check each file for link integrity, identifying broken links and circular references.
4. Score each file on a quality scale (0-1) based on link status and age.
5. Rank the top 5 oldest files by meaningful age, including paths, mtime, link status, and quality score.

**What changed:** Focus shifted from raw counts to a comprehensive audit that assesses both age and quality.
