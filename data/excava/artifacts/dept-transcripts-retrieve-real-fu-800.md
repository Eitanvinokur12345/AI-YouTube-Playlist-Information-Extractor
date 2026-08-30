# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-800` (dept) · 2026-08-30T03:22:21.379545+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Use kimtaeyoon83/mcp-server-youtube-transcript for transcript retrieval.

**Plan:**
1. Scriv executes kimtaeyoon83/mcp-server-youtube-transcript on each pending video to fetch full transcripts.
2. Store retrieved transcripts in the offline Deepgram cache for all 200k clips.
3. Verify transcript accuracy against original video content.
4. Log failures for manual review if transcripts are incomplete or missing.
5. Update pipeline documentation to reflect the new transcript source.
6. Monitor performance and adjust batch processing limits as needed.

**What changed:**
Replaced Deepgram real-time service with kimtaeyoon83/mcp-server-youtube-transcript for transcript retrieval.
