# ATLAS FORGE — Computer Architecture scoped-v1 acceptance gates

**v0.1 is the initial content/implementation kernel, not scientific v1.0 acceptance.**

| Gate | Required evidence | Current status |
|---|---|---|
| Original ISA contract | fully specified encoding, flags, ROM/RAM, branches, IO, traps | Software kernel implemented |
| Independent software models | atomic spec and separate four-stage microcycle executor | Implemented; finite tests required |
| Independent oracle | separate byte interpreter plus exhaustive 8-bit arithmetic and random programs | Implemented; finite test receipt |
| Assembler and binary round-trip | bounded two-pass assembler, disassembler, labels and rejection cases | Implemented |
| Offline reconstruction | Python 3.10+, no service/model dependencies, clean wheel and ZIP recovery | Must be verified on sealed release |
| Canonical federation continuity | original 14 nodes unchanged, original 30-domain roadmap untouched, exact revisions | Must be audited on sealed release |
| Verified physical gates | fabricated/transistor or discrete-gate datapath with measured timing/power | HOLD |
| Measured memory/IO | RAM retention, setup/hold, synchronizers, ports, clock/reset | HOLD |
| Authenticated primary publisher originals | lawful original source bytes, revision, rights and page mappings | HOLD |
| Independent scientific/engineering review | external qualified reviewer, signed findings and replication | HOLD |
| Complete computer/OS/AI | compiler, interrupts, privilege, OS/runtime, physical CPU executing binary | HOLD |

The main 30-domain roadmap does NOT list Computer Architecture & Digital Hardware as an original named slot. It is a supporting enabling node added without revising the queue. Bitwork routing stays deferred until domain-content completion, followed by integrated validation and desktop transfer.
