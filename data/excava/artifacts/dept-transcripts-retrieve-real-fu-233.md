# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-233` (dept) · 2026-07-09T22:00:49.009999+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Create a stable snapshot of `/pending/videos/` using `rsync -a --link-dest` to `/snapshots/videos_YYYYMMDD_HHMMSS/` (timestamped directory).
2. Generate an `md5sum` manifest of the snapshot contents (`find /snapshots/videos_YYYYMMDD_HHMMSS/ -type f -exec md5sum {} + > /tmp/videos_snapshot.md5sums`).
3. Verify the snapshot’s integrity by comparing the manifest against the original directory’s checksums (if pre-existing).
4. Parse the snapshot for `.mp4` files and symlinks using `find /snapshots/videos_YYYYMMDD_HHMMSS/ -type f -name "*.mp4" -o -type l`.
5. Queue the first 5 valid `.mp4` files from the snapshot for processing.
6. Log the snapshot path and checksum manifest for audit.

**What changed:** Added a locked snapshot step to prevent live-mount drift before parsing.
