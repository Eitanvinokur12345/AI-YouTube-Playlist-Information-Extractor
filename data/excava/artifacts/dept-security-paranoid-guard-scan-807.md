# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-807` (dept) · 2026-08-10T21:25:54.318657+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for the LLM Guard container’s health status.
2. ToolHive returns the real-time status report to Warden.
3. Warden forwards the status report to Audit for verification.
4. Audit confirms the container’s authenticity and health metrics.
5. If discrepancies are found, escalate to Bastion for remediation.

**What changed:** Warden’s action is now explicitly delegated to ToolHive for direct verification, with Audit as the final validator.
