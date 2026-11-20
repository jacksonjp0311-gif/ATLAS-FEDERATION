# Electronics & Semiconductors — ten constructed investigations

Each case is generated from the executable reference kernels, **not** measured data.

1. Compute `thermal_voltage(300)` using exact k_B and q; explain why 300 K does not imply 0.7 V transistor threshold.
2. Verify `mass_action_carriers(1e21,1e16)` satisfies n p = n_i^2 and n-p = N_D-N_A.
3. Test telescoping `current_divergence_1d([0.2,0.5,1.5,1.2],0.1)`: sum over cells times spacing equals 1.0 A/m² boundary difference.
4. Estimate `built_in_potential(1e22,1e22,1e16,300)` and compare depletion width for 0 and -0.1 V applied bias.
5. Round-trip ±0.1 V through `diode_current` and `diode_voltage_from_current` with I_s=1e-12 A.
6. Compute geometric oxide capacitance for ε_r=3.9, A=1e-12 m², thickness=10 nm and audit the assumption of no quantum corrections.
7. Show ideal MOSFET current is continuous at V_DS = V_GS-V_T, and zero below threshold.
8. Derive RC t_50 = R C ln(2), check code at R=1 kΩ C=1 nF, then calculate 10–90% rise time.
9. Prove Boolean NOT/NAND/NOR truth tables for all finite inputs; explain what this does not say about analog noise margins.
10. Check dynamic power αCV²f with stated activity factor and explain omission of leakage/short-circuit currents.
