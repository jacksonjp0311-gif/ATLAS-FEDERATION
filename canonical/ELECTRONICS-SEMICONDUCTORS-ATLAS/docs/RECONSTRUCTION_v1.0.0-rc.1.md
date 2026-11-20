# ATLAS FORGE — Electronics to Computer: reconstruction chain v1.0.0-rc.1

This is a verified-content **software candidate**, not a physically reconstructed semiconductor manufacturing plant. The original single 13-node federation is the source of truth.

## Traceable capability graph

1. **Measurement foundation:** BIPM SI, q, kB, dimensional conversion, instruments, calibration metadata, measurement uncertainty (Measurement, Mathematics & Physics).
2. **Physical matter:** chemical purity, crystal structure, dielectric properties, doping, diffusion, defects and process effects (Chemistry, Materials).
3. **Semiconductor devices:** ideal p-n junctions, MOS capacitors, NMOS/CMOS equations, contact behavior, leakage, body bias, I–V/C–V metrology (Electronics).
4. **Manufacturing dependencies:** mask definition, registration, oxidation/deposition/etch/doping, thermal budgets, interconnect, test structures, yield and contamination controls (**requires future Manufacturing Atlas**).
5. **Logic circuits:** inverter transfer, NAND arithmetic, noise windows, clock paths, setup/hold, unknown logic and metastability uncertainty (Electronics).
6. **State and information:** SRAM/DRAM assumptions, bounded registers, ECC, data retention, memory collision handling, programmable 8-bit state machine (Electronics → **Computer Architecture**).
7. **Computing and AI:** ISA, assembler, boot, compiler, OS, model algorithms, scientific evaluation, reproducible memory/tool systems (**future domain nodes**).

## Fully reproducible *software* vertical slice

- A finite MOSFET current equation and oxide capacitance provide bounded electrical predictions under specified assumptions.
- Logical NAND truth tables support arithmetic primitives; timing and unknown states are represented explicitly.
- The 8-bit software machine executes a small program, e.g. `LDI 5; ADD 7; STORE 0; XOR 3; HALT`, leaving RAM[0]=12 and accumulator=15.
- A separate oracle exhaustively verifies the 8-bit addition program over all 65,536 pairs. It does **not** prove physical transistor implementation.

## Hardware acceptance chain still absent

Create geometry and materials specifications, reproduce process chemistry, build and measure test diodes and capacitors, record MOS I–V/C–V curves and temperature, fit calibrated parameters with uncertainties, characterize cell noise/retention and clock timing, design and verify a simple silicon or discrete-logic prototype, test it against an independent golden software trace, and preserve design/layout/manufacturing files with licenses and hashes. None of those physical claims is made by this release.

## Recovery

Use the release's `START_HERE.md` and `RESTORE_ATLAS_FORGE_ELECTRONICS_V1RC.py` with the exact v0.4.0 predecessor archive. Preserve `DOMAIN_QUEUE.json` unchanged. The source-closed Atlas package is navigable through `AtlasStore`, not a Bitwork router. Bitwork remains deferred until all domain content is complete.
