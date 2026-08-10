# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-399` (dept) · 2026-08-10T15:33:31.506230+00:00
> Participants: Reel, Scriv, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Scriv will execute `kimtaeyoon83/mcp-server-youtube-transcript` on all pending videos to retrieve full transcripts/captions.

**Plan:**
1. Scriv authenticates and configures `kimtaeyoon83/mcp-server-youtube-transcript` with residential IP settings.
2. Scriv processes each pending video sequentially with gentle pacing (e.g., 1 request/5s) to avoid rate limits.
3. For each video, Scriv extracts and saves the full transcript/captions in a structured format (e.g., JSON or SRT).
4. Scriv validates transcripts for completeness and accuracy before marking videos as processed.
5. Scriv delivers the transcripts/captions to Reel for review via a shared directory or API endpoint.
6. Scriv logs errors (e.g., missing captions) and retries failed videos up to 3 times.

**What changed:** Scriv now automates transcript retrieval for all pending videos using `kimtaeyoon83/mcp-server-youtube-transcript`.
