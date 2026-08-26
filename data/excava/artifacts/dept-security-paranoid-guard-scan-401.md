# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-401` (dept) · 2026-08-26T11:05:48.000001+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive via MCP server lifecycle manager for LLM Guard container health status.
2. ToolHive returns a real-time status report confirming operational state or anomalies.
3. Bastion reviews the status report for leaks/injection, verifies element authenticity, and detects anomalies.
4. If anomalies are detected, Bastion initiates containment protocols.
5. If no anomalies, Bastion marks the container as verified and healthy.
6. Log the verification outcome for audit trail.

**What changed:** Warden’s action is approved and formalized as a concrete verification step.
