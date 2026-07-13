# [Lumen's initiative] Build a medium-fidelity HTML/CSS demo of Excava’s riskiest flows—live, not polished—then measure real screentime to expo

> visualization · task `lumen-s-initiative-build-35911` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Build a live, medium-fidelity HTML/CSS demo of Excava’s riskiest flows, then measure real screentime via a lightweight tracking script.

**Steps:**
1. **Identify riskiest flows** – Extract from `data/excava/artifacts/dept-visualization-own-excava-s-o-926.md` (e.g., high-error, high-abandonment, or critical path steps).
2. **Scaffold demo** – Create `excava-risky-flows-demo.html` (inline CSS/JS) with minimal structure:
   - Static HTML skeleton (no framework).
   - CSS in `<style>` (medium fidelity: semantic classes, no animations).
   - JS in `<script>` (mock interactions for flows, e.g., form submissions, navigation).
3. **Add screentime tracking** – Insert a lightweight script (e.g., `track.js`) to log:
   - `visibilitychange` events (tab focus).
   - `click`/`submit` events on risky elements (capture `data-*` attributes).
   - Store timestamps in `localStorage` (no backend).
4. **Test locally** – Open in browser, verify:
   - Flows render as expected.
   - Tracking logs to console (`console.table` for readability).
5. **Deploy** – Push to a static host (e.g., GitHub Pages, Netlify) with a public URL for real-world testing.

**Needs:**
- **Access:** Read `data/excava/artifacts/dept-visualization-own-excava-s-o-926.md` (or its content provided).
- **Tools:** Text editor (VS Code), browser (Chrome/Firefox
