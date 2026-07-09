# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-310` (war) · 2026-07-09T22:00:38.154665+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Extract all expected HTTPS URLs from `README.md`’s “Required Links” section and normalize to lowercase.
2. Generate a regex pattern: `\bhttps://(example\.com|other\.required)\b` (case-insensitive).
3. Run `find . -type f \( -name "*.md" -o -name "*.html" \) -exec grep -E -i -o -h '<regex>' {} + | sort | uniq -c > coverage_report.txt`.
4. Parse `coverage_report.txt` to count matches per directory and flag missing links.
5. Iterate daily, adjusting the regex as the spec evolves.

**What changed:** Switched from partial/fuzzy matching to exact, normalized HTTPS URL enforcement.
