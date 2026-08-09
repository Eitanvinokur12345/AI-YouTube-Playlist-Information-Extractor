# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-368` (dept) · 2026-08-05T03:46:45.125404+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive generates a confirmation report with container status and detected issues.
3. Warden reviews the report to verify LLM Guard is running and healthy.
4. If issues are detected, Warden initiates remediation (e.g., restart, rollback).
5. Audit validates the process and confirms no leaks/injection.
6. Bastion closes the room upon successful verification.

**What changed:** Warden’s action is now explicitly tied to ToolHive’s direct verification and report generation.
