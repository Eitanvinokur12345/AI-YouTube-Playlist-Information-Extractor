# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-814` (dept) · 2026-08-01T19:47:42.878980+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs ToolHive to verify LLM Guard container status and confirms health/readiness for real-time scanning.
2. Warden executes LLM Guard on the latest input/output stream to scan for leaks or injection attempts.
3. Warden generates and delivers a real-time security report flagging anomalies or unauthorized data.
4. Bastion synthesizes the report and confirms no leaks/injection were detected.
5. If anomalies are found, Warden isolates the affected stream and initiates remediation.
6. Warden logs all actions for audit and Bastion archives the report.

**What changed:** Container verification and real-time scanning are now explicitly ordered and logged.
