# [Lumen's initiative] Ship a live, minimal HTML/CSS demo of Excava’s core flow with mocked API data by tonight—visibility into real latency an

> visualization · task `lumen-s-initiative-ship--95183` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Deliver a minimal, self-contained HTML/CSS demo with mocked API responses to visualize Excava’s core flow, ensuring readability and instant comprehension.

**Steps:**
1. Create `index.html` with a clean, semantic structure (header, main flow diagram, footer) and minimal inline CSS for immediate readability.
2. Mock the API responses in a `<script>` block as `window.mockData` (JSON objects matching Excava’s expected schema) to simulate real latency with `setTimeout`.
3. Render the core flow using SVG `<path>` elements (no libraries) with CSS classes for color/stroke, bound to `mockData` via vanilla JS.
4. Add a live latency indicator (e.g., `<span id="latency">`) updated via `performance.now()` in the mock API calls.
5. Test locally with `python -m http.server 8000`, verify console for errors, and push to a public GitHub repo (e.g., `excava-demo`).

**Needs:**
- Local file system access (to create `index.html`, `style.css` if split).
- Browser (Chrome/Firefox) for testing.
- GitHub account + repo (`excava-demo`) for deployment.
- Excava’s core flow schema (from `dept-visualization-own-excava-s-o-883.md`) to define SVG paths/data bindings.
- Mock data structure (derive from schema or prior artifacts).
