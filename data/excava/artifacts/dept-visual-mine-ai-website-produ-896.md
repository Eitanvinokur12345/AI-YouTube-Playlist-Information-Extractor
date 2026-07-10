# visual: Mine AI website/product DESIGNS (the look), taste-learn from Eitan's picks.

> Decision artifact · room `dept-visual-mine-ai-website-produ-896` (dept) · 2026-07-10T10:05:59.322258+00:00
> Participants: Easel, Squint, Chroma · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Clone the full `/design-references/eitan-picks/2024-q3/` directory into `mine-ai-designs/inspo/raw/` (127 files).
2. Generate a diff report (`file_id_audit.txt`) comparing `file_id` values in `taste_scores.csv` against actual filenames in `raw/`.
3. Manually validate any mismatches (missing/renamed files) and flag corrupt entries.
4. Only after audit completion, extract the top 10 designs using *our* team’s criteria (not the CSV’s scores).
5. Save curated selections to `mine-ai-designs/inspo/top-10/` with metadata (source file, audit status).
6. Archive raw files and diff report in `mine-ai-designs/inspo/audit/`.

**What changed:** Prioritized raw file validation over inherited CSV metrics to eliminate silent corruption risks.
