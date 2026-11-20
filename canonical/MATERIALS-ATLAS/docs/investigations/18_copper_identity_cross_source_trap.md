# Investigation 18 — Two records named copper are not interchangeable

**Input A:** NIST StRD Hahn1, a numerical benchmark that reports 236 experimental observations and certified nonlinear least-squares parameters. It is used here to check the implementation of regression and residual calculations. The local capture is a checked transcription; the response numerical scale is unresolved.

**Input B:** NIST Chemistry WebBook copper solid-phase Shomate compilation, which reports Cp, relative H and S across 298–1358 K, using a published thermodynamic fit. It is not the same test and does not measure the Hahn1 regression response.

A naive keyword router could select both because they mention copper and temperature, then blend them into a synthetic material constant. The Atlas forbids such an inference: the two evidence types, response dimensions, data provenance and material-state qualifications differ. They are separately source-linked records and are meant to be retrieved with their qualifiers and exclusion criteria.

**Demonstration:** request a change in molar enthalpy of pure solid copper from 400 to 900 K. The WebBook fit yields approximately 13.3665 kJ/mol. Hahn1 cannot answer that request because its benchmark response is not molar enthalpy and its numeric scale is not authenticated. Conversely, requesting the residual pattern of the Hahn1 regression should not invoke WebBook heat-capacity coefficients.

**Required records:** type of measurement/compilation, physical quantity and units, phase, composition, temperature range, source inspected section, source-release hash (if original bytes exist), local capture hash, calculation implementation, and flags for incomplete source authentication. A correct shared navigation system must carry this information intact after all 30 domains are built. This checkpoint does not implement or test Bitwork routing.
