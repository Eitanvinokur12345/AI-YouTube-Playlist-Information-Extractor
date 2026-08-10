# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-317` (dept) · 2026-08-10T19:34:23.564287+00:00
> Participants: Warden, Audit, Bastion · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Verify the LLM Guard container's real-time state to ensure security and detect potential leaks or injections.
**Plan:**
1. Warden instructs ToolHive to verify the LLM Guard container's health status.
2. ToolHive checks the container's real-time state via its MCP server lifecycle manager.
3. ToolHive produces a status report confirming the container's state.
4. Warden receives and reviews the status report to confirm the container is running and healthy.
5. Bastion monitors the output to detect any potential security threats or leaks.
**What changed:** The LLM Guard container's health status is now being verified in real-time to ensure security and detect potential threats.
