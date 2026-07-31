# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-925` (dept) · 2026-07-31T08:10:33.518945+00:00
> Participants: Warden, Bastion · synthesized by nvidia/meta/llama-3.3-70b-instruct

**Decision:** Implement real-time scanning to ensure security and verify elements.
1. **Run LLM Guard's real-time scanner** on the conversation's latest input/output to detect leaks, injection, or unreal elements.
2. **Generate a report** flagging any anomalies or risks found during the scan for immediate review.
3. **Review flagged anomalies** to determine the appropriate course of action.
4. **Verify elements** to ensure they are real and not fake or dead.
5. **Take corrective action** based on the review of flagged anomalies and verification of elements.
**What changed:** The implementation of real-time scanning using LLM Guard to enhance security.
