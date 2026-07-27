# Raise G8 Personal fit (68/100): 21% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-83565` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Systematically tag taste attributes in existing designs to raise G8 Personal fit from 68/100 to 80+/100 via manual curation + Arena learning.

**Steps:**
1. **Audit current designs**: Run `find ./designs -type f -name "*.png" -o -name "*.jpg" | wc -l` to count total designs. Compare against `grep -r "taste:" ./designs | wc -l` to confirm 21% tag rate.
2. **Batch tagging sprint**: Use `exiftool -overwrite_original -TagsFromFile @ -xmp:all <file>` to inject XMP taste tags into 30% of remaining designs (prioritize high-traffic/arena-learned files).
3. **Arena learning sync**: Export tagged designs to `arena_learning/input/` and run `python scripts/arena_learn.py --input ./arena_learning/input/ --model g8_vibe_v1` to update taste embeddings.
4. **Validation loop**: Manually review 10% of tagged designs with `feh ./designs/valid/` and adjust tags via `exiftool -xmp:taste+="<tag>" -overwrite_original <file>` based on NOSG (Next: taste beyond) feedback.

**Needs:**
- Access to `./designs/` directory with image files.
- `exiftool` installed (`brew install exiftool` or equivalent).
- `arena_learning.py` script in `./scripts/` with `g8_vibe_v1` model.
- NOSG taste guidelines file (`./nosg
