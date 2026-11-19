# Chapter 59 — Manufacturing evidence required to move from NAND models to physical processors

**ATLAS FORGE — original 15-node federation, Computer Architecture v0.4.0**

**Evidence:** original scientific/engineering reconstruction and finite software comparisons only. No authenticated publisher original, independent expert review, transistor timing library, fabricated CPU or certified boot hardware.


## Physical dependency ladder
The knowledge necessary to construct a physical computer spans materials, devices, fabricated gates, storage, clocks, interconnect and the full machine's observable behavior. A symbolic NAND netlist provides logic but no transistor-level electrical implementation. The Electronics Atlas models capacitance, MOSFET current, timing windows and memory retention under explicit approximations. The Manufacturing Atlas provides process dependencies, metrology, sample-size uncertainties, process capability and evidence gates. These must be linked by exact revisions, not assumed as already measured.

A plausible acceptance process must acquire independent physical evidence for material identity, geometry and doping, dielectric/oxide properties, transistor I–V/C–V across corners, gate transfer, delay and noise margins, clock/reset behavior, memory read/write retention, actual boot ROM programming, power integrity, thermal performance, and hardware instruction traces. Record instrument serials, calibration, raw samples, uncertainty, fixture layout, transport hashes and independently adjudicated negative results.

## Challenge and missing proof
The existing manufacturing-to-computer challenge can execute an AT8 software program and identify which of these physical evidence types are missing. A future laboratory may provide data for those stages, but a self-authored string like `calibrated=True`, a matching SHA-256 for user-provided metadata or a numerical test log is not a calibrated transistor measurement. Do not allow metadata assertions to automatically clear physical acceptance gates.

## Falsification and release gate
A valid gate-level NAND computation that fails measured voltage margins, measured setup/hold or ECC data retention is a failed physical reconstruction despite passing all software tests. Distinguish computational correctness, document provenance, physical observation and independent scientific acceptance in the final ledger. No fabricated processor, certified PDK or secure boot firmware is claimed by this v0.4 edition.

## Equation, implementation, and provenance

- **Key relation:** `hardware acceptance requires calibrated electrical, timing, retention and manufacturing evidence`.
- **Reference algorithm:** `v04_gatelevel.gate_delay_bounds; manufacturing_atlas v0.2 evidence lattice`.
- **Units:** volts, amps, seconds, Kelvin, geometry and uncertainties.
- **Cross-domain prerequisites:** original Electronics & Semiconductors, Manufacturing, Mathematics & Physics and Computation nodes, through their exact-revision Atlas records.
- **Required external validation:** primary source transport/authenticity, human scientific review, and calibrated device/processor measurements remain open gates.
- **Relevant official-source orientation:** MIT 6.004 Computation Structures and NIST SP 800-193. Sources are pointers only; no publisher-original PDF bytes have been locally authenticated in this edition.

**Reconstruction rule:** do not convert a plausible algorithm, finite test, or digest into a claim that a circuit was fabricated or a physical processor independently verified.
