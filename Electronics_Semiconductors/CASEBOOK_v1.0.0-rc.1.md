# Electronics & Semiconductors — Constructed v1 candidate investigations

Every numerical input below is synthetic. Cases verify equations under assumptions, not physical samples. Run `PYTHONPATH=. python evidence/independent_oracle_v1rc.py` and `python -m unittest discover -s tests -q`.

## Investigation 01 — SI thermal voltage

**Constructed inputs:** 300 K; exact q and kB.

**Reference result:** 0.0258519997864 V.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 02 — MOS oxide, 1 μm² gate, 10 nm dielectric

**Constructed inputs:** parallel plate; epsilon_r=3.9 assumed.

**Reference result:** 3.45313324699e-15 F.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 03 — Body effect at 1 V reverse bias

**Constructed inputs:** V_T0=0.6 V, gamma=0.3 sqrt(V), phi_F=0.3 V.

**Reference result:** 0.747094318448 V.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 04 — NMOS linear current

**Constructed inputs:** VGS=1 V, VDS=.25 V, Vt=.5 V, k=1 mA/V².

**Reference result:** 9.375e-05 A.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 05 — NMOS saturated current

**Constructed inputs:** same transistor model at VDS=1 V.

**Reference result:** 0.000125 A.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 06 — Ideal diode at 0.3 V

**Constructed inputs:** Is=1 pA, ideality 1.5, T=300 K.

**Reference result:** 2.28908774949e-09 A.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 07 — Diffusion surface concentration

**Constructed inputs:** Q=1e16 m^-2; D=1e-14 m²/s, t=10s.

**Reference result:** 1.78412411615e+22 m^-3.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 08 — Four-point sheet resistance

**Constructed inputs:** infinite equal-pitch four-probe sheet, 10mV/1mA.

**Reference result:** 45.3236014183 Ω/square.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 09 — Hall density

**Constructed inputs:** one majority carrier, I=.01 A, B=.5 T, t=.001 m, VH=.01 V.

**Reference result:** 3.12075453723e+21 m^-3.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 10 — Thermal RC at t=1s

**Constructed inputs:** step power 2W; Rth=10 K/W; Cth=.1 J/K.

**Reference result:** 312.642411177 K.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 11 — DRAM ideal refresh deadline

**Constructed inputs:** Q0=10fC, Qmin=2fC, tau=1ms.

**Reference result:** 0.00160943791243 s.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 12 — Poisson defect-free die yield

**Constructed inputs:** D=.2 defects/cm², A=3 cm², any defect fails.

**Reference result:** 0.548811636094.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 13 — Overlay sum worst-case error

**Constructed inputs:** bounds 1,2,3 nm; target 40nm.

**Reference result:** 6 nm.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Investigation 14 — Microprogram 5 + 7

**Constructed inputs:** original 8-bit accumulator state machine, NOT fabricated CPU.

**Reference result:** 12 stored; accumulator 15.

**Reproduce:** reference functions in `electronics_atlas/v1_scoped_models.py`; independently cross-check with `evidence/independent_oracle_v1rc.py` where available. Compare units, relevant conservation or monotonicity, and invalid-domain behavior. **No real observation** is asserted.

## Negative controls

1. Zero magnetic field or Hall voltage is non-identifiable; a carrier density number must not be invented.
2. Negative oxide thickness, zero positive temperature or unsupported negative V_DS are outside reference model domains.
3. In a non-unique CMOS inverter operating point or an unqualified SRAM bitcell, do not return an invented stable analog voltage.
4. Uncharacterized DRAM retention and die yield are not manufacturing guarantees.
5. An invalid machine opcode, an odd jump address, or nonterminating program is rejected or explicitly bounded.

## Evidence vocabulary

**Mathematical derivation:** equation under declared assumptions. **Numerical test:** finite calculation checked against a separate implementation. **Bibliographic source:** publisher reference URL without authenticated bytes. **Experiment:** requires actual measurements, independent instrumentation and uncertainty controls, currently absent. **Independent peer review:** requires a qualified external reviewer, currently absent.
