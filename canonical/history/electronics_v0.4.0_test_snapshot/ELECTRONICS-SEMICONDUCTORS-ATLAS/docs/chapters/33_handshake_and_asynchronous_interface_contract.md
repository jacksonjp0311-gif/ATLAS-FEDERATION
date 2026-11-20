# Chapter 33: Four-phase handshake and asynchronous interface correctness

**ATLAS FORGE — Original canonical 13-node federation, Electronics & Semiconductors v0.4.0**

**Evidence classification:** original mathematical synthesis and bounded software verification. No calibrated physical transistor, tested wafer, authenticated source-document copy, or independent peer review.


## Asynchronous data transfer contracts
Two independent clocks cannot be assumed aligned. A four-phase return-to-zero request/acknowledge protocol is one way to define a causal exchange: requester asserts request while data is stable, receiver eventually asserts acknowledge, requester deasserts request, receiver deasserts acknowledge. Four logical phases are [00,10,11,01,00]. Explicit stateful validation rejects illegal orderings, rather than treating unordered transitions as a successful transaction.

The logical protocol **does not implement a physical synchronizer**. Its assumptions include appropriately synchronized control signals, data stability until acknowledged, monotonic return-to-zero behavior, no unbounded transport faults, and an explicit timeout/retry/error policy. The state machine cannot guarantee bounded metastability resolution, arbitration progress or data coherency across asynchronous buses by itself.

## Worked investigation
Starting in IDLE at 00, the request transitions 10 (REQUESTED), then 11 (ACKNOWLEDGED), then 01 (RETURNING), then 00 (IDLE). Attempting 00→11 skips the request stage and is rejected. Deasserting acknowledge before the requester drops request likewise violates the specified order.

## Reconstruction handoff
A measured implementation would instrument request/ack arrival times, metastable or missing transitions, control crossing constraints, data setup and failure injection, and would preserve timing/uncertainty logs. Later Computer Architecture must define the bus and memory ordering; later Manufacturing must supply a characterized standard-cell or discrete hardware implementation.

## Reference, limitations, and preserved evidence

- **Executable reference:** `electronics_atlas/v04_models.py` — `four_phase_handshake_step`.
- **Governing relation:** `(req,ack) state sequence: 00→10→11→01→00`.
- **Units:** binary logic state.
- **Previous editions:** 01–26 chapters retained as exact historical source.
- **Source register:** MIT OCW 6.004, Computation Structures (2009 lecture notes; 2017 annotated timing/metastability); OpenROAD public timing API. Citation/navigation only; original publisher transport bytes not authenticated here.
- **Validation:** new Python finite unit tests plus independently coded mathematical oracles; any remaining physical differences require measurement.
- **Audit boundary:** no fabricated transistors, no silicon device calibration, no guaranteed clock frequency, no physical CPU.
