# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-239` (dept) · 2026-07-10T10:04:36.761723+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `pipdeptree -p --json > /repo/analysis/dep_tree.json` to generate a static dependency graph, including transitive imports and C extensions.
2. Capture runtime imports dynamically using `sys.monitoring` hooks (filtering `import` events) and log all loaded modules to `/repo/analysis/runtime_imports.log`.
3. Parse Python source files with `ast` to extract conditional imports (`if`/`else`), dynamic imports (`importlib.import_module`), and entry-point plugins (via `entry_points()`).
4. Cross-validate static (`pipdeptree`) and dynamic traces against runtime logs, flagging discrepancies (e.g., missing conditional/entry-point imports).
5. Enrich analysis with `/repo/pyproject.toml` and `/repo/setup.cfg` to resolve hidden configs (e.g., `pkg_resources`, `setup.py` aliases).
6. Generate a unified report (`/repo/analysis/import_analysis.md`) summarizing static vs. runtime discrepancies.

**What changed:** Added runtime tracing (`sys.monitoring` + AST) to complement static dependency analysis.
