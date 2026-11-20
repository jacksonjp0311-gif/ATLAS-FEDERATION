# 26. Heat flow, interfaces, and thermal design boundaries

## The governing model

For a steady one-dimensional plane wall with isotropic scalar conductivity `k` and no internal generation, Fourier's law gives `Q = k A ΔT/L`. Written as a thermal circuit, one layer contributes `R=L/(kA)` with units K/W. Thermal resistances in *series* add. For a declared contact resistance Rc (K/W), `Q=ΔT/(Σ L_i/(k_i A)+Σ Rc)`.

This is an **engineering model**; it is not a measured conductivity or a heat-transfer experiment. It assumes that the layer cross-section and pathway are known, material conductivities are approximately constant in the temperature range, lateral leakage is negligible, and the specified contact resistances represent interface effects. Real components may have radiation, convection, phase change, porosity, anisotropy and transient heating; absent terms are not zero merely because the input omits them.

## Worked synthetic stack

Declare area `0.1 m²`, a `1 mm` copper-like conductive layer assigned `200 W/(m K)`, a `5 mm` insulating layer assigned `1 W/(m K)`, a contact resistance `0.3 K/W`, and applied temperature difference `50 K`. The model gives `R1=0.00005 K/W`, `R2=0.05 K/W`, total `0.35005 K/W`, and approximately **142.836738 W** of heat rate. Without the declared contact resistance, the predicted rate is about **999.001 W**. This large difference illustrates why surface finish, pressure, contact material and assembly conditions matter. The numbers are hypothetical, not tested values for a commercial thermal interface material.

## Measurement and model error

A conductivity value from a materials database is often measured at a stated temperature and microstructural condition. It may not represent a laminate, foam, coated part, grain-aligned crystal or specimen under compression. If conductivity varies with temperature, the exact 1D stationary law requires integrating `k(T)` and imposing the correct thermal boundary conditions; substituting a single catalogue value can bias the result. Contact conductance can change over cycles or with mounting pressure, and a thermal interface does not automatically have a transferable scalar k. Never infer contact resistance from a polymer bulk conductivity without actual interface measurement.

## Uncertainty and decisions

Treat geometry, material composition, conductivity fit, interface resistance, heat source, environmental boundary and sensor positioning as different error contributors. Changing a design from one material to another requires recalculation with representative property distributions and conditions, not merely comparing single conductivity numbers. The new calculator reports the declared per-layer and total resistances and refuses nonpositive conductivities or missing layers. **It does not predict actual interface temperatures, thermal stress, equipment uptime, or a pass/fail decision.**

**Related material:** Chapter 08 on thermal transport, Chapter 14 on temperature-dependent properties, and Measurement Atlas on uncertainty budgets and calibration.
