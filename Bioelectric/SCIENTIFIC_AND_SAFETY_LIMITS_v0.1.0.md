# Bioelectric Atlas — explicit scientific/safety acceptance boundary

The new node provides mathematical models of ion equilibrium, membranes, passive cables, historical squid-axon HH kinetics, an abstract excitability oscillator, ideal digitization and inert passive dummy circuit impedance.

**It is not** a medical device, diagnosis aid, person-specific biological model, certified laboratory instrument, safe therapeutic stimulator, physiological implant, or demonstration of living-tissue reproduction.

### Current gates

| Gate | Evidence | Current acceptance |
|---|---|---|
| Dimensional SI/ideal electrochemistry | Analytic identities, finite tests | Software scope only |
| Passive cable and leak-charge balance | Independent conservation tests and discretization bounds | Software scope only |
| Historical squid HH rates | Stable vtrap rate evaluation, finite integration tests | Software scope only |
| FitzHugh–Nagumo toy model | Analytic first derivatives, RK4 finite checks | Software scope only |
| Electrode dummy impedance | Passive linear RC algebra, imaginary/limiting cases | Software scope only |
| ADC and synthetic noise | Ideal quantization, aliasing, deterministic traces | Software scope only |
| Primary source original bytes | Not acquired/authenticated | **HOLD** |
| Calibrated live cell/tissue experiments | Not performed | **HOLD** |
| Medical device electrical safety and ethics | Not designed, reviewed or approved | **HOLD** |
| Independent qualified scientific review | Not performed | **HOLD** |
| Full domain v1 scientific acceptance | Not established | **HOLD** |

### Forbidden inference

A matching synthetic trace cannot be promoted into claims about a patient's health, a safe applied current, a regenerative effect, or an actual measured membrane. An electrode-equivalent circuit is a **non-biological passive dummy**, not equipment to attach to humans or animals. Use certified equipment and qualified professionals for any future biological measurement or safety-critical deployment; legal and ethics approvals must precede regulated experimentation.

### Counterexamples to preserve

A negative concentration, singular membrane equilibrium, oversized explicit time step, nonfinite voltage, or invalid gate probability must be refused rather than silently truncated. A discrete analog of a membrane capacitor does not confer calibrated electrical properties on a physical structure. A checksum records byte identity; it cannot independently authenticate scientific truth.
