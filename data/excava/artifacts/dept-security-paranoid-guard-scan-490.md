# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-490` (dept) · 2026-08-04T09:40:25.424382+00:00
> Participants: Warden, Audit, Bastion · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Verify the LLM Guard container's real-time state to ensure security and detect potential leaks or injections.
**Plan:**
1. Warden instructs ToolHive to query the LLM Guard container for its health status.
2. ToolHive verifies the LLM Guard container's real-time state and produces a status report.
3. Warden reviews the status report to confirm the container is running and healthy.
4. Bastion monitors the output to detect any potential leaks or injections.
5. If the container is confirmed healthy, Warden and Bastion proceed with normal operations.
**What changed:** The LLM Guard container's real-time state is now being verified by ToolHive to ensure security and detect potential threats.
