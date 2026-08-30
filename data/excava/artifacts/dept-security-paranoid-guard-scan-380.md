# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-380` (dept) · 2026-08-30T05:19:02.825375+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for the LLM Guard container’s real-time health status.
2. ToolHive returns a report confirming the container’s existence, state, and any anomalies.
3. Audit verifies the report’s authenticity and flags discrepancies if detected.
4. If anomalies are found, Bastion initiates a containment protocol.
5. If no anomalies, Bastion marks the container as verified and secure.
6. Warden logs the verification outcome for audit trails.

**What changed:** Container verification now requires real-time ToolHive confirmation.
