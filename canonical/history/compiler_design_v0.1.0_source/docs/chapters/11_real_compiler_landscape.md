# Chapter 11 — From a toy compiler to real targets: LLVM, Wasm, RISC-V and CompCert

LLVM's intermediate language has SSA values and explicit control-flow blocks, but it also has nuanced semantics for poison, undef and freeze. A correct optimization must respect these semantics rather than assuming every integer arithmetic operation is pure mathematical arithmetic. For example, `nsw`-annotated addition has poison behavior when signed overflow occurs. This differs from Tiny-I32, which explicitly traps on overflow.

The WebAssembly Core Specification 3.0, released in November 2026, separates decoding, validation and execution. The Atlas validator's stack-type simulation illustrates the *shape* of this reasoning, but it validates only the educational opcode grammar and must not claim to validate actual Wasm modules. WebAssembly's stack typing, polymorphic control flow, memory and real binary format are not implemented here.

The current ratified RISC-V ISA reference is a source for eventually mapping target-independent IR to machine instructions. Real RV32I code generation must account for its actual instruction encodings, ABI, register allocation, integer arithmetic and calling conventions. A JSON stack machine is not RISC-V machine code.

CompCert demonstrates a much higher evidence bar by proving preservation of behavior for an officially specified subset of C across compilation passes using a proof assistant. Tiny-I32's finite oracle checks are **not** comparable to a proof of all compiler passes for a real language.

**Suggested scientific upgrade path:** v0.2 add a second independently executable backend and an SSA form with dominance and phi-node checks; subsequent versions add memory semantics and verified instruction selection on a bounded RISC-V subset. Avoid replacing evidence with a version label.
