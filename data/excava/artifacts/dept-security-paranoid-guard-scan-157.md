# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-157` (dept) · 2026-08-05T02:26:22.191774+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive verifies and returns status: "LLM Guard container: RUNNING (healthy)" or "LLM Guard container: NOT RUNNING (unhealthy)".
3. If status is "RUNNING (healthy)", proceed with security checks.
4. If status is "NOT RUNNING (unhealthy)", escalate to container restart or replacement.
5. Log the verification result for audit trail.
6. Confirm resolution with Bastion before proceeding.

**What changed:** Container health verification is now explicitly required before security operations.
