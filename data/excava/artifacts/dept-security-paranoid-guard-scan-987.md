# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-987` (dept) · 2026-08-10T21:01:11.926804+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden queries ToolHive for the LLM Guard container’s health status.
2. ToolHive generates a live status report confirming the container is running and healthy.
3. The status report is sent to Audit for verification.
4. Audit validates the report to ensure no fake/dead processes are detected.
5. Bastion synthesizes the results to confirm security integrity.

**What changed:** Warden’s action is now explicitly tied to ToolHive’s verification and Audit’s validation.
