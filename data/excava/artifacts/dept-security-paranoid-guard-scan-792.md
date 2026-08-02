# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-792` (dept) · 2026-08-02T07:09:33.782052+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs ToolHive to verify the LLM Guard container is running and healthy.
2. ToolHive generates a live status report confirming container health.
3. Report includes detection of leaks and injection risks.
4. Audit validates the mission work of the verification process.
5. Bastion synthesizes the output into a final decision.

**What changed:** Container verification now explicitly includes leak/injection detection.
