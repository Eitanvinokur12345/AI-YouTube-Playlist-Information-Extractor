# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-688` (dept) · 2026-07-31T06:35:07.821657+00:00
> Participants: Warden, Bastion · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Implement real-time scanning using LLM Guard to ensure security and integrity of the input/output payload.
**Plan:**
1. Run LLM Guard's real-time scanner on the latest input/output payload to detect leaks, injections, or fake elements.
2. Store the security verdict in an artifact, such as "data/excava/artifacts/llm-guard-scan-current-payload-690.md", for auditing and reference.
3. Utilize LLM Guard in real-time scan mode against the current input/output stream to detect and prevent potential security threats.
4. Continuously monitor and update the security artifact to reflect the latest scan results and verdicts.
5. Process messages further only after receiving a security verdict from LLM Guard, ensuring the integrity of the conversation.
**What changed:** The implementation of real-time scanning using LLM Guard has been finalized to enhance security measures.
