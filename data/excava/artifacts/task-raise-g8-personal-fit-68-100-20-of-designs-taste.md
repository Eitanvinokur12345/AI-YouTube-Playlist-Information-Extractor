# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-43771` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Leverage taste-tagged designs in existing repos, run Arena learning live on NOSG-wired data, and expand taste beyond current scope.

**Steps:**
1. **Audit taste-tagged designs:**
   - Run `find . -type f -name "*.png" -o -name "*.jpg" | grep -E "taste|tag" > taste_files.txt` to list candidates.
   - Manually verify 20% of files meet framing standards (e.g., `feh --auto-zoom taste_files.txt`).
   - Commit valid files to `designs/taste-tagged/` with `git mv` and update references.

2. **Set up Arena learning live:**
   - Install `arena-learning` via `pip install arena-learning` (or use Docker image `ghcr.io/arena-learning/arena:latest`).
   - Run `arena-learn --dataset nosg-wired --model resnet50 --epochs 10 --output models/nosg_taste_v1` with GPU flag if available.

3. **Expand taste beyond current scope:**
   - Scrape 50 high-res design images from `designspiration.net` (or `pinterest.com`) using `scrapy crawl taste_spider -o taste_new.json`.
   - Filter via `jq 'select(.score > 0.8)' taste_new.json > taste_filtered.json` and deduplicate with `fdupes -r taste_filtered.json`.
   - Add top 10% to `designs/taste-tagged/` with manual curation.

**Needs:**
- **Tools:** `feh`, `git`, `arena-learning`, `scrapy`, `
