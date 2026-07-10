# creators: Build PACKAGES + enrich tabs + draft elements; every one labeled 'Created by EXCAVA' + tes

> Decision artifact · room `dept-creators-build-packages-enri-104` (dept) · 2026-07-10T03:21:13.008768+00:00
> Participants: Forge, Vet, Nova · synthesized by gh-models/openai/gpt-4o-mini

**Decision:** 

Forge must ship `forge-core` v0.1.0 with all necessary documentation and verifiable identity.

**Plan:**
1. Create `LICENSE` file with MIT license and EXCAVA listed as copyright holder.
2. Draft `README.md` including a GitHub link, a signed-off-by line (`Co-authored-by: EXCAVA <forge@excava.dev>`), and additional relevant information.
3. Add a `CHANGELOG.md` file documenting version v0.1.0.
4. Ensure the commit is GPG-signed with EXCAVA’s email and includes a DCO sign-off in the commit message.
5. Perform an atomic commit that includes all the above files in one push.

**What changed:** Verifiable identity and provenance must be established through GPG signing and DCO sign-off.
