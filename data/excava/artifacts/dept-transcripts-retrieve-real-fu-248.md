# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-248` (dept) · 2026-07-10T02:37:57.021390+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Verify caption reality before declaring transcripts missing.

**Plan:**
1. Scan the `/pending_videos/` directory and list all `.mp4` or `.mov` files using `ls -l`.
2. For each video file, run `ffprobe` to check for the presence of subtitle streams.
3. If subtitle streams ('s') exist, use `ffmpeg -f srt -` to attempt extracting the captions.
4. Manually check the generated `.srt` files to ensure they are not empty and contain valid content.
5. Document the results of each step to confirm the state of captions for each video.

**What changed:** The plan emphasizes verifying both the presence and content validity of captions rather than assuming they are available.
