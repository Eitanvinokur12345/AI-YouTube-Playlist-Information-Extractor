# analysis: Deep-analyze every element from its FULL source (whole transcript/repo) + enrich from >=1 

> Decision artifact · room `dept-analysis-deep-analyze-every-126` (dept) · 2026-08-28T02:36:52.785046+00:00
> Participants: Chisel, Sift, Marrow · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Update the ingestion team's zero-speech filter to classify videos as "silent" if they contain corrupted audio or non-speech audio (e.g., noise, unintelligible speech).
2. Route all "silent" flagged videos directly to curation to prevent wasted analysis cycles.
3. Document the updated criteria for "silent" flagging in the ingestion pipeline’s operational guidelines.
4. Conduct a test batch to validate that the new filter correctly identifies and routes corrupted/non-speech audio videos.
5. Notify the ingestion and curation teams of the change and provide training on the updated criteria.
6. Monitor pipeline efficiency post-implementation to ensure no false positives or missed detections.

**What changed:** The zero-speech filter now includes corrupted and non-speech audio in the "silent" classification for routing to curation.
