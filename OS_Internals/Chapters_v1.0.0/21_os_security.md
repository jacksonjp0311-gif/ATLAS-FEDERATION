# 21 — Isolation boundaries, namespaces, least privilege and update trust

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

What security properties of an OS can be articulated without claiming that a toy model provides isolation?

## Assumptions and explicit model boundary

Threats include untrusted processes, malicious files, network peers, exploitable drivers, supply-chain compromise and physical attackers. A secure design must state trusted computing base, hardware/firmware trust root, patch mechanism, privilege escalation paths and rollback policy.

## Mathematical law or invariant

Allow = valid_subject AND capability_scope AND object_policy AND kernel_check; confidentiality, integrity, availability require separate threat models.

## Derivation and operational interpretation

Least privilege reduces a compromised component’s authority. A namespace changes what names the process can resolve, but the host kernel is still shared. A virtual machine separates more execution state but depends on a hypervisor and hardware virtualization; neither is automatically a complete security boundary. An encrypted disk does not remove endpoint compromise risk. Secure update depends on authenticated metadata and a durable version monotonicity mechanism.

## Worked constructed investigation

A process restricted to a directory might escape through a symlink if the path is checked as text. A kernel-supported restricted open with no symlink traversal can enforce a stronger policy under documented assumptions. Reusing a revoked file handle must not silently confer access to a newly opened secret file.

## Executable or experimental reconstruction procedure

Draw the TCB and three explicit attack trees: file path escape, stale handle reuse, malicious update rollback. Map every mitigation to an actual mechanism and test. Document what an offline verifier can and cannot authenticate. Never treat the educational capability table as secure against adversarial memory access.

## Adversarial/negative case

A sandbox may still share a vulnerable kernel. Checksums alone cannot prevent a modified executable from passing an attacker-modified manifest. Rights checks omitted in one code path invalidate the intended policy.

## Failure boundaries, unknowns and acceptance holds

No penetration test, exploit resistance proof, secure boot deployment, kernel hardening verification, formal access-control model or verified production cryptography.

## Exact-source links and dependent knowledge

Bibliographic pointers: OPENAT2 (https://man7.org/linux/man-pages/man2/openat2.2.html), NIST_FW (https://csrc.nist.gov/pubs/sp/800/193/final), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: cryptographic-protocols-atlas, software-design-patterns-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
