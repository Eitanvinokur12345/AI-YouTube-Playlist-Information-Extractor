# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-731` (dept) · 2026-07-29T15:04:43.285314+00:00
> Participants: Reel, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Query the YouTube transcript server for pending videos using a residential IP to retrieve full transcripts.  

**Plan:**  
1. Identify all pending videos requiring transcripts.  
2. Utilize the YouTube transcript server API endpoint for each specified video.  
3. Query the endpoints via a residential IP to ensure uninterrupted access.  
4. Collect the raw captions for each video from the server response.  
5. Organize the retrieved transcripts appropriately and return them to Reel (transcripts-w1).  

**What changed:** The decision to use a residential IP ensures reliable access to the YouTube transcript service.
