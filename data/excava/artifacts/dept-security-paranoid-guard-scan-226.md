# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-226` (dept) · 2026-08-30T04:12:35.432251+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for the LLM Guard container’s health status.
2. ToolHive returns a real-time report confirming the container’s operational state and security posture.
3. Audit verifies the report’s authenticity and logs the outcome for compliance.
4. If the container is unhealthy, Warden initiates remediation via ToolHive.
5. Bastion archives the report and updates the security dashboard.
6. Repeat the verification process every 4 hours as a baseline security measure.

**What changed:** Automated real-time verification of LLM Guard container integrity via ToolHive’s MCP server.
