# visual: Mine AI website/product DESIGNS (the look), taste-learn from Eitan's picks.

> Decision artifact · room `dept-visual-mine-ai-website-produ-111` (dept) · 2026-07-10T03:22:32.767337+00:00
> Participants: Easel, Squint, Chroma · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Pull Eitan’s picks via a single-page dry-run with strict file-type/size filters, hash duplicates, and log 404s before proceeding.

**Plan:**
1. Execute a dry-run using `wget -r -l 1 -nd -H -A.png,.jpg,.jpeg,.svg https://eitanspicks.com/gallery/123` to test a single gallery page.
2. Analyze the dry-run output for file count, total size, and any encountered 404 errors or tracking pixels.
3. Implement hash checks to identify and eliminate duplicate files from the downloaded assets.
4. Review and document the results of the dry-run before deciding whether to proceed with a broader asset pull.
5. If approved based on the dry-run, execute the full download, saving assets in a dedicated folder with timestamps.

**What changed:** The approach now emphasizes careful inspection and validation of files before any extensive downloads.
