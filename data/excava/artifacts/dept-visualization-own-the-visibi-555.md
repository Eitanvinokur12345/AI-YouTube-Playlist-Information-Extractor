# visualization: Own the visibility AND ACCESSIBILITY of the whole interface — liveliness, info access, enj

> Decision artifact · room `dept-visualization-own-the-visibi-555` (dept) · 2026-07-10T03:22:37.481138+00:00
> Participants: Facet, Pane, Lumen · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Add live NVDA/JAWS screen-reader test to verify `aria-label="800×600 canvas"` is announced correctly before proceeding.

**Plan:**  
1. Open `src/vis/access.ts` and implement the focused test in `test/access.spec.ts` to verify keyboard tab order on the SVG root.  
2. Add assertions to `test/screen-reader.spec.ts` to confirm that NVDA/JAWS announce the `aria-label="800×600 canvas"` as expected.  
3. Run `npm test` to ensure all tests pass before moving forward.  
4. Use live testing with NVDA/JAWS to confirm the screen reader behavior during development.  
5. Once verified, seed `data/sample.json` with 20 mock records.

**What changed:** A live screen-reader test was mandated to ensure accurate announcements before proceeding with visualization development.
