# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-295` (dept) · 2026-08-18T13:27:22.962012+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive generates a real-time status report of the container’s state and health metrics.
3. Warden verifies the report confirms the container is active and not fake/dead.
4. Audit validates Warden’s action as MISSION work.
5. Bastion synthesizes the verification into a closed-loop security confirmation.

**What changed:** Container health status is now confirmed via real-time ToolHive report.
