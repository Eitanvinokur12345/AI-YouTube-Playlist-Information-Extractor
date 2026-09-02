# Deliver: Keep the Designs tab pure: designs only, live previews, taste-ranked

> Decision artifact · room `war-deliver-keep-the-designs-tab-538` (war) · 2026-09-02T11:39:13.821306+00:00
> Participants: Chisel, Sift, Scope, Scriv, Echo, Reel · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt the PCIe-attached validator with a $50 ARM board and $300 TPM-backed NVMe drive for real-time transcript validation.

**Plan:**
1. Procure a $50 ARM board (e.g., Raspberry Pi CM4) with PCIe support.
2. Pair it with a $300 TPM-backed NVMe drive (e.g., Kingston KC2500 with TPM 2.0).
3. Audit the NVMe firmware and TPM trust chain for integrity.
4. Deploy the validator artifact via the bus task (Owner: Reel).
5. Integrate the validator into the Designs tab pipeline for live previews.
6. Enforce *free-only* compliance by disabling Deepgram’s API.

**What changed:**
Replaced cloud-dependent Deepgram validation with a local, hardware-backed validator.
