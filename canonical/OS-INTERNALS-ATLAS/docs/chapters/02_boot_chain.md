# 02 — Firmware, boot loaders, kernel initialization and trusted recovery

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

What is the minimally reconstructible sequence from power-on to a verified userspace service?

## Assumptions and explicit model boundary

Assume a processor reset vector, executable firmware, nonvolatile boot storage, an executable image, initialized RAM, a clock/interrupt setup and a console. Verified boot is conditional on an authenticated root of trust and failure-safe key provisioning; hashing a boot image without authenticating the expected digest is not sufficient.

## Mathematical law or invariant

Boot transition: reset -> firmware hardware discovery -> loader -> kernel entry -> memory/interrupt setup -> initial process -> services; accept(image) := Verify(root_key,signature,Hash(image)) AND anti_rollback_version.

## Derivation and operational interpretation

The reset address provides initial instructions. Firmware initializes enough memory and I/O to read a loader. A loader interprets an executable image, chooses load addresses and hands off memory maps and firmware descriptors. The kernel establishes page tables, protection domains, interrupt vectors, allocators and a first process. Each step has an assumed interface. A trustworthy chain is not transitive if a later stage trusts unsigned configuration or allows rollback to vulnerable code.

## Worked constructed investigation

A 64-bit ELF segment has p_filesz=100 bytes and p_memsz=256 bytes. A loader copies 100 bytes and zeros 156 bytes. A corrupted p_filesz larger than p_memsz must be rejected before allocation. The Python ELF64 parser checks this invariant without executing untrusted code.

## Executable or experimental reconstruction procedure

Create a minimal offline boot manifest with target ISA, endianness, memory map, expected image digest, verified signing-key source, console and storage device identifiers. Validate ELF headers and storage blobs in isolation; do not run unsigned firmware. Record failed dependency discovery as HOLD instead of claiming a bootable OS.

## Adversarial/negative case

A SHA-256 checksum stored next to the image cannot authenticate an adversary-controlled image. A loader can reject malformed binaries yet still boot the wrong image if the trust anchor is missing. Power-loss during antirollback counter update can re-enable old firmware.

## Failure boundaries, unknowns and acceptance holds

No live UEFI, BIOS, ROM, secure-element, firmware flashing or target-board boot experiments. Platform-specific image formats and boot protocols must be separately validated.

## Exact-source links and dependent knowledge

Bibliographic pointers: NIST_FW (https://csrc.nist.gov/pubs/sp/800/193/final), ELF5 (https://man7.org/linux/man-pages/man5/elf.5.html), DEVICE_MODEL (https://docs.kernel.org/driver-api/driver-model/overview.html)

Cross-domain prerequisites: computer-architecture-digital-hardware-atlas, cryptographic-protocols-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
