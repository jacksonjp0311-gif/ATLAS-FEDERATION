# 10. Thermal transients and characteristic time scales

**Area:** Heat Transfer. **Release:** Energy Atlas 0.1.0. **Source status:** assistant-checked selected publisher scope; original publisher bytes NOT retained.

## Definitions and physical context

Many real systems do not reach steady state before a measurement or demand change. A lumped thermal model treats a body as spatially isothermal, with thermal capacitance mc and a surface heat transfer hA. Its temperature difference from ambient decays exponentially when no internal heat is generated. The characteristic time is tau=mc/(hA). This model is appropriate only when internal thermal resistance is small relative to boundary heat transfer, commonly assessed with a small Biot number. Battery packs, computing modules, furnace walls and buildings often need spatial models because internal gradients cannot be ignored.

## Fundamental relationship, symbols and SI dimensions

`m c dT/dt = −hA(T−T_env); T(t)=T_env+(T0−T_env)e^(−t/τ); τ=mc/(hA).`

The variables' units must be stated from the actual system. Positive directions, sample intervals, pressure or temperature references and operating boundaries may differ. A dimensionally correct equation is a necessary, not sufficient, condition for an accurate physical model.

## Derivation and why it holds under its assumptions

Separate variables in the linear first-order differential equation, integrate d(T−Tenv)/(T−Tenv)=−dt/τ, and apply the initial condition. The exponential solution cannot predict sensor response or material changes unless those are modeled. At one time constant the temperature difference is 1/e of its starting value; after several time constants the system approaches ambient asymptotically.

## Reconstruct the example without external AI

For 10 kg, c=500 J/(kg K), h=20 W/(m² K), area=2 m², compute tau=125 s. Compare model temperatures after 125 and 250 s. State what a Biot-number calculation would need before using this on a real motor.

The example is a stipulated model, not a measurement. Recalculate the symbolic steps and compare with the pure-Python code where a corresponding function exists. Preserve all input values, units, and source differences.

## Counterexample, limitations and what is still unknown

A negative or zero time constant is unphysical under this passive model. Uniform temperature and constant h are approximations, not universal physical truths.

A complete physical application needs independent measurement and a qualified engineer or scientist to validate calibration, safety envelopes and missing mechanisms. Never promote source summaries or synthetically passing tests to observational proof.

## Source navigation and rights

- [DOE Energy Efficiency Versus Energy Intensity](https://www.energy.gov/cmei/energy-efficiency-vs-energy-intensity) — inspected: Efficiency differs from sector intensity and structural changes
- [NIST Measurement Uncertainty Guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) — inspected: Measurement uncertainty, measurand, instrument and calibration context

The above sources are referenced and paraphrased, **not** redistributed as primary works. The precise publisher edition and permission to mirror full text have not been established.
