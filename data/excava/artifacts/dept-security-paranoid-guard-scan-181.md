# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-181` (dept) · 2026-08-03T19:47:24.169245+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for the LLM Guard container’s health status.
2. ToolHive executes a real-time scan for leaks/injection risks and verifies container integrity.
3. ToolHive returns a status report confirming operational state and scan results.
4. Audit cross-checks the report for consistency and flags anomalies.
5. Bastion archives the report for compliance and initiates remediation if risks are detected.

**What changed:** Warden’s action is now formalized as a mandatory verification step.
