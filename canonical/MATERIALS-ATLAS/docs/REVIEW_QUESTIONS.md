# Materials Atlas authored review prompts (not held-out model evaluation)

These 20 checks are visible development aids. They were not independently authored or administered to an AI model.

1. When is a measured property comparable across two lots? Specify mandatory context fields.
2. What cannot be concluded from a Materials Project 0 K energy above hull?
3. Why is the model/functional and correction scheme part of a computed energy record?
4. Demonstrate a mass-versus-mole-fraction failure in a two-phase lever rule.
5. Why does a unit-cell theoretical density differ from real bulk density?
6. What is the difference between θ and 2θ in a powder diffraction report?
7. What additional measurements can distinguish competing phases with overlapping peaks?
8. Why is a crystal unit cell not a grain?
9. Give two processing changes that can affect properties without changing bulk chemistry.
10. What must be known before calculating a yield strength from a force/extension trace?
11. Why is ultimate tensile strength not a fatigue-life guarantee?
12. Explain why a single stress–strain point does not determine modulus.
13. What assumption is made in the Voigt scalar mixture equation?
14. Why cannot mass fraction replace volume fraction in a modulus mixture?
15. When does thermal free-strain mismatch fail to determine interface stress?
16. What changes in the result if a missing competing phase is added to a computed binary hull?
17. Why may two data entries with equal units and names still be incomparable?
18. What rights and uncertainty metadata must accompany a reused repository value?
19. What should the Atlas say when a component qualification question lacks test standards?
20. Which questions should be passed to Measurement, Causal and Manufacturing rather than answered solely from Materials?

**Review intent:** Check evidence closure, assumptions, abstention and failure modes, not memorization of toy numbers.


## v0.2.0 new evidence-focused questions (authored, not held-out evaluation)

1. What evidence would establish the physical units of the NIST Hahn1 response?
2. What does agreement between certified RSS and a locally copied data table support, and not support?
3. Why is a least-squares solution initialized near the certified optimum not evidence of unique global convergence?
4. Under which physical assumptions can an α(T) curve predict an unconstrained specimen's length ratio?
5. Why can't a coefficient tabulated at 295 K justify a 600 K design assumption without more information?
6. How would you distinguish bulk diffusion from grain-boundary transport in measured concentration profiles?
7. Which uncertainties enter the conversion from force–extension data to reported yield strength?
8. Why does uniform deformation have to be established before converting engineering to true stress?
9. What measured information is required before stress intensity can be compared to validated fracture toughness?
10. Why does a Paris rate at one ΔK not establish cycles to failure?
11. What conditions would trigger refusing a materials ranking even when all candidate numbers are finite?
12. Which deployment and routing checks remain deferred until all thirty content libraries exist?


## v0.3.0 adversarial scientific reasoning checks (authored development material, not held-out)

1. Why does G''(x)>0 fail to prove homogeneous global equilibrium inside a miscibility gap?
2. How do binodal and spinodal endpoints differ physically?
3. Why does a root solver returning x=0.5 fail to find a low-temperature binodal?
4. At what point is an equilibrium lever fraction not the same as image-based phase area fraction?
5. Why is a 0 K DFT energy hull not automatically the finite-T common-tangent free energy?
6. Why must an XRD instrument's 2θ be divided by two in Bragg's relation?
7. Why is a known hkl assignment an input here, not evidence that the phase has been identified?
8. What happens to a shared wavelength uncertainty when the number of indexed peaks increases?
9. What unmodeled sources can produce a high reduced chi-square among derived lattice parameters?
10. Why can a Hahn1 temperature-neighbor residual correlation not be called measurement-time autocorrelation?
11. What does an 11-digit certified RSS agreement prove and not prove?
12. Which missing facts should block a claim that an alloy has a measured critical temperature?


## v1.0.0 method and source audit questions (not a hidden AI benchmark)
1. What phase, temperature range, heat capacity definition, and enthalpy reference state accompany the NIST copper fit?
2. Which conversion is needed between kJ and J when checking dH/dT against Cp?
3. Why does a fitted polynomial that matches two-decimal displayed NIST values not prove a calibration certificate?
4. Why is a source display coefficient set insufficient for a statistical confidence interval on heat capacity?
5. What could a local pit do to a coupon while leaving the average mass-loss rate unchanged?
6. Why does cleaning procedure and blank correction enter the uncertainty of mass-loss corrosion?
7. How is 87600 in the coupon mass-loss equation obtained from unit conversions?
8. What contact boundary assumptions are necessary before adding layer resistances in series?
9. When can a temperature-varying thermal conductivity invalidate the constant-k estimate?
10. What is the physical difference between an isothermal Avrami curve and a continuous-cooling transformation?
11. Why does a requested transformed fraction of exactly one imply no finite time in the ideal JMAK law?
12. What stress units are embedded in the Norton pre-factor A when stress is entered in MPa?
13. Why does doubling an assumed Norton creep rate not imply halved rupture life?
14. What independent evidence establishes bulk-flaw weakest-link volume scaling?
15. Why cannot an ordinary fitted Weibull strength distribution alone justify component size scaling?
16. How would a surface-flaw-controlled material differ from a bulk volume-flaw law?
17. Why are the Hahn1 copper benchmark and WebBook copper thermochemical fit not a shared response?
18. What is the appropriate answer when neither maximum pitting nor lot-specific strength is measured?
19. What local file hash proves, and what it cannot prove, in a transcribed publisher table?
20. Which part of the source register was backfilled from historical metadata rather than re-inspected?
21. What third-party content rights are preserved and what was not mirrored?
22. What outstanding experimental and integration gates remain after scoped content v1?
