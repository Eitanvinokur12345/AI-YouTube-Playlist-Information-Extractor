# transcripts: Retrieve REAL full transcripts/captions for pending videos (residential IP; gentle pacing)

> Decision artifact · room `dept-transcripts-retrieve-real-fu-670` (dept) · 2026-07-10T03:44:17.832664+00:00
> Participants: Reel, Scriv, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Reel must fetch full `whois` + ASN proof for each resolved IP (IPv4/IPv6) from direct endpoints, confirming residential ISP ownership before transcription.

**Plan:**
1. Scan the pending videos queue to identify the top 5 untranscribed files with `.mp4` or `.mov` extensions.
2. Use `youtube-dl --get-url` to resolve the top 3 video URLs to their direct endpoints.
3. For each resolved endpoint, extract the IP address using `curl` and query the full `whois` output for the IP.
4. Verify that the ASN and orgname from the `whois` results match a residential ISP (e.g., ASN 7922 for Comcast).
5. Queue the valid video URLs for transcription only if they meet the residential ISP criteria.

**What changed:** The need for comprehensive ASN verification and proof of residential ISP ownership was established.
