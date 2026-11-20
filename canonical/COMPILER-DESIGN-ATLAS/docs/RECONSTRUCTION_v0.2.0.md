# Compiler v0.2.0 offline reconstruction

The original 24-node federation remains intact. First run the 15 v0.1 unit tests, then all 26 current tests, then both independent seeded laboratories. Verify the parser agreement, register code semantic equivalence, control-flow must-def checks, and deliberately bad programs. Reconstruct the exact whole archive using the historical Compiler v0.1 archive and delta. Never substitute a standalone node for that full federation.

Rebuild from source: implement grammar levels C/A/M/P independently; define the 14 typed-register opcodes and a forward must-defined dataflow verifier; run AST, stack and register interpreter agreement on valid and trapping programs.

Limit: no executable machine code, link format, real memory model, external ABI, real-system security or scientific peer review.
