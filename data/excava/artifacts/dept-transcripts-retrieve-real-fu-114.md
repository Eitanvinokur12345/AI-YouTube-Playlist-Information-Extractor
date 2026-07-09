# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-114` (dept) · 2026-07-09T15:05:20.371776+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Select 10 TED Talk videos with verified transcripts from the TED corpus (IDs: `TED1`, `TED2`, ..., `TED10`).
2. For each video, run `yt-dlp --write-auto-sub --sub-langs en --output "transcripts/%(id)s.%(ext)s"` to generate auto-captions.
3. Download the verified transcripts from the TED corpus for the same videos.
4. Generate a side-by-side comparison report (TED Talk ID, yt-dlp output, verified transcript, line-level diffs, error rate %).
5. Calculate the average error rate across all 10 videos to determine transcript reliability.
6. If the error rate is ≤5%, proceed with the residential IP scrape for pending videos; otherwise, refine the verification method.

**What changed:** Verification now requires blind cross-check against TED Talks’ verified corpus before any residential IP scrape.
