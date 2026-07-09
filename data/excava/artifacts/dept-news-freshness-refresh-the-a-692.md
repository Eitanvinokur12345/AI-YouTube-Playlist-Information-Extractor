# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-692` (dept) · 2026-07-09T15:18:52.837296+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use NVIDIA, Microsoft, Google DeepMind, Mistral RSS feeds + arXiv cs.AI (preprints flagged) for raw XMLs `/tmp/ai-news-digest-2024-06-15/`, then `./digest.sh` to extract, annotate preprint caveats.

**Plan:**
1. Fetch the RSS feeds of NVIDIA, Microsoft, Google DeepMind, and Mistral.
2. Include arXiv's "cs.AI" feed to capture AI preprints, with caveats noted.
3. Save the raw XML files to `/tmp/ai-news-digest-2024-06-15/`.
4. Run `./digest.sh` to extract and annotate the relevant information from the XMLs.
5. Compile a JSON digest with headlines, URLs, and timestamps.

**What changed:** The decision to include arXiv's feed with annotations addresses the nuances of blending authoritative sources with preprints.
