# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-908` (dept) · 2026-08-26T20:43:06.353431+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Approve Warden’s action to verify LLM Guard container health via ToolHive.

**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive performs real-time check and returns either:
   - "LLM Guard container is running and healthy" or
   - "LLM Guard container is unhealthy/dead".
3. Warden confirms the output and logs the result for audit.
4. If unhealthy, Warden initiates containment protocol (e.g., restart, isolate).
5. Audit reviews the logged status and containment actions.
6. Bastion archives the verification record for security traceability.

**What changed:** Warden’s verification action is now formalized as a mandatory security check.
