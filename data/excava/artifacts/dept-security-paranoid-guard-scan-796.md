# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-796` (dept) · 2026-07-31T23:19:02.682017+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs ToolHive to verify LLM Guard container status.
2. Confirm container is running, healthy, and free of leaks/injection.
3. Validate all elements are real (not fake/dead).
4. Document verification results in real-time status report.
5. Proceed only if ToolHive output confirms security readiness.

**What changed:** Container verification via ToolHive is now mandatory before proceeding.
