# 16. Clock timing from digital control to physical register requirements

**ATLAS FORGE — original canonical federation / Computer Architecture & Digital Hardware v0.1.0.**

**Evidence classification:** original engineering reconstruction, finite reference calculations, deterministic test vectors and bibliographic navigation. **Not** a fabricated computer, production ISA or independently reviewed silicon design.

## Reconstruction question

Clock timing from digital control to physical register requirements. The goal is to explain the necessary concepts, state transitions, units, negative cases and verification conditions in a form that is independently reproducible offline.

## Derivation and architectural reasoning

Symbolic FETCH/DECODE/EXECUTE/COMMIT stages are not physical clock cycles. A real synchronous implementation requires a critical-path analysis linking register clock-to-Q delay, combinational logic propagation, setup time, clock skew and uncertainty. The corresponding hold constraint uses contamination/minimum delays and may fail even at a low clock frequency. The Electronics node already contains independently testable one-clock timing inequalities and explicit unknown-state behavior on setup/hold aperture violations. This Computer Architecture node uses those as exact-revision dependencies rather than claiming a Python microstep has an electrical duration.

A physical implementation would need a cell library calibrated over process, supply and temperature, extracted interconnect parasitics, clock tree and reset behavior, asynchronous I/O synchronization, realistic memory delays, and power/thermal budgeting. A clock-frequency claim without those inputs is unsupported. For reconstruction, map each AT8 micro-operation onto a register/ALU/memory control graph, identify its longest and shortest sensitized timing paths, and require measured bounds before signing off. A valid software trace can coexist with a physically unstable circuit.

## Executable contract and invariants

**Governing statement:** `T+skew >= t_cq_max+t_pd+t_setup+uncertainty; t_cq_min+t_cd >= t_hold+skew+uncertainty`.

**Implementation:** `Electronics v0.4 timing context + AT8 microstate DAG (no measured clock)`.

**Relevant dimensions:** seconds, hertz, voltage, temperature. Interpret byte addresses, machine cycles and SI electrical units separately. Digital flags and byte values are not measurements of physical voltages or time.

The reference is a bounded contract: valid inputs produce specified machine states, invalid encodings produce explicit refusals, and all output events are reproducible from ROM and input tapes. An independent implementation or test must verify the state transition rather than solely reusing this source code. The original shared exact-revision Atlas graph identifies this concept, its equation, its procedure and the assumptions that limit its use.

## Worked reconstruction investigation

Use the Electronics timing reference with hypothetical values, then mark the clock-speed field of the AT8 evidence record as unverified. Do not invent a frequency from its four microstates.

A researcher should record input bytes, program counter and register states before/after the relevant instruction, compare with a separately coded oracle, retain negative cases, and include the SHA-256 of the exact ROM. No fabricated hardware measurement should be inferred from these software results.

## Counterexamples, uncertainty, and failure boundaries

No clock-tree design, metastability characterization, SPICE model, standard-cell synthesis or STA signoff is included here.

A numerical or Boolean verification can establish reproducibility of the *chosen model* on tested inputs; it does not independently establish the adequacy of a manufacturing process, a circuit's electrical timing, the identity/rights of a source document or peer-reviewed scientific truth. Lack of those inputs must be recorded as a missing evidence condition.

## Source provenance and original federation dependencies

- **Bibliographic orientation ID:** `MIT-65900-2026`, official pointer: https://csg.csail.mit.edu/6.5900/lecnotes.html. **Publisher original bytes were not downloaded/authenticated or redistributed in this edition.**
- **Foundational dependencies:** Electronics & Semiconductors (NAND, timing, memory), Manufacturing (calibration/process evidence), Mathematics & Physics (Boolean arithmetic and measurement equations), Computation (algorithms).
- **Preservation constraints:** original 30-domain queue unchanged; exact previous releases retained; this node is an auxiliary engineering dependency rather than a newly invented slot of that queue; Bitwork routing remains deferred until domain-content completion.
