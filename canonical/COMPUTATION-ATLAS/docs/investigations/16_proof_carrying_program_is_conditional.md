# Investigation 16 — A type-checked program may still compute the wrong answer

**Origin:** conceptual formal-methods counterexample. An integer function has a valid input and output type but returns 1 for every input, including cases whose specification demands a different value. Type correctness does not imply functional correctness relative to the human requirement.

**Evidence needed:** an explicit operational semantics, a formal precondition/postcondition, and a small independently trusted checker. Hoare logic and proof-carrying software can establish properties under these assumptions, but this library does not contain a certified theorem-proving kernel or type checker. No real compiled binary was formally verified.
