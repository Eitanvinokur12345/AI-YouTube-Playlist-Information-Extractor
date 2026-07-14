# [Lumen's initiative] Ship a live HTML/CSS prototype tonight with mocked API responses to test performance and responsiveness; the design team

> visualization · task `lumen-s-initiative-ship--96359` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Deliver a minimal, responsive HTML/CSS prototype with mocked API responses to validate performance and responsiveness before integrating real endpoints.

**Steps:**
1. **Initialize project**
   ```bash
   mkdir lumen-prototype && cd lumen-prototype
   git init
   npm init -y
   touch index.html styles.css mock-api.js
   ```

2. **Build static prototype**
   - Write `index.html` with semantic HTML, minimal CSS in `styles.css` (mobile-first, flex/grid).
   - Add mocked API responses in `mock-api.js` (e.g., `fetch('/api/data')` returns static JSON).
   - Test locally:
     ```bash
     npx serve
     ```

3. **Validate responsiveness**
   - Use Chrome DevTools (device toolbar) to test breakpoints (320px, 768px, 1024px).
   - Check Core Web Vitals (Lighthouse) via:
     ```bash
     npx lighthouse http://localhost:3000 --output=html --output-path=./report.html
     ```

4. **Commit & share**
   ```bash
   git add .
   git commit -m "Initial prototype with mocked API"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

**Needs:**
- Local dev environment (Node.js, npm).
- Browser (Chrome/Firefox) for testing.
- Optional: GitHub repo for version control.
