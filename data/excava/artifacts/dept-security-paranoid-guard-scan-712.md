# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-712` (dept) · 2026-08-03T22:55:18.223191+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
The Warden’s request to verify the LLM Guard container’s real-time operational state is approved.

**Plan:**
1. Warden queries ToolHive via its container lifecycle API for the LLM Guard container’s health status.
2. ToolHive returns a real-time operational state report (e.g., running, healthy, or degraded).
3. Audit confirms the report’s authenticity and logs the verification.
4. If the container is unhealthy, Bastion triggers a remediation workflow (e.g., restart or alert).
5. Warden updates the security dashboard with the verified status.
6. Bastion archives the report for compliance auditing.

**What changed:**
LLM Guard container health status is now verified and logged via ToolHive’s API.
