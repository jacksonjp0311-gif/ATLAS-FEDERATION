# 17 — Drivers, device registers, IRQs, DMA and IOMMU trust boundaries

**ATLAS FORGE · Original 30-domain priority #15 · OS Internals scoped offline technical reference v1.0.0**

## Scientific/engineering question

What contracts connect interrupt-driven devices to kernel memory without arbitrary device DMA access?

## Assumptions and explicit model boundary

A device driver binds to identified hardware, maps device resources, handles interrupts, and may direct DMA to memory buffers with platform-dependent cache and IOMMU requirements. A device can be buggy or malicious. No actual hardware register access is attempted.

## Mathematical law or invariant

DMA_allowed(device,address,length) := mapped_IOMMU_domain AND bounds(address,length) AND lifetime_pinned AND coherent_ordering_contract.

## Derivation and operational interpretation

The host kernel enumerates buses and devices, chooses drivers, assigns memory-mapped I/O and interrupt resources and establishes DMA mappings. The CPU and device have separate agents for memory ordering. A correct descriptor ring requires ownership and memory barriers so the device does not read partially initialized commands. An IOMMU can restrict DMA to an assigned physical/IOVA range, but software setup errors remain possible.

## Worked constructed investigation

A device is allowed a 4 KiB DMA buffer at address 0x100000. Descriptor length 8192 extends beyond the mapping and must be rejected or segmented. If a driver frees the buffer while DMA remains active, an unrelated kernel object may be overwritten. A checksum cannot prevent that memory corruption.

## Executable or experimental reconstruction procedure

Define a mock descriptor structure: device ID, IOVA base, length, direction, generation and completion token. Enumerate zero, oversize and stale generation cases. Later build a separate user-approved emulated device lab before attempting actual DMA or interrupt configuration.

## Adversarial/negative case

Accepting device-reported lengths without bounds lets DMA overwrite unrelated memory. Missing synchronization at disconnect allows a stale interrupt callback to dereference a freed driver object.

## Failure boundaries, unknowns and acceptance holds

No IOMMU or device emulation, PCIe bus tests, actual USB/network/block drivers, hardware interrupts, DMA coherency verification or real fault containment.

## Exact-source links and dependent knowledge

Bibliographic pointers: DEVICE_MODEL (https://docs.kernel.org/driver-api/driver-model/overview.html), GENERICIRQ (https://docs.kernel.org/core-api/genericirq.html), MEM_BARRIER (https://docs.kernel.org/core-api/wrappers/memory-barriers.html)

Cross-domain prerequisites: electronics-semiconductors-atlas, manufacturing-atlas. Exact immutable record revisions are sealed into the shared Atlas relation store. A citation pointer is not publisher-byte authentication or scientific peer review.

**Units:** pages, bytes, ticks, cores, cycles or dimensionless logic as specified. **Real host measurements:** none. **External expert review:** not performed.
