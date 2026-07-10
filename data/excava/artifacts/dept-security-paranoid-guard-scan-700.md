# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-700` (dept) · 2026-07-10T02:04:34.723659+00:00
> Participants: Warden, Audit, Bastion · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** Conduct a comprehensive scan for unauthorized SUID binaries and verify their legitimacy across all filesystems.

**Plan:**
1. Execute `find / -perm -4000 -type f 2>/dev/null | sort -u > /tmp/suid_all.txt` to identify all SUID binaries.
2. Incorporate checks for unmounted filesystems, tmpfs, and bind mounts during the scanning process.
3. Cross-verify each found binary's legitimacy against all potential package managers, including dpkg, snap, pip, gem, and any custom installation methods.
4. Document the results in a detailed report, including the path, ownership, and legitimacy status of each binary.
5. Schedule regular scans to monitor for new unauthorized SUID binaries.

**What changed:** The decision now includes scanning all filesystems and verifying binaries against a wider range of package management systems.
