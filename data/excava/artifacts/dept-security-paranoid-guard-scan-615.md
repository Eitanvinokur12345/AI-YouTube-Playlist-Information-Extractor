# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-615` (dept) · 2026-08-03T19:22:02.000553+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive generates a real-time container health report (running/healthy or failure details).
3. Audit verifies the report’s authenticity and mission relevance.
4. Bastion synthesizes the report into a consolidated status update.
5. If unhealthy, initiate containment protocol per security SOP.
6. Log the verification event in the audit trail.

**What changed:** Warden’s verification is now explicitly delegated to ToolHive for real-time, authoritative status.
