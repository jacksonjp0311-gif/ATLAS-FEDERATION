# 60. Diode current as an ideal semiconductor-interface model

**Theme:** Electronics interface · **Chemistry Atlas scoped research v1.0.0**

**Evidence level:** project-written mathematical/reference explanation with scope-limited official sources. Every worked numeric input is hypothetical; publisher originals are not in this archive.

## Scientific foundation

A diode introduces directional current-voltage behavior through carrier transport and junction electrostatics. The Shockley ideal diode expression provides a bounded introductory description of current under prescribed temperature, saturation current and ideality factor. These quantities are not universal material constants, and a commercial diode's behavior is affected by contacts, high injection, self-heating, series resistance and reverse breakdown. A numerical model that returns an exponential curve must not be interpreted as a working chip or its electrical safety specification.

## Governing relationship and dimensional conventions

`I=I_s [exp(q V/(n k_B T))-1]. Here I_s>0 is supplied saturation current, n>0 ideality factor, T>0 kelvin.`

Dimensionless activities and properly normalized state conventions are required before taking logarithms. All heat-capacity and carrier-density inputs must carry the declared temperature, phase and units.

## Reconstruction and derivation

The exponential term reflects thermal dependence of carrier injection across an idealized junction. With V=0 the exponent is zero, so current is zero. For sufficiently negative bias, the ideal result approaches -I_s, but real reverse breakdown and leakage mechanisms are not captured. In computations, expm1(x) improves accuracy for small x and explicit input bounds prevent silent exponential overflow. This is a mathematical model, not proof that the contacts or material junction can be realized.

## Original worked investigation

Choose hypothetical Is=1e-12 A, n=1 and T=300 K. Verify I(0)=0, estimate current at ±0.1 V, and compare the results with a direct NumPy exponential calculation. Investigate why the ideal reverse-bias prediction cannot certify breakdown voltage.

**Evidence requirement:** reproduce this arithmetic by hand or with independently written code; do not assert a laboratory result from an authored fixture.

## Failure boundaries and uncertainty

No device fabrication, P-N junction profile, contact resistance, thermal management or electrical certification. Real doping, recombination and defects require independent materials data.

An incomplete dataset, untested thermodynamic fit or missing device safety requirement must remain explicitly unknown. No hazardous synthesis, energized apparatus or chemical processing steps are specified by this reference.

## Published source navigation (link only)

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/)
- [Materials Project API and computed materials data schema](https://docs.materialsproject.org/downloading-data/using-the-api)

These URLs are citations, not local authenticated copies of the publisher's full document. Check edition, license, original-byte hash and applicability before empirical use.
