# 13 — VFS objects, namespaces, descriptors and filesystem path resolution

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

How does an OS turn a pathname into a handle to persistent data while preventing unexpected traversal?

## Assumptions and explicit model boundary

A VFS separates filesystem implementations from common operations. Distinguish superblocks, inodes, directory entries, open-file descriptions and per-process file descriptors. A pathname is a lookup request, not an immutable object identity.

## Mathematical law or invariant

open(path,flags,creds) -> file_description; fd_table[fd] -> file_description; authorization depends on resolved object and policy at lookup/use.

## Derivation and operational interpretation

Directory components resolve relative to a root or directory descriptor, traversing mount points and symbolic links subject to lookup constraints. An inode-like object stores metadata and file identity; a dentry caches a name-to-object association. Multiple descriptors may refer to one open-file description and thus share a file offset. Race-safe constrained lookup requires kernel-enforced resolution policies rather than concatenating a trusted directory prefix with user input.

## Worked constructed investigation

A program creates an output under /trusted/data but naively appends ../../outside to a user-supplied filename. This escapes the intended namespace. openat2 RESOLVE_BENEATH or RESOLVE_IN_ROOT can constrain traversal under documented assumptions, whereas string prefix tests cannot reliably handle symlinks.

## Executable or experimental reconstruction procedure

Draw the chain process fd -> open-file description -> dentry/inode -> filesystem object. List required rights, directory fd, mount assumptions, symlink policy and TOCTOU hazards. Future host validation must run read-only mapping tests on an isolated filesystem fixture.

## Adversarial/negative case

A symlink target can change between path validation and open. A renamed directory invalidates naive path-string authorization. A file descriptor is a process-specific number and cannot independently authenticate the target object.

## Failure boundaries, unknowns and acceptance holds

No filesystem driver, mount namespace, credential checks, real openat2 calls or malicious path traversal experiments.

## Exact-source links and dependent knowledge

Bibliographic pointers: VFS (https://docs.kernel.org/filesystems/vfs.html), OPENAT2 (https://man7.org/linux/man-pages/man2/openat2.2.html), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: software-design-patterns-atlas, cryptographic-protocols-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
