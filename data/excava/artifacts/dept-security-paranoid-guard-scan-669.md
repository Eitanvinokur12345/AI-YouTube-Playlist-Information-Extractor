# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-669` (dept) · 2026-08-01T17:34:57.902002+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs ToolHive to verify the LLM Guard container status and produces a container health report.
2. Warden activates LLM Guard in real-time scan mode against the current input/output stream.
3. LLM Guard generates a live report flagging any suspicious patterns or unauthorized data exposure.
4. If leaks/injection are detected, Bastion triggers immediate containment protocols.
5. Verify all elements in the stream are real (not fake/dead) via cross-referencing with ToolHive.
6. Log all findings and actions for audit purposes.

**What changed:** Container verification and real-time scanning are now mandatory before proceeding.
