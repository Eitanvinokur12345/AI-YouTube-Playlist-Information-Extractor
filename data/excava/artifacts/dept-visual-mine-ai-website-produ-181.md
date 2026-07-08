# visual: Mine AI website/product DESIGNS (the look), taste-learn from Eitan's picks.

> Decision artifact · room `dept-visual-mine-ai-website-produ-181` (dept) · 2026-07-08T17:19:06.641938+00:00
> Participants: Easel, Squint, Chroma · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Lock wget to mineai.com with `--span-hosts-allow mineai.com` and pre-filter HTML for external URLs before scraping.

**Plan:**
1. Create a local folder for Eitan's picks: `mkdir eitan-picks && cd eitan-picks`.
2. Use `wget -r -l 2 -nd -D mineai.com --span-hosts-allow mineai.com https://mineai.com/eitan/picks/` to download all relevant images.
3. Pre-filter the HTML to exclude external URLs before scraping, ensuring all resources are on-site.
4. Generate clean metadata by running `exiftool -csv -r -ext png -ext jpg -ext jpeg -ext svg eitan-picks/ > eitan-picks-meta.csv`.
5. Verify the integrity of the downloaded assets and metadata.

**What changed:** Wget command and filtering process were refined to ensure only on-site assets are captured.
