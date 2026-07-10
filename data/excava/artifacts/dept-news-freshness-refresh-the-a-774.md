# news: Freshness: refresh the AI-news digest from the newest official/company/national sources.

> Decision artifact · room `dept-news-freshness-refresh-the-a-774` (dept) · 2026-07-10T03:56:36.931071+00:00
> Participants: Scoop, Factcheck, Wire · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Utilize Bloomberg's AI-specific RSS feed and NVIDIA's sitemap API for static AI headlines while excluding dynamic content.

**Plan:**
1. Run `curl -s https://feeds.bloomberg.com/technology/feed.xml | xq '.rss.channel.item[] | select(.title | ascii_downcase | contains("ai") or contains("artificial intelligence"))'` to accurately count AI-specific items from Bloomberg.
2. Access NVIDIA's sitemap API to extract static AI headlines. 
3. Filter the extracted data to ensure only valid AI-related news is included from both sources.
4. Document the counts and headlines with their corresponding timestamps and source URLs.
5. Compile the information into a digest format for distribution.

**What changed:** The approach now focuses strictly on filtered AI news, enhancing accuracy in content sourcing.
