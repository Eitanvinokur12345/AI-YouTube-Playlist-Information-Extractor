# Keep the Designs tab pure: designs only, live previews, taste-ranked

> visual · task `keep-the-designs-tab-pur-92118` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Implement a strict content filter for the Designs tab, ensuring only live previews and curated designs remain, ranked by aesthetic taste.

**Steps:**
1. **Audit existing content** – Run `find designs/ -type f \! -name "*.html" -o -name "*preview*"` to identify non-preview files (e.g., raw assets, unrendered designs).
2. **Automate cleanup** – Use a script (e.g., `scripts/clean_designs.sh`) to:
   - Delete non-HTML files (e.g., `.psd`, `.fig`, `.sketch`).
   - Move unrendered designs to `/archive/` (preserve but hide).
   - Keep only `.html` files with embedded previews (e.g., `<iframe src="live-preview">`).
3. **Enforce live previews** – Add a GitHub Action (`.github/workflows/validate_previews.yml`) to block PRs without:
   - A live preview URL (e.g., Vercel/Netlify deploy link in `README.md`).
   - A screenshot in `/screenshots/` (auto-generated via Puppeteer if missing).
4. **Taste-ranking system** – Add a `designs/.taste_rank` file with a 1–10 score per design, updated via PR review consensus (e.g., `git blame` tracks changes).
5. **Purge violations** – Run `git filter-repo --invert-paths --path designs/ --path-exclude "*.html"` to rewrite history, then force-push to `main`.

**Needs:**
- `git filter-repo` installed (`pip install git-filter
