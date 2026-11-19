# 14 — Write-ahead logging, ordering, fsync, namespace persistence and recovery

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

What is a committed transaction and which data can survive a crash under an explicitly specified storage model?

## Assumptions and explicit model boundary

The Python model stores a stable durable prefix and an unflushed volatile suffix. A flush moves every volatile record to the durable prefix; crash discards unflushed records. Actual drives, caches, filesystems and power-fail hardware do NOT guarantee this simplified atomic prefix behavior without additional evidence.

## Mathematical law or invariant

Recover(durable_log) = apply(write_sets of transactions with BEGIN and COMMIT in durable order); ack_after_flush -> logical durability only under the modeled flush contract.

## Derivation and operational interpretation

A write-ahead log separates intent from materialized state. Recovery scans durable entries and applies writes only after observing a matching commit. An uncommitted durable BEGIN/SET remains ignored. A commit appended to volatile buffers but acknowledged before a flush is not durable in this model. For file replacement, fsync(file) and fsync(parent_directory) are distinct obligations on Linux; rename namespace atomicity does not imply physical crash durability.

## Worked constructed investigation

Log has durable BEGIN(x),SET(x,a,1),COMMIT(x). Recovery sets a=1. If COMMIT(x) was only volatile at crash, recovery leaves a unchanged. If the directory update was never synchronized, the name of a newly created file may be lost despite fsync on file data, depending on platform and filesystem semantics.

## Executable or experimental reconstruction procedure

Run CrashJournal with commit-before-flush and commit-after-flush scenarios, crash and compare states. Independently scan the stable prefix using a second interpreter. Record exact flush points, device cache configuration and fsync error handling required for eventual physical tests. Avoid destructive power-cut experiments on user data.

## Adversarial/negative case

A transaction ID can be reused after reboot, causing a second side effect. A badly placed commit acknowledgment can claim data is durable when it is not. A checksum detects corruption but is not sufficient to repair or authenticate a damaged journal.

## Failure boundaries, unknowns and acceptance holds

No actual fsync, battery-backed write cache, power-loss test, filesystem ordering proof or production recovery certification.

## Exact-source links and dependent knowledge

Bibliographic pointers: FSYNC2 (https://man7.org/linux/man-pages/man2/fsync.2.html), RENAME2 (https://man7.org/linux/man-pages/man2/rename.2.html), OSTEP (https://pages.cs.wisc.edu/~remzi/OSTEP/)

Cross-domain prerequisites: distributed-systems-atlas, software-design-patterns-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
