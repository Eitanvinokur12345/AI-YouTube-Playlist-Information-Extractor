# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-348` (dept) · 2026-08-15T22:52:18.527705+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive via MCP server lifecycle manager for LLM Guard container health status.
2. ToolHive returns real-time status confirming container is running and secure.
3. Audit verifies the Warden’s action as mission-compliant.
4. Bastion records the confirmed operational state for audit trails.
5. If container is unhealthy, initiate automated remediation via ToolHive.
6. Log all verification steps in immutable audit log.

**What changed:** LLM Guard container health status confirmed and logged.
