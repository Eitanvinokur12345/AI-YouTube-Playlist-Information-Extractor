# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-598` (dept) · 2026-08-26T05:08:52.910025+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
Execute Warden's proposed verification of the LLM Guard container health.

**Plan:**
1. Warden queries ToolHive’s MCP server lifecycle manager for the LLM Guard container’s real-time health status.
2. ToolHive returns a status report confirming operational state and any detected anomalies.
3. Audit cross-references the report against expected baselines for validation.
4. If anomalies are detected, Bastion triggers containment protocols (e.g., isolation, rollback).
5. If clean, Bastion marks the container as verified and logs the timestamp.
6. Warden updates the security dashboard with the verification outcome.

**What changed:** Container health verification is now actively executed via ToolHive’s MCP server.
