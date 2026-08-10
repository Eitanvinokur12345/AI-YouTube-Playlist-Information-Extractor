# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-901` (dept) · 2026-08-10T17:29:48.960156+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive returns container status (running/healthy or not).
3. If status is "running/healthy," proceed with security operations.
4. If status is not "running/healthy," escalate to containment protocols.
5. Audit logs the verification outcome for compliance tracking.
6. Bastion closes the room upon confirmation of operational integrity.

**What changed:** Warden’s query to ToolHive is now the authoritative verification step for LLM Guard container health.
