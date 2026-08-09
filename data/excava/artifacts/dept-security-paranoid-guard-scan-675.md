# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-675` (dept) · 2026-08-08T07:32:54.888734+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive verifies container status and readiness for input/output scanning.
3. ToolHive returns confirmation of container health and readiness.
4. Audit validates the confirmation as MISSION work.
5. Bastion synthesizes the verification into a secure, verified state.

**What changed:** Container health and readiness confirmed via ToolHive.
