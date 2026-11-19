# Chapter 29: Setup, hold, clock skew, and timing closure

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Edge convention and proof obligations
Consider one launch register clocked at time 0 and one capture register clocked at time Δ (positive capture-minus-launch skew). The next capture edge is T+Δ. The latest data reaches the destination at t_cq,max + t_comb,max. Safe setup requires latest arrival ≤ T+Δ−t_setup−u_setup. The earliest data arrives at t_cq,min+t_comb,min; safe hold requires earliest arrival ≥ Δ+t_hold+u_hold. The equations above are these inequalities rearranged as slacks. Positive capture skew eases setup but makes hold harder.

The model refuses inconsistent minimum/maximum bounds and exposes both slacks separately. A circuit cannot be judged safe using only maximum delay. Negative slack is a violation of the declared assumptions, not a number to round up.

## Worked investigation
Take T=10 ns, t_cq[min,max]=[1,2] ns, combinational[min,max]=[2,4] ns, setup=1 ns, hold=0.5 ns, and zero skew/uncertainty. Setup slack=3 ns and hold slack=2.5 ns. With positive 2 ns capture skew, setup slack becomes 5 ns but hold slack drops to 0.5 ns. Now add enough skew/uncertainty to make hold negative; accepting the setup margin alone would be unsafe.

## Limits
This is single-clock, one-cycle static timing, not a multi-clock signoff engine. Actual gate delay tables, clock tree jitter, launch/capture correlations, input-output constraints, metastability and silicon process/thermal corners are not supplied. Measurement across chips and corners would be needed before asserting any maximum clock rate.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `synchronous_setup_hold`.
- **Governing relation:** `S_setup=T+skew−t_setup−u_setup−t_cq,max−t_comb,max; S_hold=t_cq,min+t_comb,min−skew−t_hold−u_hold`.
- **Units:** seconds.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
