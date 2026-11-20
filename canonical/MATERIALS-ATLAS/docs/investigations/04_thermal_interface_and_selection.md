# Investigation 04 — Thermal mismatch versus actual interface risk

**Evidence type:** Author-constructed thermal example. Reference: [NIST Engineering Metrology Toolbox FAQ](https://emtoolbox.nist.gov/faq/faq.asp).

Two illustrative materials have scalar thermal-expansion coefficients `23e−6 /K` and `12e−6 /K`, assumed constant over a `+60 K` change. The free strain difference is `(23−12)e−6 × 60 = 660 microstrain`. This algebra does not provide an interface stress or an engineering failure criterion. Actual constraint, bond, geometry and temperature-dependent properties are missing.

A robot housing may need thermal cycling life, oxidation protection, mechanical fatigue resistance, dimensional tolerance and assembly fit in addition to stiffness. A table of room-temperature moduli will not settle the design. The correct comparison ledger includes property origin, tested range, thermal history and load path, plus what qualification test must be run before deployment.

A materials selection answer from this first Atlas edition should therefore read: “The assumed pair has a modeled free thermal mismatch of 660 microstrain; component-level reliability cannot be determined from these inputs.” The latter statement is as essential as the numerical result.
