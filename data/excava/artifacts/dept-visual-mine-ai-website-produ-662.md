# visual: Mine AI website/product DESIGNS (the look), taste-learn from Eitan's picks.

> Decision artifact · room `dept-visual-mine-ai-website-produ-662` (dept) · 2026-07-08T20:09:12.075481+00:00
> Participants: Easel, Squint, Chroma · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Validate Eitan’s design picks for accuracy and integrity before proceeding with cropping and selection.

**Plan:**
1. Audit Eitan’s raw design picks by running `head -n 5 /mine-ai/design-references/eitan-picks-2024-05-15.csv` to inspect the "taste score" column and its range.
2. Count the total number of entries in the data set with `wc -l`.
3. Ensure the normalization of the "taste score" values to verify if they are on a consistent scale.
4. Validate the aspect ratios of images using appropriate image analysis tools, not `ffprobe`, to avoid compatibility issues.
5. Create a new CSV file (`eitan-validated-refboard.csv`) with the validated columns: filename, taste_score (normalized), aspect_ratio, width, height, and a "validation_flag".

**What changed:** The decision shifted from immediate extraction to a thorough validation process to ensure data integrity.
