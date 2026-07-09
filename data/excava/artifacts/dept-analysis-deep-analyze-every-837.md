# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-837` (dept) · 2026-07-09T14:41:36.649440+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `grep -r "protocol" --include="*.scala" --include="*.java" . | wc -l` to count all protocol mentions across the entire repo.
2. Filter for code-only hits (exclude comments) using `grep -r "protocol" --include="*.scala" --include="*.java" . | grep -v "//" | grep -v "/*" | wc -l`.
3. Cross-reference protocol mentions with "error" and "state" in the same files via `grep -r -l "protocol" --include="*.scala" --include="*.java" . | xargs grep -l "error\|state" | wc -l`.
4. Generate AST/dependency graph (e.g., `scalac -Xprint:typer` or `jdeps` for Java) to map protocol mentions to critical paths.
5. Manually validate top 10% most frequent files for false positives (e.g., comments, tests).
6. Synthesize findings into a ranked list of protocol-critical components.

**What changed:** Shifted from file-counting to context-aware, code-only protocol analysis with static validation.
