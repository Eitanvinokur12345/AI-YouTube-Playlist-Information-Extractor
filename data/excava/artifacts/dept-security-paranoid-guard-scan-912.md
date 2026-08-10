# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-912` (dept) · 2026-08-10T20:02:06.228506+00:00
> Participants: Warden, Audit, Bastion · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement verification of LLM Guard container health status through ToolHive.
1. **Warden instructs ToolHive**: to verify the LLM Guard container is running and healthy.
2. **ToolHive checks container health**: via its MCP server lifecycle manager.
3. **ToolHive reports back**: to Warden with a confirmation or failure report on the container's status.
4. **Warden receives output**: containing the health status of the LLM Guard container.
5. **Analyze the report**: to determine the next course of action based on the container's health status.
**What changed:** The LLM Guard container's health status will be verified and reported back to Warden.
