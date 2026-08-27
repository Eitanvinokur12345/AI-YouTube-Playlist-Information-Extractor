# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-376` (dept) · 2026-08-27T14:45:37.446952+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for the LLM Guard container’s health status.
2. ToolHive returns a real-time status report confirming the container’s operational state and security posture.
3. Audit verifies the report’s authenticity and alignment with security requirements.
4. Bastion synthesizes the report into a final security assessment.
5. If the container is healthy, proceed with secure operations; if not, trigger containment protocols.

**What changed:** Warden’s action is now explicitly tied to ToolHive’s MCP server for direct verification.
