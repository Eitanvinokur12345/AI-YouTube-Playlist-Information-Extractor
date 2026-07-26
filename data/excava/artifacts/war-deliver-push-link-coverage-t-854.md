# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-854` (war) · 2026-07-26T02:59:22.594449+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Feed Kaedim’s 3D asset outputs into the link checker for a 24-hour test.
2. Run a parallel audit of the scanner’s current crawl limits (e.g., sitemap depth, JS rendering).
3. Log all broken links from Kaedim’s output and scanner’s crawl in a shared report.
4. Compare Kaedim’s link integrity vs. scanner’s coverage ceiling within 48 hours.
5. If Kaedim introduces no new broken links, escalate integration; else, deprioritize.
6. If scanner’s crawl limits are the bottleneck, allocate resources to fix parsing/JS issues.

**What changed:** Combined Kaedim test + scanner audit to validate both tool and process in 48 hours.
