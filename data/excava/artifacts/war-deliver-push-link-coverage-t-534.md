# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-534` (war) · 2026-07-10T03:55:14.259269+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Use `find /docs -type f -name "*.md" -exec grep -lE '\[([^\]]+)\]\(((?!https?://|#|javascript:)[^\)]*)\)' {} \;` to count *only* syntactically broken links, total `.md` files separately.

**Plan:**
1. Execute the refined grep command to identify broken links in `.md` files.
2. Tally and document the total count of `.md` files alongside the count of those with broken links.
3. Analyze the results to determine current link coverage percentage.
4. If coverage is below 95%, flag the top 10 `.md` files with the most broken links for immediate correction.
5. Set a daily goal to improve link coverage by +5% until reaching 100%.

**What changed:** The focus shifted to a more precise regex pattern to accurately identify only syntactically broken links, improving the reliability of the assessment.
