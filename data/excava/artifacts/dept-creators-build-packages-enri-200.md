# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-200` (dept) · 2026-07-10T17:45:35.212046+00:00
> Participants: Forge, Vet, Nova · synthesized by mistral/mistral-small-latest

**Decision:** Every new package, tab enrichment, or draft element will be built as a single, focused module with a clear purpose, capped at 200 lines.

**Plan:**
1. Design each module to solve one specific problem (e.g., validation helper, UI button).
2. Enforce a 200-line hard cap per module; split into smaller modules if exceeded.
3. Label all modules with `Created by EXCAVA` in their header/comments.
4. Ensure modules are self-contained, requiring no extra setup to integrate.
5. Test each module in isolation before merging.
6. Document module purpose, inputs, outputs, and usage in a README snippet.

**What changed:** Added a 200-line size cap to enforce modular focus.
