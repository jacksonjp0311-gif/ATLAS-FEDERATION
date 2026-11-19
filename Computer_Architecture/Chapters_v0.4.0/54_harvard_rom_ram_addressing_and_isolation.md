# Chapter 54 — Harvard ROM/RAM separation and addressing boundaries

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Memory separation as an architectural invariant
AT8 is an educational Harvard machine: program ROM is immutable during normal execution and is stored separately from 256 bytes of writable data memory. The program counter addresses fixed two-byte instructions and must be even. RAM read and write addresses are byte indexes. The ISA also exposes four abstract input and output ports; these are **not** memory-mapped I/O and may not be silently reinterpreted as such.

The new reference bus provides distinct `fetch`, `read`, and `write` entry points. A ROM write is refused. All operations validate types and bounds before modifying memory; an out-of-range address must not cause a partial write or trace event. The transcript can be deterministically serialized to JSON and hashed, but a hash proves only internal consistency if its expected digest is anchored elsewhere.

## Worked case
Assemble `LDI R0,1; HALT`, fetch the first two ROM bytes at PC=0, write byte 255 at RAM address 0, and read back the same value. An odd PC=1 or RAM address 256 is rejected. Compare the transcript SHA-256 from two independent fresh runs with identical inputs. Deliberately request a ROM modification to demonstrate that the architecture has no such instruction.

## Verification boundary
A simulated read-only ROM cannot establish flash write protection or secure boot. Real hardware needs memory isolation, power/clock sequencing, permission logic, bus arbitration and timing measurements. The source-to-boot chain should retain provenance, a known trusted hash or signature, and measured device access traces before claiming that these abstractions correspond to physical components.

## Equation, implementation, and provenance

- **Key relation:** `ROM fetch PC even, 0<=PC+1<ROMlength; RAM 0<=address<256`.
- **Reference algorithm:** `v04_memory.HarvardBus; isa.validate_rom`.
- **Units:** bytes, addresses and transaction events.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
