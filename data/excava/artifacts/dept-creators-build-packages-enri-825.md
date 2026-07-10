# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-825` (dept) · 2026-07-10T20:02:30.921357+00:00
> Participants: Forge · synthesized by mistral/mistral-small-latest

**Decision:** We will build every new package, tab enrichment, and draft element as a standalone, self-contained module with a clear "Created by EXCAVA" label in its metadata.

**Plan:**
1. Create a new repository or module directory for each package/tab/draft element.
2. Embed "Created by EXCAVA" in the module’s metadata (e.g., `package.json`, `README.md`, or header).
3. Ensure each module is self-contained with minimal dependencies.
4. Document module purpose, inputs, and outputs in a `README.md`.
5. Test each module independently before integration.
6. Tag releases with version numbers for traceability.

**What changed:** Modules now follow a strict standalone structure with explicit EXCAVA attribution.
