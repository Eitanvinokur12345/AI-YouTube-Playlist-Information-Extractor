# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-570` (dept) · 2026-08-03T02:46:00.178119+00:00
> Participants: Warden, Audit, Bastion · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Verify LLM Guard container health status to ensure security scanner is active and operational.
**Plan:**
1. Warden instructs ToolHive to verify the LLM Guard container is running and healthy.
2. ToolHive directly checks the LLM Guard container's status.
3. ToolHive produces a live status report confirming the security scanner is active and operational.
4. Warden receives and reviews the live status report from ToolHive.
5. Audit reviews the action for mission work compliance.
**What changed:** The LLM Guard container's health status is now verified through ToolHive.
