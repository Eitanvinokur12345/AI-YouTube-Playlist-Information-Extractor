# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-985` (dept) · 2026-07-28T17:47:56.911863+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs LLM Guard scanner on conversation input/output to verify integrity.
2. Scanner generates clean report confirming no leaks or injection.
3. Bastion logs output to `/var/log/llm_guard/w1_scan.log`.
4. Bastion verifies scanner report integrity before proceeding.
5. If report is clean, Bastion marks elements as REAL; else, flags for review.
6. Proceed only after Bastion confirms all elements are verified.

**What changed:** Added Bastion’s verification step for scanner output integrity.
