# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-998` (dept) · 2026-08-26T09:31:37.023844+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for the LLM Guard container’s health status.
2. ToolHive returns a real-time status report confirming the container’s existence and operational state.
3. Bastion verifies the report’s authenticity and logs the result for audit.
4. If the report confirms health, proceed with the next security step.
5. If the report indicates issues, trigger containment protocols.
6. Audit records the verification for compliance.

**What changed:** Warden’s action is now explicitly executed via ToolHive’s MCP lifecycle manager for direct verification.
