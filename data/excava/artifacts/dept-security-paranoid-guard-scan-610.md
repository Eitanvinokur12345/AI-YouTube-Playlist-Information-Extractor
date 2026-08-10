# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-610` (dept) · 2026-08-10T20:35:54.757714+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive verifies and confirms the container’s status and readiness.
3. Output the verification result to Audit.
4. Audit records the confirmation as part of the security verification process.
5. If verification fails, escalate to containment protocols.

**What changed:** Warden’s action is now explicitly delegated to ToolHive for direct verification.
