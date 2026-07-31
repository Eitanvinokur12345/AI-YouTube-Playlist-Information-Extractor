# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-553` (dept) · 2026-07-31T22:37:17.792134+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs ToolHive to verify LLM Guard container status.
2. ToolHive outputs real-time health report confirming container is live and responsive.
3. Bastion synthesizes report to confirm no leaks/injection and elements are real.
4. If container is healthy, proceed with secure operations.
5. If container is unhealthy, quarantine and investigate immediately.
6. Log all verification steps for audit trail.

**What changed:** Container verification now enforced via ToolHive health check.
