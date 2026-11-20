# Computer Architecture — scoped software v1 readiness gates (v0.3.0)

**v0.3.0 is a bounded software and scientific-content research edition. It is not a scientifically accepted v1, a secure boot certification, or a fabricated processor.**

| Evidence gate | Current status | Required independent evidence |
|---|---|---|
| Versioned AT8 ISA unchanged | PASS, software | Exact original v0.1 encoded ROMs and instruction tests preserved |
| Boot image parsing and canonical bytes | PASS, finite tests | Source/header/payload hashes and invalid-input refusals |
| Simulated two-slot recovery | PASS, finite tests | Torn-write tests on actual nonvolatile media, authenticated anti-rollback |
| SECDED 1-/2-bit cases | PASS, finite tests | Physical memory cell error distributions and burst/redundancy testing |
| Conservative control graph | PASS, finite tests | Formal proof or appropriate bounded exhaustive model for larger control semantics |
| Structured source compilation | PASS, finite tests | Independent AST, atomic and microcycle comparison of complete observable state |
| Small write-through cache | PASS, software | Memory timing, coherence with DMA/other cores, physical cache design |
| Deterministic batch job receipts | PASS, host-side harness | Process privilege, preemption, memory isolation, I/O drivers and real OS runtime |
| Primary publisher documents | **HOLD** | Authenticated original transport bytes, rights, source-to-equation mapping |
| External independent scientific review | **HOLD** | Qualified reviewer identity, negative results, signed independent reproduction |
| Hardware/FPGA/discrete CPU execution | **HOLD** | Measured I/O and clock signals, physical build and test receipts |
| Firmware cryptographic root of trust | **HOLD** | Trusted keys, signing, secure storage, revocation, power-failure testing |
| All 30 original scientific domains | **HOLD** | Complete original domain program, preserving roadmap and release history |

**Next:** deep Computer Architecture content toward scoped v1; then Compiler Design and Operating Systems as their own planned scientific domains. Bitwork routing only after the content stage, followed by integrated evaluation and desktop transfer.


# v0.4.0 engineering-content increment

**Passed candidate evidence:** deterministic eight-bit NAND datapath netlist, 3-valued unknown logic, arithmetic/refinement checks at retirement, Harvard ROM/RAM typed bus, parity detection with demonstrated two-bit blind spot, bounded conditional-fair arbiter, canonical source→assembler→AT8R/3 boot→execution→gate certificate. A total of 12 new chapters and independent constructed checks are supplied.

**Scientific/HW acceptance HOLD:** authenticated original publisher documents/rights, qualified independent reviewer, transistor-level gate library, calibrated timing/clock/memory, physical ROM A/B atomicity, signed firmware origin and a fabricated working CPU. Functional tests and digest consistency do not close those gates. The original thirty-domain knowledge roadmap is unchanged; Bitwork routing remains deferred.
