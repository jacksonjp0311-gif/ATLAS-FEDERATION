# Chapter 49 — DRAM charge decay, sense thresholds and refresh policy

**ATLAS FORGE — canonical Electronics & Semiconductors scoped-v1 candidate.**

## Reconstruction problem

A DRAM bit stores charge on a small capacitor. A simple mathematical leakage model is Q(t)=Q₀ exp(−t/τ). With minimum readable charge Q_min, the ideal refresh deadline is t_ref=τ ln(Q₀/Q_min), assuming Q₀>Q_min and known τ. This formula does not bound the actual worst-case retention time over process, voltage, temperature, disturbance, and distribution tails; real DRAM requires statistical characterization.

A destructive-read or charge-sharing model must additionally include the sense amplifier, bitline capacitance, access-device resistance, wordline timing, refresh serialization and error detection. A memory timing calculation without these dependencies cannot be promoted to a functioning DRAM design.

**Worked investigation:** for synthetic Q₀=10 fC, Q_min=2 fC and τ=1 ms, compute t_ref≈1.609 ms. Check that a query before 95% of the ideal deadline returns retained and after 105% returns not retained. Mark both outcomes as ideal mathematical prediction, not qualified retention.

## Implementable contract and falsification

- **Reference equation:** `Q(t)=Q0 exp(−t/tau); t_ref=tau ln(Q0/Q_min)`.
- **Dimensional quantities:** C, s; all inputs must name units, geometry, sign and material assumptions.
- **Reference implementation or dependency:** `dram_retention`. Run `python -m unittest discover -s tests -q` and the independent oracle with the exact recorded package revision.
- **Falsification:** a counterexample that violates the stated assumptions, creates a non-finite intermediate or returns an unjustified deterministic result must be reported as a model limitation or rejected input, never silently corrected.
- **Evidence grade:** constructed mathematical and numerical example only. No authenticated original publisher file, physical wafer/device data, certified process design kit, independently signed expert review or fabricated CPU is supplied by this chapter.

## Interfaces to the original ATLAS FORGE federation

The mathematical models use the pre-existing Mathematics & Physics node for SI, continuum equations, numerical verification and nonlinear charge transport; the Chemistry, Materials, Energy, Computation and Control nodes supply prerequisite context. References to other nodes are navigation or prerequisites, not evidence that those domains were experimentally validated. The canonical thirty-domain roadmap is unchanged, and Electronics remains a node of the same shared Atlas schema.

**Bibliographic reference ID:** `MIT-6374` from the source register. References identify public publication pages, not archived authenticated originals.
