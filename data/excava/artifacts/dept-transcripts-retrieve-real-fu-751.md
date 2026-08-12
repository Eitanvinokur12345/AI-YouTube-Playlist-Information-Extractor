# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-751` (dept) · 2026-08-12T03:07:07.313122+00:00
> Participants: Echo, Reel, Scriv · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run `kimtaeyoon83/mcp-server-youtube-transcript` on the first pending video to fetch its full transcript (timestamps, speaker IDs, text in ISO 8601 format).
2. Validate the output schema matches the four-field requirement.
3. Repeat steps 1–2 for the remaining 9 pending videos.
4. Store transcripts in a structured directory (e.g., `/transcripts/{video_id}.json`).
5. Log completion status (success/failure) for each video in a summary file.
6. Notify stakeholders upon full batch completion.

**What changed:** Action execution shifted from debate to systematic tool deployment.
