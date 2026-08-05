# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-845` (dept) · 2026-08-05T02:14:07.579735+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for LLM Guard container health status.
2. ToolHive generates and returns a real-time container health report.
3. Bastion verifies the report confirms the container is operational and free of anomalies.
4. Audit cross-checks the report’s authenticity via ToolHive’s direct verification.
5. If anomalies detected, escalate to containment protocol; else, proceed with secure operation.

**What changed:** Warden’s action is now explicitly tied to ToolHive’s direct verification via MCP server lifecycle manager.
