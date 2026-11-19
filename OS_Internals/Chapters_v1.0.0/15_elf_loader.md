# 15 — ELF64 executable headers, loadable segments, alignment and zero fill

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How can a bounded loader inspect executable segments without trusting corrupt offsets or executing untrusted bytes?

## Assumptions and explicit model boundary

Only little-endian ELF64 ET_EXEC/ET_DYN for x86-64 or AArch64 is in scope. The parser never maps executable memory or runs instructions. Each PT_LOAD has an offset, virtual address, file size, memory size, flags and alignment.

## Mathematical law or invariant

0 <= p_filesz <= p_memsz <= M_limit; p_offset+p_filesz <= len(file); p_vaddr mod p_align = p_offset mod p_align (p_align > 1).

## Derivation and operational interpretation

The ELF file header supplies program header count, size and offset; the loader must check multiplication and bounds before iterating. For PT_LOAD the initialized prefix is copied from the file and the memory tail up to p_memsz is zero initialized. Alignment and address width may constrain mapping. On a real system dynamic relocation, interpreter loading, ASLR, TLS segments, RELRO and executable permission enforcement add layers absent from a bounded parser.

## Worked constructed investigation

A constructed ELF64 has a single PT_LOAD at file offset 4096 and virtual address 0x402000, four initialized bytes ABCD and memory size 128. The parser reports 124 zero-fill bytes. A file with memory size 3 but file size 4 is rejected; a truncated file offset is also rejected.

## Executable or experimental reconstruction procedure

Run os_atlas.elf64.loadable_segments on a synthetic test ELF64 and independently unpack its 64-byte header and 56-byte program headers. Validate truncation at every boundary, permission flags, alignment and an upper bound before allocating any segment.

## Adversarial/negative case

A missing bounds check on e_phnum*e_phentsize can read outside a file. An unchecked p_memsz can request enormous memory; a wrong p_offset may load unrelated bytes as code. A parser passing does not make an executable trusted or safe.

## Failure boundaries, unknowns and acceptance holds

No dynamic linker, relocation, signature verification, executable memory allocation, process creation, or non-ELF formats (PE/Mach-O).

## Exact-source links and dependent knowledge

Bibliographic pointers: ELF5 (https://man7.org/linux/man-pages/man5/elf.5.html), EXECVE2 (https://man7.org/linux/man-pages/man2/execve.2.html)

Cross-domain prerequisites: computer-architecture-digital-hardware-atlas, cryptographic-protocols-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
