# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-328` (dept) · 2026-08-13T11:24:22.851355+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for LLM Guard container health status.
2. ToolHive verifies container existence and operational state in real-time.
3. ToolHive returns a status report confirming the container is running and healthy.
4. Bastion records the verified status as the authoritative state.
5. Audit logs the verification action as MISSION work.

**What changed:** LLM Guard container health status confirmed via ToolHive’s direct verification.
