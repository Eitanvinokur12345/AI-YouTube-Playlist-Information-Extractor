# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-57860` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Taste-tag 20% of designs via manual curation + Arena live feedback, then wire NOSG for taste propagation.

**Steps:**
1. **Tag 20% of designs**
   - Run `find ./designs -type f -name "*.png" -o -name "*.jpg" | shuf -n $(( $(wc -l < <(find ./designs -type f \( -name "*.png" -o -name "*.jpg" \))) * 20 / 100 )) > taste_tag_list.txt`
   - For each file in `taste_tag_list.txt`, open in `feh --scale-down --title "Taste Tag: [filename]" [file]` and append tags to `taste_tags.csv` (format: `filename,tag1,tag2,...`).

2. **Arena learning live**
   - Launch Arena server: `python arena.py --port 8000 --data taste_tags.csv --model nosg_v1`
   - Open `localhost:8000` in browser; rate 50 pairs of designs (A/B) via `arena_client.py --mode rate --pairs 50`.

3. **NOSG taste propagation**
   - Train NOSG model: `python nosg_train.py --tags taste_tags.csv --epochs 100 --output nosg_v2.pkl`
   - Validate: `python nosg_validate.py --model nosg_v2.pkl --test 0.2`
   - Deploy: `cp nosg_v2.pkl ./models/active/`

**Needs:**
- `feh` (image viewer)
-
