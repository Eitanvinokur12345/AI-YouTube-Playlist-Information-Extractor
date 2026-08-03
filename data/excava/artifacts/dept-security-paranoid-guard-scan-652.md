# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-652` (dept) · 2026-08-03T04:30:19.698110+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for LLM Guard container health status.
2. ToolHive generates a real-time status report confirming operational state.
3. Report includes detection of leaks or injection risks.
4. Audit verifies the mission work is complete.
5. Bastion synthesizes findings into a final status update.
6. Container status is logged for future reference.

**What changed:** Container health verification is now explicitly tied to leak/injection detection via ToolHive.
