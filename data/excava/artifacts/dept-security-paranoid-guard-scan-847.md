# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-847` (dept) · 2026-07-27T22:12:19.044315+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks or injection attempts.
2. Flag any suspicious patterns or anomalies in real-time and report them immediately.
3. Verify all elements (inputs, outputs, references) are real and not fake/dead.
4. Cross-check detected anomalies against known injection/leak signatures.
5. If anomalies are found, isolate and quarantine the affected data stream.
6. Log all scan results and verification steps for audit purposes.

**What changed:** Scanner integration and verification steps added to the workflow.
