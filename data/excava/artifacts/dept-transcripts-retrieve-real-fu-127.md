# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-127` (dept) · 2026-08-07T19:32:51.790845+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Reel executes `kimtaeyoon83/mcp-server-youtube-transcript` on the pending video tagged “r.”
2. Verify the tool’s residential IP capability (e.g., via logs or tool documentation).
3. If residential IP is confirmed, proceed with transcript/caption retrieval.
4. If residential IP is not confirmed, switch to an alternative method (e.g., manual download or API fallback).
5. Store the retrieved transcript/captions in the designated repository.
6. Mark the video as processed in the tracking system.

**What changed:** Tool execution is now contingent on confirming residential IP capability.
