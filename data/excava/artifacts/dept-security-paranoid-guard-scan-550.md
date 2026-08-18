# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-550` (dept) · 2026-08-18T14:36:11.686058+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
Proceed with Warden’s verification of the LLM Guard container’s real-time health via ToolHive.

**Plan:**
1. Warden queries ToolHive for the LLM Guard container’s health status.
2. ToolHive executes a container lifecycle check to verify real-time operational integrity.
3. ToolHive returns a status report confirming the container’s authenticity and health.
4. Audit reviews the status report for discrepancies or anomalies.
5. If verified, proceed with downstream security checks; if not, trigger containment protocols.

**What changed:** Warden’s action is now formalized as a direct verification step via ToolHive.
