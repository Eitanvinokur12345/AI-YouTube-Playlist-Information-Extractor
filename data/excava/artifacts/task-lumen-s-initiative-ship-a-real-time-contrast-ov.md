# [Lumen's initiative] Ship a real-time contrast overlay that flags *only* the worst offenders in the canvas during changes, but blocks submiss

> visualization · task `lumen-s-initiative-ship--3861` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Implement a minimal real-time contrast overlay that highlights only the most severe contrast violations during canvas edits, without blocking submissive changes.

**Steps:**
1. **Add a WASM-based contrast analyzer** to the canvas editor (using `wasm-pack` to compile Rust to WASM) that scans changed regions for WCAG AAA failures (contrast < 4.5:1 for text).
2. **Overlay a semi-transparent red flash** (via CSS `::after` pseudo-element) only on the worst offenders (contrast < 3:1) for 1s after each edit, using `requestAnimationFrame` for smoothness.
3. **Integrate with the existing diff system** by patching the `onChange` handler in `src/editor.ts` to trigger the analyzer and overlay updates.
4. **Add a toggle in settings** (`localStorage` key `contrastOverlayEnabled`) to disable the feature without blocking submissive changes.
5. **Test in staging** by manually editing text with low contrast (e.g., `#000` on `#fff`) and verifying the overlay appears only for the worst cases.

**Needs:**
- Rust toolchain (`rustup`, `wasm-pack`) for contrast analyzer.
- Access to `src/editor.ts` and canvas diff system.
- CSS/JS environment for overlay rendering (existing build system).
- Test cases with known low-contrast text (e.g., `#000` on `#f0f0f0`).
```
