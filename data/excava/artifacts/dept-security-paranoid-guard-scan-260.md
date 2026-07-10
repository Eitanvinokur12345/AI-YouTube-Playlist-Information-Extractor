# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-260` (dept) · 2026-07-10T01:30:17.680729+00:00
> Participants: Warden, Audit, Bastion · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** The artifact must include a verifiable baseline of critical binaries and processes from an external trusted source to ensure integrity.

**Plan:**
1. Establish a verifiable baseline of critical binaries using an external trusted source, such as a vendor repository or offline ISO.
2. Pull cryptographic hashes of critical binaries and compare them to the established baseline using `sha256sum`.
3. Validate the integrity of auditing tools (`rkhunter`, `chkrootkit`) by retrieving their binary hashes from an external trusted source.
4. Conduct a full filesystem audit with `rkhunter` and `chkrootkit` using the validated versions of the tools.
5. Cross-check running processes against an external known-good baseline to ensure accuracy and integrity.
6. Utilize alternative monitoring tools or methodologies to validate system integrity beyond relying solely on local tools.

**What changed:** Emphasis was placed on obtaining external verification for both binaries and auditing tools to prevent reliance on potentially compromised local tools.
