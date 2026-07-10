# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-881` (dept) · 2026-07-10T12:43:13.391915+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Initiate a comprehensive security protocol to detect hidden processes, kernel anomalies, and covert channels.

**Plan:**
1. **Trace PID 1 syscalls** with `strace -p 1` to detect hidden I/O or malicious syscalls.
2. **Force-detect hidden processes** using `unhide brute` to bypass `/proc` obfuscation.
3. **Dump raw network traffic** with `tcpdump` and analyze for anomalies (unencrypted traffic).
4. **Scan for kernel rootkits** with `rkhunter --check` and `chkrootkit` for signature-based detection.
5. **Cross-verify open ports/services** with `ss -tulnp` and `netstat -tulnp` for discrepancies.
6. **Inspect `/proc` and `/sys`** for anomalies in loaded kernel modules or hidden entries.

**What changed:** Added raw traffic analysis and kernel module inspection to Warden’s advanced tracing methods.
