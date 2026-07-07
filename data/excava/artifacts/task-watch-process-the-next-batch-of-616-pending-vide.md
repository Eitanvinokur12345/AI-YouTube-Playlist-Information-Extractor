# Watch: process the next batch of 616 pending videos

> watch · task `watch-process-the-next-b-46085` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Process the 616 pending videos in batches using FFmpeg for metadata extraction and validation, then apply the given `[cost 30/steps 40/risk 10]` constraints.

**Steps:**
1. **List pending videos** – Run `ls -1 pending/*.mp4 > pending_list.txt` to generate a file with all 616 video paths.
2. **Batch process metadata** – Use `ffprobe -v error -show_entries format=duration,size,codec_name -of default=noprint_wrappers=1:nokey=1 -i "{file}" >> metadata.csv` in a loop over `pending_list.txt` to extract duration, size, and codec.
3. **Filter by constraints** – Run `awk -F, '$2 < 29e6 && $3 == "h264" {print $1}' metadata.csv > filtered_list.txt` to retain only videos matching `size=29(small)` and `codec=h264`.
4. **Validate count** – Confirm `wc -l filtered_list.txt` outputs `65` (expected size).
5. **Apply risk mitigation** – For each file in `filtered_list.txt`, run `ffmpeg -i "{file}" -c copy -f null - 2> "{file}.risk.log"` to log potential corruption without re-encoding.

**Needs:**
- `ffmpeg` and `ffprobe` installed (v4.4+).
- `pending/` directory containing 616 `.mp4` files.
- Write permissions in `pending/` and output directory.
- Bash/awk for scripting.
```
