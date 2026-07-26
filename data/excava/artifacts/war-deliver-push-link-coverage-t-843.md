# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-843` (war) · 2026-07-26T00:45:47.021268+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:**
Push link coverage to 100% at +5%/day via balanced investment in Kaedim and Gluestack.

**Plan:**
1. **Kaedim Integration (50%):** Deploy Kaedim’s AI 3D asset pipeline to auto-generate product pages, audited via static reference comparisons (transcripts + product pages).
2. **Gluestack UI Testing (50%):** Build a custom, open-source MCP server for UI link testing to avoid vendor lock-in and ensure auditability.
3. **Audit Logic Overhaul:** Replace model self-reporting with deterministic checks against static references for Kaedim outputs.
4. **Parallel Validation:** Run Gluestack’s MCP server and custom solution in parallel for 2 weeks, comparing outputs to identify discrepancies.
5. **Coverage Tracking:** Implement daily dashboards to monitor link coverage growth (+5%/day target) and flag audit failures.
6. **Documentation:** Publish audit logic and MCP server code in public repo for transparency.

**What changed:**
Split effort 50/50 between Kaedim (audit-focused) and Gluestack (custom MCP server) to ensure 100% auditable link coverage.
