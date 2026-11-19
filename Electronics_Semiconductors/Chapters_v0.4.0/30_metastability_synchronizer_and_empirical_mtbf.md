# Chapter 30: Metastability, synchronization, and empirical failure envelopes

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Why deterministic digital proofs stop at clock-domain boundaries
A clocked storage element can enter an analog metastable region if an input changes near its aperture. No finite digital-time bound guarantees resolution for every possible event. The correct engineering approach is to reduce risk through synchronizer stages and protocol design, not to declare the event impossible.

An illustrative empirical tail model uses two **measured device parameters** T0 (seconds) and τ (seconds): the event rate is approximately f_clk f_data T0 exp(−T_res/τ), so MTBF is its reciprocal. Work in logarithms to avoid overflow at large resolution times. This equation assumes a stationary input-toggle process, appropriate synchronizer topology, suitable environmental calibration and a regime where a fitted exponential model is justified. It is not universally predictive.

## Worked investigation
For a *hypothetical* example with f_clk=10 MHz, f_data=1 MHz, T0=1 ns, and τ=30 ps, increasing available resolution from 1 ns to 2 ns raises log10(MTBF) by ΔT/(τ ln10)≈14.48 orders of magnitude under this formula. These parameters are invented demonstration inputs, not characterized semiconductor data; the result must not be interpreted as a silicon reliability guarantee.

## Reconstruction protocol
Record the flip-flop family, process/corner, clock tree, supply, temperature, output load and metastability characterization method before claiming an empirical MTBF. For multi-bit buses, independently synchronizing each bit is insufficient to guarantee coherent atomic capture. Use a handshake, Gray-coded pointer with proper constraints, or asynchronous FIFO under specified assumptions. The reference calculation deliberately requires explicit T0 and τ rather than defaulting to misleading constants.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `synchronizer_mtbf_log10`.
- **Governing relation:** `MTBF≈exp(T_res/τ)/(f_clk f_data T0); log10(MTBF)=T_res/(τ ln10)−log10(f_clk f_data T0)`.
- **Units:** hertz and seconds.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
