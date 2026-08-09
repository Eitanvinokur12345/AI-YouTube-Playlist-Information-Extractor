# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-674` (dept) · 2026-08-08T21:02:30.699542+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
The transcripts task is approved and will be executed.

**Plan:**
1. Deploy `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos.
2. Configure the tool to run immediately with residential IP settings and gentle pacing.
3. Verify transcript generation for each video, ensuring full captions are retrieved.
4. Store transcripts in the designated repository with metadata (video ID, timestamp).
5. Log completion status for each video in the tracking system.
6. Notify Scriv upon full transcript collection for pending videos.

**What changed:** Transcripts will now be automatically fetched for all pending videos using the specified tool.
