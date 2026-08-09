# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-539` (dept) · 2026-08-04T14:51:59.999992+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Approve Warden’s action to verify LLM Guard container health via ToolHive.

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for LLM Guard container status.
2. ToolHive returns a live status report confirming container existence and operational state.
3. Bastion records the report as verified evidence of LLM Guard’s real-time health.
4. Audit cross-references the report with prior baselines for consistency.
5. If status is healthy, proceed with security protocols; if not, trigger remediation.
6. Document the verification in the security audit log.

**What changed:** LLM Guard container health status now confirmed via ToolHive’s direct verification.
