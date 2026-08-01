# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-911` (dept) · 2026-07-31T21:50:47.239355+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard against the latest conversation input to scan for prompt injection or data leaks.
2. Generate a security report flagging any suspicious patterns or unsafe content.
3. Verify all elements in the report are real (not fake/dead) by cross-checking with the original input.
4. Detect and log any confirmed leaks or injections for further review.
5. If no issues are found, proceed with normal operations; otherwise, quarantine the input and notify the Warden.

**What changed:** Input security scan and verification now mandatory before processing.
