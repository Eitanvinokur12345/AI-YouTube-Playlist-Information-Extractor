# Keep the Designs tab pure: designs only, live previews, taste-ranked

> visual · task `keep-the-designs-tab-pur-83565` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

**Approach:**
Enforce a strict "designs-only" policy on the Designs tab by automating validation, archiving non-conformant content, and ensuring live previews are taste-ranked via a curated system.

**Steps:**
1. **Audit Existing Content**
   - Run `find ./designs -type f \! -name "*.png" \! -name "*.jpg" \! -name "*.webp" -exec mv {} ./archived/non-designs/ \;` to move non-image files to an archive.
   - Use `grep -r "screenshot" ./designs --include="*.md"` to flag markdown files referencing screenshots; move them to `./archived/screenshot-references/`.

2. **Enforce Live Preview Requirement**
   - Add a GitHub Actions workflow (`.github/workflows/validate-designs.yml`) that:
     - Checks for `preview: true` in YAML frontmatter of each design file.
     - Fails if `preview` is missing or `false`, blocking merges to `main`.

3. **Taste-Ranking System**
   - Create `./designs/.taste_rank.yaml` with a list of approved curators (GitHub usernames).
   - Add a script (`scripts/rank_designs.py`) that:
     - Scrapes GitHub reactions (👍/👎) on design files.
     - Assigns a `taste_score` based on curator reactions (e.g., 👍 from curator = +2, 👎 = -1).
     - Updates `./designs/.taste_rank.yaml` with scores.

4. **Automated
