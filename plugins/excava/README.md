# EXCAVA — preserved, disconnected

EXCAVA is retained as a candidate for a future optional plugin. It is not the main product, is not loaded by the dashboard, and has no active GitHub workflow.

- `src/`: original OS source, moved without changing its blobs.
- `workflows/`: original workflows, outside GitHub's active workflow directory.
- `ui/`: complete original dashboard shell and script, with the factory floor.
- Existing `data/excava/` and other historical data remain unchanged.

The independent core reads Element/Package data through `src/library.py`, and enriches sources through stateless `src/analysis_engines.py`. Neither imports or starts EXCAVA. Package reads still include the historical package store so existing kits remain available.

This is preserved source, **not an installable plugin yet**. Its historical `src.*` imports and repository-relative paths must be adapted before reactivation. A future adapter needs isolated imports/state, an explicit opt-in lifecycle and permissions, and separate activation tests. Do not restore its workflows as a shortcut.

Original snapshot: ee12b15a444b037ae42cb163b894468df4af7254.
