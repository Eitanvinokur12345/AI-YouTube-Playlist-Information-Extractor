# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-217` (dept) · 2026-08-10T20:48:22.410759+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Approve Warden’s action to verify LLM Guard container health via ToolHive.

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for LLM Guard container status.
2. ToolHive returns a real-time status report confirming container existence and operational state.
3. Audit verifies the report’s authenticity and logs the result.
4. Bastion cross-checks the report against ToolHive’s lifecycle logs.
5. If status is healthy, proceed; if not, trigger remediation via Warden.

**What changed:** LLM Guard container health verification is now mandatory and automated via ToolHive.
