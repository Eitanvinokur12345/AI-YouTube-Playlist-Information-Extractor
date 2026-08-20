# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-591` (dept) · 2026-08-20T17:04:46.998796+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for real-time LLM Guard container health status.
2. ToolHive performs runtime verification to confirm container is running, healthy, and not leaking.
3. Warden receives and validates the status report from ToolHive.
4. Audit confirms ToolHive’s verification as mission-appropriate.
5. Bastion records the confirmed operational state in logs.

**What changed:** LLM Guard container health status verified via ToolHive runtime check.
