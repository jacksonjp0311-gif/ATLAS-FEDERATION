# Investigation 17 — Can coupon strength be scaled to twice the volume?

A fitted Weibull curve for failure stress is not automatically a physical weakest-link fracture law. The publisher abstract of a 2020 *Ceramics International* review explicitly distinguishes the ordinary empirical distribution from Weibull fracture theory. [Abstract and DOI](https://www.sciencedirect.com/science/article/pii/S0272884220313092). No full article was mirrored or claimed inspected.

**Constructed conditional model.** Assume physically independent identical bulk flaw populations over elemental volume, uniform tension, and survival `S=exp[−(V/V0)(σ/σ0)^m]`. For σ=120 MPa, σ0=200 MPa, m=5, V=V0=1000 mm³, survival is **0.925186445**. At twice the volume with the same stated law, survival is **0.855969957**, the square of the first result. This illustrates how a physical failure mechanism could imply size dependence.

**Critical alternative.** If observed failure originates from surface machining flaws, the number and severity of critical flaws may scale with stressed surface area, not bulk volume. Residual stress, flaw orientation or spatial stress gradients also break the simplified bulk-volume form. Two samples of equal material chemistry could have different strength distributions due to finishing or geometry. The calculator therefore refuses any volume scaling until a caller explicitly asserts the bulk weakest-link hypothesis. Assertion is **not verification**.

A real component-strength prediction requires measured specimen failure statistics, failure-origin fractography, correct loading geometry, sampling uncertainty, environmental sensitivity and appropriate design standards. The Atlas does not infer characteristic strength from a tensile curve or provide a certified failure probability.

**Outcome:** computed conditional probabilities only, not reliability qualification. The default abstention prevents a misleading transfer from empirical statistics to structural reliability.
