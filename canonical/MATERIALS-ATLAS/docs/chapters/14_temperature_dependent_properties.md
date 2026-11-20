# Chapter 14 — Thermal properties vary with state, temperature and direction

An engineering property record requires material specification, composition, processing state, orientation, temperature, testing method, and provenance before it can support a design comparison. A single tabulated coefficient at 295 K does not establish that coefficient over 20–800 K. The NIST Neutron Research reference table provides illustrative values for selected materials **at 295 K**, including aluminum and copper density, expansion and thermal conductivity; it does not document a particular specimen in the user's possession.

## Three thermal questions that must not be conflated

1. **Coefficient at one state:** instantaneous scalar coefficient `alpha(T) = d[ln L(T)] / dT`, when this definition is appropriate. Isotropy and direction have to be stated.
2. **Free dimension change along a path:** `ln(L(T1)/L(T0)) = integral_T0^T1 alpha(T) dT`, if the material follows a reversible path represented by the same function. `materials_atlas.advanced.linear_thermal_strain_path` uses trapezoidal quadrature over strictly increasing supplied temperatures. Its input MUST be in reciprocal kelvin; it will not infer units.
3. **Interfacial stress and failure:** free mismatch `Delta epsilon = (alpha_A - alpha_B) Delta T` is not stress. Constraint, spatial temperature gradients, plasticity, creep, adhesive state, transient heat transfer and geometry govern the resulting stresses. No joint safety decision follows from a scalar mismatch alone.

Temperature-dependent α curves can be affected by phase transformation, heat-treatment history, crystallographic direction and environmental factors. In crystalline anisotropic materials α is a tensor; using an average can be poor for an oriented single crystal. In polymers, glasses and composites, time and relaxation history often matter. Reversible small-strain integration also fails if heating triggers irreversible changes.

## Model demonstration, not measured property

With a synthetic coefficient grid of `[18,20,22]×10^-6 K^-1` at `[300,350,400] K`, trapezoidal integration returns log length change 0.002 and the length ratio `exp(0.002)`, approximately 1.002002. A shortcut multiplying α(300 K) by 100 K returns 0.0018, a different estimate even within the same constructed model. Neither result validates that any actual alloy has those coefficients.

**Re-use rule:** A measured curve, a handbook table and a DFT-computed property cannot be put into one comparison without declaring their different reference states and uncertainty. The optional NIST table is a contextual reference; the Hahn1 response scale remains unresolved. Related shared nodes: Measurement Atlas for uncertainty and Control Atlas (queued) for temperature-control effects.

**Source:** NIST NCNR Reference Tables, `https://www.nist.gov/ncnr/neutron-instruments/sample-environment/sample-mounting/reference-tables`.
