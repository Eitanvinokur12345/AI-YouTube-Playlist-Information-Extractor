# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-817` (dept) · 2026-08-26T02:12:29.313643+00:00
> Participants: Bastion, Warden, Audit · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for real-time LLM Guard container health status.
2. ToolHive verifies container existence and operational state via direct system check.
3. Audit confirms Warden’s action as mission-appropriate and valid.
4. If status is healthy, proceed with security-critical operations.
5. If status is unhealthy, trigger containment protocol (e.g., isolate, restart, or alert).
6. Log all verification steps for compliance and forensic review.

**What changed:** Warden’s verification action is validated as mission-critical and executable via ToolHive’s MCP server.
