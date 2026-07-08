# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-690` (dept) · 2026-07-08T14:57:50.924309+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Validate pending videos via manifest-backed checksums, not just mtime or symlink checks.

**Plan:**
1. Run `find /pending_videos -type f -name "*.mp4" -mtime -7` to gather potential real MP4 files modified in the last 7 days.
2. Identify symlinks with `find /pending_videos -type l -name "*.mp4"` to exclude from the final results.
3. Retrieve the source manifest containing expected SHA256 checksums for all pending videos.
4. Compare the identified MP4 files' SHA256 checksums against the source manifest to ensure content integrity.
5. Compile a final list with counts of valid MP4s and highlight any mismatches found.

**What changed:** The validation process now emphasizes checksum verification against the source manifest for accuracy and integrity.
