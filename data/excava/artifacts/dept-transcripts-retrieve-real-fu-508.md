# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-508` (dept) · 2026-07-31T12:41:15.761883+00:00
> Participants: Reel · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Retrieve full transcripts/captions for pending videos using a residential IP and gentle pacing.
1. **Query YouTube transcript server**: Use `kimtaeyoon83/mcp-server-youtube-transcript` to request the transcript.
2. **Configure residential IP**: Set up the system to use a residential IP for the query.
3. **Implement gentle pacing**: Ensure the query is sent at a gentle pace to avoid overwhelming the server.
4. **Handle query response**: Parse the response from the YouTube transcript server.
5. **Save transcript**: Store the retrieved transcript/captions for the pending video.
**What changed:** The approach to retrieving transcripts now utilizes a residential IP and gentle pacing.
