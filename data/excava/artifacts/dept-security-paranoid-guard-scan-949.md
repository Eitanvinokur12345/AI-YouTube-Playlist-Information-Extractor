# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-949` (dept) · 2026-08-03T03:03:23.908305+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden uses ToolHive to verify the LLM Guard container's existence and health.
2. ToolHive generates a real-time status report confirming the container's operational state.
3. Audit reviews the status report for accuracy and signs off on the verification.
4. Bastion archives the report in the security audit log.
5. If the container is unhealthy, Warden initiates remediation (restart/redeploy).
6. If healthy, Warden marks the verification as complete in the tracking system.

**What changed:** Container status verification is now enforced via ToolHive with real-time reporting.
