# [Lumen's initiative] Ship one live HTML/CSS demo of Excava’s core flow with mocked API data via VeriTeknik proxy *and* one Figma clickable pr

> visualization · task `lumen-s-initiative-ship--93003` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Deliver a minimal, live HTML/CSS prototype of Excava’s core flow using mocked API data served through VeriTeknik proxy, plus a clickable Figma prototype.

**Steps:**
1. Clone the VeriTeknik proxy repo (`veriteknik-proxy`) and verify proxy config supports `/excava/api/*` routing.
2. Create `/excava/demo/` dir in project; write `index.html`, `style.css`, and `mock-api.js` with static JSON responses matching Excava’s core endpoints.
3. Run proxy locally (`npm run dev`), serve demo at `http://localhost:3000/excava/demo`, confirm mocked data loads.
4. Export Figma file (`excava-core-flow.fig`) with frames for each core screen (login, dashboard, detail view); add interactive hotspots linking frames.
5. Publish Figma prototype (share link) and push HTML/CSS/JS to `veriteknik-proxy/excava/demo/`; verify live demo works via proxy.

**Needs:**
- Access to `veriteknik-proxy` repo (GitHub).
- Figma file access (`excava-core-flow.fig`).
- Node.js/npm for proxy dev server.
- Excava core flow screenshots/wireframes (for mock data structure).
```
