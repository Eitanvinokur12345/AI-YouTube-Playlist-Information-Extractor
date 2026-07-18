# [Lumen's initiative] Embed real-time contrast visibility directly into the canvas so designers see and fix issues as they work—not as a gate 

> visualization · task `lumen-s-initiative-embed-14937` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Embed real-time contrast visibility directly into the canvas by modifying the rendering pipeline to overlay contrast metrics on elements as they are edited, using existing design tool APIs and accessibility libraries.

**Steps:**
1. **Audit the canvas rendering pipeline** – Identify where element styles (fill, stroke, text) are applied in the codebase (e.g., `src/render/canvas.ts` or similar). Add a post-processing step to compute contrast ratios (WCAG 2.1 AA/AAA) for each visible element against its background.
2. **Integrate contrast overlay** – Use the tool’s plugin system (e.g., Figma Plugin API, Sketch’s `sketch-module-web-view`, or a custom Electron overlay) to inject a semi-transparent layer that:
   - Highlights elements with contrast < 4.5 (AA) in red, 4.5–7 (AAA) in yellow, and >7 in green.
   - Updates dynamically on style changes (debounced at 200ms).
3. **Expose contrast metrics in the UI** – Add a collapsible sidebar panel (e.g., `src/ui/contrast-panel.tsx`) showing:
   - A list of elements failing contrast, sorted by severity.
   - Quick-fix buttons to auto-adjust colors (e.g., using `chroma-js` or `tinycolor2`).
4. **Persist contrast checks in artifacts** – Save contrast results to the design file metadata (e.g., as a `contrast-audit.json` alongside the `.fig`/`.sketch` file) for review in version control.
5. **Add CLI validation for CI** – Create a Node.js script (`scripts/contrast-check.js`) that
