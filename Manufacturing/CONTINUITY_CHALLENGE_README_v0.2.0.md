# Manufacturing → Computer: reconstruction challenge evidence report

Run `python evidence/reconstruction_challenge.py` **from the Manufacturing node inside the complete ATLAS FORGE federation**. It imports the actual retained Electronics `EightBitAccumulator` and verifies a small deterministic program. It then evaluates six physical manufacturing stages through the evidence gate.

The expected software fixture is accumulator `15`, RAM[0] `12`, five executed instructions. Twelve physical evidence types are **missing**, six physical stages remain **HOLD**, and independent physical certification is **false**. Synthetic evidence metadata can make the process graph structurally complete but **never** qualify a real machine, wafer, semiconductor or processor.

Independent replication: execute on a fresh restored archive; compare this report with `RECONSTRUCTION_CHALLENGE_REPORT_v0.2.0.json`. Record every absent instrument certificate, source-original, measured device curve, processing result, physical gate timing and hardware execution trace before attempting a real-world qualification.

This challenge intentionally represents an open technical-continuity problem, not a completed chip fabrication experiment. The first success is correctly identifying what is **not** yet supported by evidence.
