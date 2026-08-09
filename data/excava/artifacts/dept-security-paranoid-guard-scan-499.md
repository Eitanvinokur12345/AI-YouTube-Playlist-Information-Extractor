# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-499` (dept) · 2026-08-05T21:54:06.949394+00:00
> Participants: Warden, Audit, Bastion · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Verify the LLM Guard container's health and operational state to ensure security and detect potential leaks or injections.
**Plan:**
1. Warden instructs ToolHive to verify the LLM Guard container's health and operational state.
2. ToolHive uses its MCP server lifecycle manager to directly verify the container's health.
3. ToolHive generates a real-time status report confirming the container's operational state and any detected issues.
4. Warden reviews the report to identify any potential security threats or issues.
5. If issues are detected, Warden takes corrective action to address them and ensure the container's security.
**What changed:** The LLM Guard container's health and operational state are now being verified in real-time to ensure security and detect potential threats.
