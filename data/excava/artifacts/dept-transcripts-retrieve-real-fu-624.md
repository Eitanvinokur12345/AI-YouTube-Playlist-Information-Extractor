# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-624` (dept) · 2026-07-29T11:05:53.463892+00:00
> Participants: Reel · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Retrieve the full transcripts for pending videos using the designated server and method.

**Plan:**  
1. Identify all pending video IDs that require transcripts.  
2. Use residential IP to query the YouTube transcript server (`kimtaeyoon83/mcp-server-youtube-transcript`).  
3. Implement gentle pacing in the query requests to avoid server overload.  
4. Collect and compile the retrieved transcripts into a structured format.  
5. Ensure that all retrieved transcripts are reviewed for accuracy and completeness.  

**What changed:** The method of retrieval using residential IP and gentle pacing was confirmed as the preferred approach.
