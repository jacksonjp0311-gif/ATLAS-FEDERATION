# Chapter 27: Digital voltage thresholds and guaranteed noise windows

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Foundations and derivation
Binary digits are abstractions of analog voltage intervals, not fixed voltages. For a receiving gate, values no greater than VIL(max) represent low, and values no less than VIH(min) represent high. Voltages strictly between those two limits have no guaranteed binary interpretation. The driving gate's worst low output is VOL(max), and its worst high output is VOH(min).

For a high signal to be guaranteed valid after bounded noise of magnitude N, its lower bound VOH(min) − N must remain at least VIH(min); therefore N ≤ VOH(min) − VIH(min). For low signals, VOL(max) + N ≤ VIL(max), giving N ≤ VIL(max) − VOL(max). Take the minimum to obtain a symmetric conservative noise budget. The implementation rejects inconsistent ranges; it does not coerce an unknown input to 0.

## Worked investigation
Suppose VDD=3.3 V, VOL≤0.4 V, VIL≤1.0 V, VIH≥2.1 V, VOH≥2.9 V. The two static margins are 0.6 and 0.8 V. A measured input at 1.5 V lies between thresholds and must yield UNKNOWN, not a fabricated bit. A margin of 0 V is logically possible but admits no positive bounded noise.

## Failure analysis and reconstruction
There is no universal CMOS threshold; thresholds depend on process, supply, temperature and loading. Neither these intervals nor a static margin establish dynamic noise immunity, hysteresis, interconnect crosstalk, supply droop or immunity to radiation events. To reconstruct them physically, characterize low/high transfer limits over voltage, temperature and input transition rate; retain instruments, uncertainty and repeat traces. A source card without original publisher bytes is not measured evidence.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `digital_noise_margins, input_logic_level`.
- **Governing relation:** `NML = VIL(max) - VOL(max), NMH = VOH(min) - VIH(min)`.
- **Units:** volts.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
