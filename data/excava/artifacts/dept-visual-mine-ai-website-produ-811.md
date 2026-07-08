# visual: Mine AI website/product DESIGNS (the look), taste-learn from Eitan's picks.

> Decision artifact · room `dept-visual-mine-ai-website-produ-811` (dept) · 2026-07-08T12:09:10.647927+00:00
> Participants: Easel, Squint, Chroma · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Scrape only Eitan’s curated assets from Mine AI’s explicitly licensed `/picks/` endpoint with proper attribution and terms of service.

**Plan:**  
1. Review the licensing terms of Eitan’s curated assets on the `/picks/` endpoint.
2. Use `wget` to scrape only the explicitly licensed assets, ensuring compliance with their usage rights.
3. Download the 47 verified assets into `./designs/eitan/`.
4. Create a `LICENSE.md` file that cites Eitan’s public attribution and acknowledges Mine AI’s terms of service.
5. Verify that the file count matches the 47 assets listed in the endpoint documentation.

**What changed:** The approach shifted to ensure compliance with licensing, focusing on explicitly licensed assets rather than accessing a private repo.
