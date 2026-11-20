# Investigation 14 — The interface dominates a two-layer heat path

A hypothetical device has two layers conducting in one dimension over 0.1 m². Layer 1 is 1 mm thick with assigned conductivity 200 W/(m K); layer 2 is 5 mm thick with assigned conductivity 1 W/(m K). The applied temperature difference is 50 K, and a declared contact resistance is 0.3 K/W.

The resistances are `0.001/(200×0.1)=0.00005 K/W` and `0.005/(1×0.1)=0.05 K/W`. Total resistance is **0.35005 K/W**, giving **142.8367376 W** by the steady 1D model. Without the contact resistance, the same geometric formula would give about 999 W: a warning against treating catalogue bulk conductivity as interface conductance.

These are chosen numbers, not an actual thermal-interface test. Neither thickness nor conductivity is known to represent a specific product. Heat flow can change with thermomechanical contact, temperature-dependent conductivities, convection, radiation and side leakage. The calculator cannot infer a device safe temperature or prevent a burn, fire or equipment failure. It can highlight which missing measurement is likely important.

A real investigation would record sample thickness under actual compression, thermal-contact conductance at assembly pressure, temperature profile, contact area, environmental boundary temperatures, sensor position and calibration, dissipated power, transient history and repeated mounting. Anisotropy or a three-dimensional heat field may require a different model entirely.

The calculation rejects zero thermal conductivity, negative thickness, or missing layers and returns model assumptions with the numeric result. The result can inform a test plan but does not certify a component.
