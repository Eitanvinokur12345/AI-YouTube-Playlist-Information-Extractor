# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-300` (dept) · 2026-08-03T04:48:20.323481+00:00
> Participants: Warden, Audit, Bastion · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Verify the LLM Guard container's health status to ensure secure scanning of inputs/outputs.
**Plan:**
1. Warden instructs ToolHive to verify the LLM Guard container's health status.
2. ToolHive produces a real-time status report confirming the container's operational state.
3. The report is reviewed to confirm the container is running and healthy.
4. If the container is verified healthy, proceed with scanning inputs/outputs for leaks/injection.
5. If issues are detected, initiate corrective actions to ensure container health and security.
**What changed:** The LLM Guard container's health status is now verified, enabling secure scanning of inputs/outputs.
