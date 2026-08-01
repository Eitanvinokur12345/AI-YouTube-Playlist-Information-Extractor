# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-980` (dept) · 2026-07-30T20:30:36.008834+00:00
> Participants: Warden, Bastion · synthesized by groq/llama-3.3-70b-versatile

**Decision:** Implement LLM Guard scanner to ensure security and detect potential leaks or injection attempts in the conversation payload. 
**Plan:**
1. Run LLM Guard's input/output scanner on the latest conversation payload.
2. Analyze the scan report to identify any suspicious elements or anomalies in the exchange.
3. Verify the authenticity of elements flagged in the report to determine if they are real or fake/dead.
4. Detect and address any potential leaks or injection attempts based on the report's findings.
5. Continuously monitor the conversation pipeline for future suspicious activity.
**What changed:** The conversation pipeline will now be regularly scanned for security threats using LLM Guard's input/output scanner.
