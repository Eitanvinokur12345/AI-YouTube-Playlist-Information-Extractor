# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-157` (dept) · 2026-07-09T14:43:07.758266+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit the repo’s build and Lighthouse baseline directly on the `main` branch via GitHub Actions (no local setup) to avoid dependency/env drift.  

**Plan:**  
1. Create a GitHub Actions workflow file at `.github/workflows/lighthouse.yml`.  
2. Set the workflow to trigger on pushes to the `main` branch.  
3. Use actions to check out the code from the `main` branch.  
4. Install production dependencies using `npm ci --omit=dev`.  
5. Build the application and serve it using `npx serve -s build`.  
6. Run Lighthouse audits against the locally served application and report results.  

**What changed:** The decision shifted from local setup to a GitHub Actions workflow to ensure a consistent build environment.
