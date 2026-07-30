# Keep the Designs tab pure: designs only, live previews, taste-ranked

> visual · task `keep-the-designs-tab-pur-42478` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Implement a strict filtering system to ensure the Designs tab only contains polished, live previews with curated aesthetics.

**Steps:**
1. **Audit existing designs** – Run `find ./designs -type f \\( -name "*.png" -o -name "*.jpg" -o -name "*.gif" \\) | wc -l` to count unfiltered assets. Delete or archive files failing taste criteria (e.g., low-res, unrendered mockups).
2. **Enforce live preview requirement** – Use a script to verify each design has a working URL (e.g., `curl -s -o /dev/null -w "%{http_code}" [URL] | grep -q "200"`). Remove entries without valid links.
3. **Taste-ranking system** – Implement a `designs/.taste_rank` file with manual scores (1-10) for each design. Add a `sort -k2 -nr` command to auto-sort the tab by rank.
4. **Automated cleanup** – Add a GitHub Action (`.github/workflows/designs-purge.yml`) to run steps 1-3 on `git push`, failing if new designs violate rules.
5. **Frame-worthy framing** – Replace thumbnails with high-res exports (e.g., `ffmpeg -i input.mp4 -vframes 1 -q:v 2 output.jpg`) and enforce 16:9 aspect ratio via `imagemagick`.

**Needs:**
- Access to the `designs/` directory in the repo.
- `curl`, `ffmpeg`, `imagemagick` installed in CI.
- GitHub Actions enabled
