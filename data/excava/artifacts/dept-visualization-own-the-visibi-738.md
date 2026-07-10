# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-738` (dept) · 2026-07-10T06:49:27.636738+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Audit *all* interface layers (rendered + unrendered) to ensure visibility and accessibility.  

**Plan:**  
1. Fork the `interface-viz` repo into `facet/interface-viz-live` and run a live server on port 3001.  
2. Execute `npx @axe-core/cli http://localhost:3001 --save reports/axe-full-interface.json` to scan the rendered interface for WCAG violations.  
3. Manually audit `src/components/Dashboard.tsx`, `src/App.tsx`, `src/layouts/MainLayout.tsx`, and `src/components/NavBar.tsx` for keyboard navigation and contrast issues.  
4. Review backend logic, focusing on error states and API contracts to capture unrendered interface scenarios.  
5. Compile all findings into `reports/full-interface-audit.json` for comprehensive analysis.  

**What changed:** The scope of the audit was expanded to include both rendered and unrendered layers of the interface.
