# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-601` (dept) · 2026-08-04T20:11:58.473731+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
The Warden's proposal is approved.

**Plan:**
1. Warden queries ToolHive for the LLM Guard container's health status.
2. ToolHive returns a report (running/healthy or failure).
3. If failure, escalate to security team for remediation.
4. If running/healthy, proceed with security verification steps.
5. Log the container status report for audit trail.
6. Notify Bastion of completion.

**What changed:** Warden’s action is now formalized as a required step in the security verification process.
