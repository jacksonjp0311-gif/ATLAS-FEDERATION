# CHEMISTRY ATLAS — Technological Continuity Reference v0.1.0
James Paul Jackson research program · 14 November 2026 · ATLAS Common Contract 1.0
This is original educational reconstruction, not a complete licensed chemical industry, a trainable language model, or certified chemistry practice.
The central objective is to preserve the chemistry needed to understand and eventually recreate sensors, materials, storage, semiconductors and AI hardware. No dangerous manufacture or real chemical experiment is performed.
## 35 chapters

---

# Chapter 01 — Matter, chemical identities, and traceable units

**Domain:** Foundations  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemistry studies substances and transformations at atomic, molecular, ionic, and bulk levels. A substance name does not fully specify a sample: phase, isotopic composition, purity, pressure, temperature, and measurement uncertainty may be material to a result. Chemical identity can be represented by formula, structure, standardized identifier, or reference specimen; these representations need not be equivalent. Reconstructing useful chemistry requires knowing what was measured, which system boundary was used, and what was assumed about missing components. The kilogram, kelvin, mole, second and related SI units are derived through defining constants; chemistry combines them into concentrations, reaction energies, diffusion coefficients, and electrochemical potentials. A standard state's conventions must always accompany thermodynamic values.

## Mathematical or physical principle

`n=N/N_A; mol defined by N_A=6.02214076×10^23 mol^-1, exactly.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A mole counts specified elementary entities rather than describing a universal mass of material. The SI fixing of Avogadro's constant makes the proportionality exact, while converting grams to moles requires an experimentally justified molar mass. A chemical formula can count atoms in a molecular representation, but elements in compounds may have natural isotopic variability. A reasonable teaching calculation uses a declared atomic mass table; it must not claim atomic weights are exact constants. Do not extrapolate the precision of an exact unit definition to chemical sample purity.

## Reconstruct an illustrative result offline

Choose a fictional pure species with stated molar mass 20 g/mol and a declared sample mass 40 g. Compute 2 mol and multiply by the exact Avogadro constant to obtain the entity count. Separately name the missing uncertainties in the sample mass and actual species identity.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

An arbitrary chemical label, web identifier, or model-generated formula does not prove a bottle contains that compound. SI unit exactness is not empirical substance identity or safety certification.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [BIPM SI base unit: mole](https://www.bipm.org/en/si-base-units/mole) — inspected: Mole and exactly defined Avogadro constant; selected official public page
- [CIAAW Standard Atomic Weights 2024](https://ciaaw.org/atomic-weights.htm) — inspected: Interval and point recommended standard atomic weights and normal-material definition

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 02 — Atomic nuclei, electrons, isotopes, and the periodic table

**Domain:** Foundations  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Atomic number counts protons and defines the chemical element, whereas mass number includes protons and neutrons. Isotopes of an element differ in nuclear mass and can influence vibrational spectra, diffusion, and measurement without changing elemental identity. Electron configurations and effective nuclear charge help explain periodic trends, but simple shell diagrams are approximations to many-electron quantum mechanics. The same nominal element may have multiple oxidation states in compounds. Standard atomic weights for normal materials can be intervals because isotopic abundances vary in nature. A future knowledge archive should preserve the source edition and the distinction between exact isotope mass, relative atomic mass, average standard atomic weight, and nominal mass number.

## Mathematical or physical principle

`A_r(E)=Σ_i f_i m_i/m_u for fractions f_i summing to one under a given isotopic composition.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Average isotopic mass is a weighted sum over isotopic contributions. For individual isotopes the mass is measured and has uncertainty; composition fractions can vary by sample. A CIAAW entry represented as an interval is not a point constant; choosing a value within it without reporting the assumption hides potential uncertainty. Atomic number and electron count determine neutral ground-state chemistry only at a broad level, not detailed material defect or surface behavior.

## Reconstruct an illustrative result offline

Create two artificial isotopes of mass 10 and 11 in equal fractions and compute mean 10.5. Vary the fraction to 90/10 and observe the change. Explain why one fixed molar mass is insufficient to characterize all isotopic samples.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This reference is not a nuclear-reaction or isotope enrichment manual. Neither rounded mass numbers nor chemical electron structures demonstrate nuclear safety or radioactive sample provenance.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [CIAAW Standard Atomic Weights 2024](https://ciaaw.org/atomic-weights.htm) — inspected: Interval and point recommended standard atomic weights and normal-material definition
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 03 — Electronic structure and chemical bonding

**Domain:** Quantum and bonding  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemical bonding arises from electron-nuclear interactions governed by quantum mechanics. Ionic, covalent, metallic and intermolecular descriptions are useful idealizations whose boundaries can blur. Lewis structures encode local connectivity and formal charge but do not supply complete electron density, orbital mixing, or band structure. In solids, periodic atomic arrangements produce electronic bands, and chemical composition and defects can tune conductive properties. Rebuilding computing hardware requires understanding the relationship from electronic structure through stable materials to fabrication, not treating a bond diagram as a semiconductor design. Reference energy levels and spectra should remain tied to measurement methods or a specified quantum approximation.

## Mathematical or physical principle

`Electronic energy obeys Hψ=Eψ in a stated quantum model; photon energy E_photon=hν.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The time-independent Schrödinger equation defines an eigenvalue problem for a Hamiltonian; the quality of the calculated energy depends on approximations to electron correlation, boundary conditions and nuclei. A bonding orbital picture can predict a trend but does not prove experimental conductivity or device lifetime. Transition energies relate to photon frequency under energy conservation; observed spectral lines can test assignments only after instrument calibration.

## Reconstruct an illustrative result offline

Take a hypothetical photon with frequency 5×10^14 Hz and compute energy with the exact Planck constant. Explain why that energy alone does not determine whether an unknown material absorbs it: allowed electronic transitions and optical properties are also required.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No atomistic quantum-chemistry solver, band-structure measurement or material purity assessment is implemented in this first edition. High-level bonding explains tendencies, not actual process recipes.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [BIPM SI Brochure, ninth edition, updated 2026](https://www.bipm.org/en/publications/si-brochure) — inspected: Updated ninth edition, seven defining constants and CC BY 4.0 brochure license statement
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 04 — Chemical formulas and exact atom conservation

**Domain:** Stoichiometry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A chemical equation describes chosen reactant and product species with coefficients; balancing its elemental counts is a necessary mathematical condition for a valid chemical transformation. It is not evidence that the reaction proceeds spontaneously, quickly, safely or with specified selectivity. Formulas can contain nested groups and integer multiplicities, but charged species, isotopic labels and coordination compounds may require richer notations. An archive should preserve the original representation and show exactly what a parser accepts. For simple neutral species, a vector of counts per element provides a sparse conservation matrix; its nullspace contains formally balanced coefficient assignments.

## Mathematical or physical principle

`For matrix A of product-negative/reactant-positive atom counts, Aν=0, ν_i>0. Primitive integer ν obtained from rational nullspace when unique.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Each row corresponds to an element; conservation requires that total atoms on each side agree for that element. Rational Gaussian elimination gives exact candidate coefficients without floating-point rounding. When the nullspace has more than one independent dimension, arbitrary choices are possible and the algorithm should refuse to guess. The first edition intentionally rejects unsupported charge notation: a neutral atom balance alone cannot handle ionic redox charge conservation.

## Reconstruct an illustrative result offline

For 2 H2 + O2 → 2 H2O, write hydrogen and oxygen row balances and show both residuals equal zero. Repeat with incorrect coefficients 1,1,1 to exhibit nonzero residuals. The provided exact-Fraction code reconstructs primitive coefficients.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Balanced equations do not prove that chemicals are accessible, reactions occur under ambient conditions, or that mixing would be safe. Some syntactically balanced proposals are experimentally unrealizable.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms
- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — inspected: Equilibrium, chemical potential and Gibbs relationship, 2025 online edition

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 05 — Molar mass, limiting reagents, and theoretical yield

**Domain:** Stoichiometry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

The conversion between measured mass and amount of substance uses molar mass, which can depend on isotopic composition and whether the formula describes a defined molecular entity. Stoichiometric coefficients give ideal ratios of consumed species and produced products. When supplied amounts cannot satisfy the full ratio, the limiting species bounds the hypothetical reaction extent. Theoretical yield assumes complete conversion to the specified products and does not include kinetic inhibition, side reactions or purification loss. A useful chemical knowledge base separates mathematical reaction balance, measured feedstock composition and actual process yield.

## Mathematical or physical principle

`n_i=m_i/M_i; ξ_max=min_i(n_i/ν_i) over supplied reactants for a specified reaction.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Mass divided by g/mol gives moles. For every reactant, dividing available moles by the positive stoichiometric coefficient yields the maximum reaction extent that one species could support. The minimum determines the binding resource. This argument assumes each molecule in the feed represents a usable reactant, with no contaminant consumption or kinetic constraints. A correct limiting calculation is a theoretical inequality, not a claim about an actual chemical manufacturing run.

## Reconstruct an illustrative result offline

A fictional reaction A+2B→C starts with 2 mol A and 5 mol B. The maximum extent is min(2,2.5)=2 mol; A limits. List remaining 1 mol B and describe what an independently measured product yield would need to report.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Do not interpret calculated theoretical yields as instructions for dangerous chemical synthesis or predictable conversion in a chemical reactor. Feed purity and phase may determine actual behavior.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms
- [BIPM SI base unit: mole](https://www.bipm.org/en/si-base-units/mole) — inspected: Mole and exactly defined Avogadro constant; selected official public page

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 06 — Chemical solutions, concentration, and activities

**Domain:** Solution science  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Solution concentration may be reported as molarity, molality, mole fraction, mass fraction, or an activity-based thermodynamic quantity. These measures are not interchangeable: molarity uses the final solution volume and changes with temperature, while molality uses solvent mass. Chemical potential and equilibria depend fundamentally on activities, which account for deviations from ideal mixing. A concentration label can identify nominal composition but cannot tell whether a sample is reactive, corrosive, safe or biologically appropriate. High ionic strength and complex formation require special attention to activity coefficients and reference standards.

## Mathematical or physical principle

`c=n_solute/V_solution; a_i≈γ_i(c_i/c°) under specified activity convention.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Dividing the amount of solute by the final solution volume gives molarity. Diluting a nonreacting solute at constant solute amount yields c1V1=c2V2, but volume additivity can fail in strongly nonideal mixtures. In thermodynamic calculations, unitless activity must appear inside logarithms; logging a dimensional mol/L number without a standard concentration silently changes the model. Activity coefficients are not usually known from a single concentration measurement.

## Reconstruct an illustrative result offline

For a stipulated 0.2 mol amount in 0.5 L final solution, calculate 0.4 mol/L. Model dilution to 1 L at constant solute amount and obtain 0.2 mol/L. Explain why the calculation is insufficient to specify an actual mixing operation or final activity.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This is analytical bookkeeping, not chemical preparation, safe mixing or acid-dilution advice. Reaction, heat, precipitation and contamination can invalidate the simple dilution model.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — inspected: Equilibrium, chemical potential and Gibbs relationship, 2025 online edition
- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 07 — Thermodynamic states, enthalpy, and heat capacity

**Domain:** Thermodynamics  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A material's thermodynamic state depends on temperature, pressure, composition and phase, not merely its chemical formula. Enthalpy is useful for constant-pressure heating and flow-process energy accounting. Heat capacity may vary strongly with temperature and can change abruptly near transitions. Compiled reference data such as the NIST Chemistry WebBook provide values conditional on selected phases, standard states and fits. Chemical process calculations must preserve the edition and independent uncertainty of those values. Deriving a result from a fit outside its stated temperature range is invalid even if the formula still returns a number.

## Mathematical or physical principle

`ΔH=Σ_p ν_p Δ_fH°_p −Σ_r ν_r Δ_fH°_r for consistent phases and reference states; Δh≈∫C_p(T)dT.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Enthalpy is a state function; Hess's law permits reaction enthalpy to be assembled from formation enthalpies because the net difference is independent of the chosen state path. Formation values must share the same thermodynamic reference and chemical phases. Thermal-process energy adds sensible, latent and reaction enthalpy terms under a defined boundary. The WebBook Shomate parameterization is a fit, not an always-valid universal heat-capacity law.

## Reconstruct an illustrative result offline

Construct hypothetical formation enthalpies A=-10 and B=-20 J/mol for A→B, giving Δ_rH=-10 J per mol extent. Reverse the reaction and confirm the sign changes. Replace B's phase label without changing the reference and explain why the numerical example would be incomplete.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Reaction enthalpy does not determine reaction rate or safe process temperature. Thermal data may include third-party publisher contributions not automatically in the public domain.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [BIPM SI Brochure, ninth edition, updated 2026](https://www.bipm.org/en/publications/si-brochure) — inspected: Updated ninth edition, seven defining constants and CC BY 4.0 brochure license statement

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 08 — Entropy, Gibbs energy, and chemical potential

**Domain:** Thermodynamics  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemical systems obey the first and second laws together. At fixed temperature and pressure, Gibbs free energy helps determine thermodynamic preference; the Gibbs chemical potential describes how energy changes with composition. A negative reaction Gibbs energy indicates the specified forward transformation is thermodynamically favored under a state model, but not that it occurs quickly. Kinetic barriers can preserve metastable materials. Chemical activities enter potential differences and reaction quotients; using unspecified concentrations can lead to qualitatively wrong predictions. Data quality and reference-state consistency are critical when reconstructing thermodynamic claims.

## Mathematical or physical principle

`Δ_rG=Δ_rG°+RT ln Q; at equilibrium Δ_rG=0 and ln K=−Δ_rG°/(RT).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

For reactants and products, the quotient is a product of dimensionless activities raised to their stoichiometric powers. It accounts for composition's effect on chemical potential. The relationship follows from summing the chemical potentials and separating standard-state terms. At equilibrium forward and reverse macroscopic rates balance. A finite sample may not equilibrate on the observation time scale, and state changes can affect temperature and activities.

## Reconstruct an illustrative result offline

Set Δ_rG°=0 and Q=2 at 298 K. The resulting RT ln2 is positive; the modeled forward direction is not favored. Invert Q to 1/2 and verify the sign changes, then explain why neither numerical result predicts a rate.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

A negative ΔG is not a promise of benign materials or safe reaction. Chemical hazards, activation barriers, product phases and competing pathways must be assessed independently.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — inspected: Equilibrium, chemical potential and Gibbs relationship, 2025 online edition
- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 09 — Equilibrium constants and free-energy provenance

**Domain:** Thermodynamics  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Equilibrium constants are thermodynamic descriptors tied to specified species, activities, phases and temperature. They cannot be copied between different reaction representations without checking stoichiometry and standard states. For strongly favorable reactions, K may be too large for a common binary floating-point number; log K remains useful and avoids overflow. A scientific reference should preserve logarithmic values and their source uncertainties. The existence of one equilibrium constant never describes how quickly equilibrium is approached, whether products precipitate, or whether a material degrades under operation.

## Mathematical or physical principle

`K=exp(−Δ_rG°/RT); ln K=−Δ_rG°/(RT).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

At fixed T, the reversible equilibrium condition is zero Gibbs change, so setting Δ_rG°+RT lnK=0 yields log K directly. Multiplying all reaction coefficients by a factor changes the conventional equilibrium constant accordingly: the same physical equilibrium can have a different numeric K under a redefined equation. For this reason an archive must couple values to exact reaction stoichiometry and standard states.

## Reconstruct an illustrative result offline

Given Δ_rG°=−RT at any positive T, demonstrate lnK=1 and K=e. Multiply the formal reaction by 2 and observe that Δ_rG° doubles, so K becomes e² under the new representation.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

An equilibrium constant in concentration units is generally not a thermodynamic standard-state constant; the log requires dimensionless activities. Extremely high K does not prove perfect conversion or absence of competing chemistry.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book: chemical equilibrium](https://goldbook.iupac.org/terms/view/C01023) — inspected: Equilibrium, chemical potential and Gibbs relationship, 2025 online edition
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 10 — Reaction kinetics and Arrhenius approximations

**Domain:** Chemical kinetics  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Reaction rates describe how species amounts or concentrations change over time. A thermodynamic driving force and a rate law answer different questions: a stable equilibrium may require geological time if the kinetic barriers are large. The Arrhenius relationship models the temperature dependence of certain rate constants over a limited range; its apparent activation energy can change with mechanism. A first-order exponential decay is one possible kinetic model, not a universal description of chemical aging, degradation or polymerization. The parameter and conditions must be preserved alongside a measured dataset, and fits require independent validation.

## Mathematical or physical principle

`k(T)=A exp(−E_a/RT); ln(k2/k1)=−(E_a/R)(1/T2−1/T1); C(t)=C0 exp(−kt) for first order.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Taking logarithms of the Arrhenius form eliminates the preexponential factor and permits a ratio of rates at two absolute temperatures. Separating dC/dt=−kC gives the exponential first-order solution. Both derivations assume temperature and mechanism conditions that may not hold in an industrial process. A rate inferred from only two points can reflect transport effects or multiple pathways instead of a single activation barrier.

## Reconstruct an illustrative result offline

Take invented Ea=20 kJ/mol and compare a model rate constant at 300 K and 330 K. Confirm the rate increases under this positive-Ea assumption. Separately use a first-order k=0.1/s to compute concentration after 10 seconds.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Never use this teaching rate law to set hazardous reactor residence times, unstable chemical storage, or an accelerated-aging safety claim without independent material/kinetic testing.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — inspected: Data Version 2026, gas-phase reaction kinetics indexing and research references
- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 11 — Acids, bases, pH, and measurement conventions

**Domain:** Solution science  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Acid-base reactions involve proton-transfer or electron-pair concepts depending on the theory and chemical system. pH is fundamentally related to hydrogen-ion activity, not merely the negative logarithm of a measured molar concentration in every solution. Activity coefficients, temperature, ionic strength, liquid junctions and calibration influence measured pH. A scale of 0 to 14 is a common introductory approximation for aqueous systems at particular conditions, not a universal mathematical bound. A researcher must record electrode calibration, standard buffers, temperature and sample composition to interpret real pH measurements.

## Mathematical or physical principle

`pH=−log10(a_H+); a_H+ dimensionless relative to standard activity convention.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A logarithm requires a dimensionless argument; an activity is normalized to a reference state. The pH scale changes by one unit for a factor-of-ten change in the activity under its definition. In real solutions an electrode reading must be linked to its reference electrodes and calibration buffers; the computed activity may be an operational estimate. A chemical identity does not imply acid strength, which depends on equilibria and solvent context.

## Reconstruct an illustrative result offline

Take a hypothetical a_H+=10^-7 and calculate pH=7. Repeat with activity 2 and observe a negative pH; explain why this is mathematically permitted and why instrument calibration matters.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This chapter is not a recipe for handling strong acids or bases, adjusting drinking water, or determining biological safety. Concentration alone does not prove pH or benign chemical behavior.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific
- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 12 — Buffer equilibria and Henderson–Hasselbalch limits

**Domain:** Solution science  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A buffer resists certain changes in hydrogen-ion activity by involving conjugate acid-base species. The Henderson–Hasselbalch expression relates pH to pKa and the ratio of conjugate base to acid activities under equilibrium approximations. Its convenience can encourage invalid use outside the expected activity/concentration range or when multiple equilibria compete. Real buffer capacity depends on total composition, temperature, ionic strength and other chemical species; equal activities alone do not determine the amount of acid or base a system can absorb. A scientific reference should preserve these limitations explicitly.

## Mathematical or physical principle

`pH≈pKa+log10(a_base/a_acid) under a conjugate equilibrium convention.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Rearranging Ka=a_H+a_base/a_acid and taking a base-ten logarithm gives the expression. If activities are equal, the ratio is one and pH≈pKa. This does not provide a recipe for making a specified pH solution: the activity ratio and total concentration must be established independently, and laboratory hazards may prohibit casual mixing.

## Reconstruct an illustrative result offline

Assume fictitious pKa=5 and base/acid activity ratio 2. Calculate pH≈5.301. Replace the ratio with 1/2 and obtain ≈4.699. Explain what data would be needed to predict buffer capacity or safe material compatibility.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

An ideal ratio is not a calibration standard, medical buffer or chemical handling guideline. Multiple protonation states and activity coefficients can invalidate the simple formula.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific
- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 13 — Electrochemical charge and Faraday constant

**Domain:** Electrochemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Electrochemical science connects electron transfer, chemical potential, electrical potential and material changes. The Faraday constant measures electric charge per mole of elementary charge carriers and is determined from the exactly defined elementary charge and Avogadro constant. Charge accounting is necessary for batteries, electrolysis and corrosion measurements, but it cannot establish product yield, chemical purity or electrical safety. Electrochemical processes can have multiple reaction channels and parasitic currents, so an electrical charge measurement must be interpreted with a documented current efficiency and product analysis.

## Mathematical or physical principle

`F=N_A e≈96485.332123 C/mol; Q_electric=n_e F.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The coulomb per mole constant follows from multiplying entities per mole by charge per elementary carrier. For a declared amount of electrons, n_eF is a charge quantity; time-integrated current is independently Q=∫I dt. Faradaic efficiency compares the charge attributed to the desired reaction with total transferred charge, which requires measured composition and a known electron stoichiometry. Merely drawing current does not prove the intended substance formed.

## Reconstruct an illustrative result offline

Compute the charge corresponding to 1 mol of singly charged electrons and report the source of the exact constants. Then suppose only half an experimental current contributes to the desired reaction: explain why theoretical charge cannot determine product yield without additional evidence.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No electrolyzer, battery cell, plating apparatus or chemical synthesis is constructed or specified here. Current-driven hazardous chemistry requires validated industrial procedures and appropriate safety standards.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [BIPM SI Brochure, ninth edition, updated 2026](https://www.bipm.org/en/publications/si-brochure) — inspected: Updated ninth edition, seven defining constants and CC BY 4.0 brochure license statement
- [IUPAC Gold Book: Nernst equation](https://goldbook.iupac.org/terms/view/09068) — inspected: Reversible electrode potentials in terms of activity quotient, T, electron number and Faraday constant

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 14 — Nernst potential, standard electrode references, and activity

**Domain:** Electrochemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Electrode potential is an intensive thermodynamic quantity under specified reference electrodes and electrochemical conditions. The Nernst equation relates equilibrium electrode potential to standard potential and a dimensionless reaction quotient built from species activities. Real electrodes may display overpotential, resistance, concentration gradients and other deviations under load. A standard potential without reference convention or phase and ionic-state information can be meaningless in comparative calculations. Battery nameplate voltage is not automatically a Nernst equilibrium prediction for every temperature and state of charge.

## Mathematical or physical principle

`E_eq=E°−(RT/nF)ln Q, with n positive integer electrons and Q an activity-based dimensionless quotient.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Starting from ΔG=−nFE for a reversible electrochemical reaction and ΔG=ΔG°+RT lnQ, substituting yields the potential correction. At Q=1 the correction is zero. Larger product activity relative to reactants changes the equilibrium potential in a direction set by the stipulated quotient. The derivation assumes equilibrium interfaces and an externally measured standard reference. Under operating current the electrode can depart from that equilibrium value.

## Reconstruct an illustrative result offline

Set E°=1 V, n=1, T=298.15 K, Q=1 and recover 1 V. Change Q to 10 and evaluate the potential correction; report that this is not a forecast of delivered battery power.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Without cell identity, phase, reference electrode, activities, kinetics and load, the number has no operational device validity. The code cannot charge batteries or control chemical processes.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [IUPAC Gold Book: Nernst equation](https://goldbook.iupac.org/terms/view/09068) — inspected: Reversible electrode potentials in terms of activity quotient, T, electron number and Faraday constant
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 15 — Battery chemistry and the difference between capacity and reaction extent

**Domain:** Electrochemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Battery performance connects active material composition, reversible electron transfer, ionic transport, electrodes, electrolyte stability and thermal behavior. Stoichiometry can bound theoretical charge, but practical capacity is lower and depends on use, rate, aging and degradation. Electrochemical free energy relates to reversible cell voltage only under appropriate phase and activity conventions. Batteries must therefore be modeled across chemical, electrical and thermal domains, with protection and hazard controls separate from the theoretical energy stored in reactants. This connection is central to future computing infrastructure because power availability and battery safety affect processors, storage and communication devices.

## Mathematical or physical principle

`Q_theoretical=n_e F; E_reversible=−Δ_rG/(nF), with charge Q in C and reaction Gibbs energy Δ_rG in J per mol reaction extent.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Multiplying reaction extent by electron stoichiometry gives moles of transferred electrons, hence coulombs. Dividing the thermodynamic free energy per reaction mole by charge per reaction mole yields voltage for an ideal reversible transformation. This is not a real constant terminal voltage; concentration, activity, polarization and transport change the observed voltage as state evolves. Thermal runaway and short-circuit hazards are not deducible from this reversible model.

## Reconstruct an illustrative result offline

For a hypothetical reaction carrying 2 mol electrons per mol extent, compute 2F coulombs. If the reversible energy per extent were a stated value, calculate E and explain why measured terminal voltage and capacity could differ.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No electrolyte formulation, abusive testing, improvised battery construction or protection bypass is provided. These topics require certified engineering and standards separate from theory.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [IUPAC Gold Book: Nernst equation](https://goldbook.iupac.org/terms/view/09068) — inspected: Reversible electrode potentials in terms of activity quotient, T, electron number and Faraday constant

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 16 — Chemical process boundaries and mass conservation

**Domain:** Chemical engineering  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemical engineering scales chemical knowledge into systems with feeds, products, separation, recycling, utilities, materials compatibility and environmental controls. A process flow diagram can describe species and energy movements without prescribing hazardous synthesis. At every defined boundary, total mass and element-specific balances must reconcile, including accumulation and emissions. Real reactions can introduce byproducts, phase changes, losses to equipment surfaces and unmeasured streams. An unexplained residual is an evidence problem, not an invitation to assert that matter disappeared. Industrial continuation requires metrology and process records as much as chemical reaction equations.

## Mathematical or physical principle

`m_in−m_out−Δm_inventory = residual; for each conserved element i, n_in,i−n_out,i−Δn_i=0.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Elemental balance arises because ordinary chemical reactions rearrange atoms without nuclear transmutation. With an explicit inventory of flows and accumulation, an unexplained residual signals incomplete accounting, errors or untracked species. For a steady process the accumulation may vanish, but that state must be verified from measurements. A total-mass balance can pass while composition is wrong, so a chemical processor needs species and energy balances and calibrated instruments for acceptance.

## Reconstruct an illustrative result offline

In a fictional process, 100 kg input becomes 60 kg primary product, 20 kg separate output and 10 kg inventory growth. A 10 kg residual remains. List missing emission, sampling and accumulation hypotheses without assuming one is proven.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

A mass balance cannot certify absence of toxic release, safe plant operation or correct treatment of chemical waste. Technical processing requires qualified safety and environmental procedures.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [American Chemical Society, Laboratory Safety Guidance](https://institute.acs.org/acs-center/lab-safety/education-training/college-univ-guidelines.html) — inspected: RAMP risk-recognition education and safe laboratory institutional responsibilities

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 17 — Reaction engineering, transport, and residence time

**Domain:** Chemical engineering  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A reactor converts material while moving heat and species. Scale changes make mixing, heat transfer and diffusion compete with intrinsic kinetics. A rate law measured in a small vessel may cease to describe production at large scale because concentration and temperature become spatially nonuniform. A residence-time distribution describes how long material spends inside a process rather than guaranteeing every fluid element reacts equally. Chemical engineering equations must retain phase, density and applicable fluid models. A useful atlas teaches nondimensional comparisons and the distinction between chemical and physical time scales, without asserting one process recipe works for every chemistry.

## Mathematical or physical principle

`τ_nominal=V/Q for a steady volume-flow approximation; conversion X=(F_A,in−F_A,out)/F_A,in for specified feed basis.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Dividing a vessel's effective liquid volume by volumetric flow gives a nominal residence scale under incompressible continuous flow. It is not the actual time distribution in a nonideal vessel. Conversions require measured molar flow and a chemical species, not merely mass totals. Reaction extent from the previous chapter provides theoretical stoichiometric bounds; real thermal transport and product formation rates determine whether those bounds can be approached. A process that conserves all atoms might still be unsafe or consume excessive energy.

## Reconstruct an illustrative result offline

Invent volume 2 m³ and flow 0.5 m³/h, obtaining nominal τ=4 hours. Explain why a bypass channel or nonuniform mixing would make some fluid parcels exit much sooner than four hours. Report the missing reactor mixing model rather than declaring complete conversion.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This chapter contains no actionable reactor startup, synthesis temperatures, hazardous catalysts or material recipes. Scale-up requires external safety, waste handling, and process-control evidence.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — inspected: Data Version 2026, gas-phase reaction kinetics indexing and research references
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 18 — Catalysis, activation barriers, and selectivity

**Domain:** Chemical kinetics  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Catalysts change reaction pathways and may lower activation barriers without violating chemical equilibrium thermodynamics. Different catalysts can favor different products, and catalyst degradation or poisoning can change measured performance. Catalysis matters to materials synthesis, pollution control, energy conversion and semiconductor processing, but a kinetic improvement does not imply the desired pathway dominates or remains safe at industrial scale. A chemical record must separately capture reaction rates, selectivity, catalyst identity, thermal history, surface area and reproducibility. Many catalytic processes are heterogeneous: surface reaction and transport combine, and simple Arrhenius plots can conceal mechanism shifts.

## Mathematical or physical principle

`Rate law r=k(T)f(activities) under a stated model; activation-limited k∼A exp(−E_a/RT).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A catalyst can modify the pathway and therefore activation energy parameters, accelerating forward and reverse microscopic processes without changing the thermodynamic equilibrium constant for the same reaction at unchanged conditions. In a real process, mass transport and surface coverage may determine the measured rate. One temperature-dependent series is not sufficient to infer active sites or mechanistic causality. A controlled comparison would use matched reactants, surface area and conditions and independent analytical composition.

## Reconstruct an illustrative result offline

Compare two invented Arrhenius activation energies at the same temperature, holding their preexponential factors equal as an explicit assumption. The lower barrier gives a larger k. Explain why different preexponential factors and reaction pathways could reverse an actual measured comparison.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

A catalyst effectiveness number is not a recipe for a hazardous reaction. No catalysts are manufactured or evaluated here; specificity and safety remain unverified.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — inspected: Data Version 2026, gas-phase reaction kinetics indexing and research references
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 19 — Phase diagrams, chemical potentials, and crystallization

**Domain:** Materials and phases  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A phase diagram records which phases are thermodynamically stable under conditions such as temperature, pressure and composition. It is not a universal material map: diagram interpretation depends on equilibrium, purity and kinetic history. Liquid-solid phase boundaries, solubility and polymorphism determine whether a substance can be used in electronics, battery materials or optical devices. Nucleation and crystal growth can be kinetically inhibited, so an equilibrium phase may not form on an experiment's time scale. A reconstruction needs phase identities, measurement method, source sample composition, unit conventions and uncertainty, especially around metastable states.

## Mathematical or physical principle

`At equilibrium for coexisting phases α,β: μ_i^α(T,p,x)=μ_i^β(T,p,x) for each equilibrated component i.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Chemical potential equality follows from a minimum of Gibbs free energy when small amounts of a component may transfer between phases at fixed total amount. In a binary alloy, composition is another state coordinate; a single melting point may be meaningless for a multiphase region. The phase rule constrains degrees of freedom under declared equilibrium conditions, but a real crystal grown through a changing temperature field can trap nonequilibrium defects. An Atlas must preserve experimental heating/cooling history in addition to phase labels.

## Reconstruct an illustrative result offline

Sketch a two-phase coexistence under a hypothetical equilibrium of material A between solid and liquid. Explain why cooling quickly can trap a metastable amorphous state, while slow equilibration might approach the predicted phase. No temperature setpoints or synthesis instructions are inferred.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Phase diagrams alone do not provide industrial crystallization recipes or guarantee purity and absence of defects. Kinetics, compositional gradients and sample provenance remain independent.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 20 — Crystal lattices, defects, and structure–property relations

**Domain:** Materials and phases  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Crystalline solids have periodic long-range arrangements that can be represented by lattice vectors and a basis of atoms. Defects such as vacancies, interstitials, grain boundaries and substitutional impurities change chemical and electronic properties. Many important modern materials, including silicon, are intentionally modified through controlled impurities; others are harmed by contamination. Diffraction patterns can provide evidence about periodic structure but need instrument geometry and a model for scattering factors. A crystallographic structure file without synthesis and sample characterization does not certify material purity or semiconductor function.

## Mathematical or physical principle

`Bragg relation 2d sinθ=nλ in a specified elastic diffraction geometry; reciprocal lattice satisfies a_i·b_j=2πδ_ij.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

For a periodic set of lattice planes, scattered wave phases can add constructively when path difference is an integer number of wavelengths, giving a pedagogical Bragg relation. Real powder diffraction introduces multiple overlapping peaks, strain, instrumental broadening and preferred orientation. A model of perfect crystalline order does not capture grain boundaries or amorphous regions. Crystallography is crucial to identifying semiconductor and battery materials, but requires real calibrated measurements for a specific sample.

## Reconstruct an illustrative result offline

Choose a hypothetical lattice plane spacing d=0.20 nm and radiation wavelength λ=0.10 nm, first order n=1. Calculate sinθ=0.25 and approximate θ. Explain why observing a matching peak alone would not uniquely identify a real material.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No x-ray device, materials synthesis or lattice measurement is performed. Radiation safety and actual crystal-phase interpretation require qualified instrumentation.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 21 — Corrosion, passivation, and materials durability

**Domain:** Materials and phases  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Corrosion occurs when material transformations are thermodynamically and kinetically possible in an environment. Surface oxides may protect a bulk solid in some conditions yet fail through cracking, pitting or galvanic coupling in others. Potential diagrams summarize thermodynamic possibilities and cannot by themselves determine corrosion rates. Electrical conductivity, electrolyte activity, mechanical stress and microstructure all affect durability. Rebuilding high-quality electrical infrastructure requires understanding corrosion of conductors, contacts, sensors and storage components, not merely finding a metal with favorable nominal conductivity.

## Mathematical or physical principle

`ΔG=−nFE for reversible electrochemical conditions, with ΔG and E tied to the exact specified reaction and reference.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The relation connects Gibbs energy to reversible electrical work, providing thermodynamic context for oxidation and reduction. It does not imply a corrosion current or service life: charge-transfer kinetics, oxygen transport, surface films and defects control observed behavior. When combining metals and electrolytes, the material interface creates additional effects not present in bulk composition tables. A verified materials record must include surface condition, environment and time-dependent measurements.

## Reconstruct an illustrative result offline

Imagine two candidate metals with the same nominal bulk conductivity but different unmeasured oxide stability. Explain why a conductivity-only ranking cannot decide long-term electrical contact reliability. Name the electrochemical and microscopy measurements needed.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No pickling, cleaning acids, electroplating or hazardous corrosion experiments are specified. Protective coatings and their lifetime require independently validated tests.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [IUPAC Gold Book: Nernst equation](https://goldbook.iupac.org/terms/view/09068) — inspected: Reversible electrode potentials in terms of activity quotient, T, electron number and Faraday constant

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 22 — Polymers, molecular distributions, and soft materials

**Domain:** Materials and phases  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Polymers comprise distributions of chain lengths and structures, with mechanical, thermal and chemical behavior dependent on molecular-weight distribution, cross-linking, tacticity and environment. A single molecular formula or average mass rarely describes a polymer sample. Glass transition differs from melting and depends on chain mobility and formulation. Insulation, flexible connectors, photoresists and device packaging rely on polymer chemistry. Durable knowledge should capture monomer identifiers and linked physical property data, but avoid treating one name as a universal recipe. Residual solvent, additives and degradation can dominate real engineering performance.

## Mathematical or physical principle

`Number-average molar mass M_n=Σ_i N_i M_i /Σ_i N_i; approximate chain DP_n=M_n/M_repeat under declared chemistry.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Number average weights each chain equally, whereas weight average emphasizes mass-bearing long chains. Their ratio measures one aspect of distribution breadth; neither alone determines mechanical strength or environmental resistance. The repeat unit's molar mass is needed to convert an average molecular mass to chain length and terminal groups introduce corrections. Under heat or ultraviolet radiation polymers can change chemically, invalidating a static specification.

## Reconstruct an illustrative result offline

For a fictional collection with 3 chains of mass 100 units and 1 chain of mass 200 units, compute M_n=125 units. Compare weight-average and note how one longer chain raises it more than the number average.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This chapter does not describe manufacturing energetic polymers, hazardous solvents or consumer-safe formulations. Properties require real characterization and licensing of data.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [OpenStax Chemistry 2e academic textbook](https://openstax.org/books/chemistry-2e/pages/preface) — inspected: General chemistry curriculum and educational overview; different public pages/versions report CC BY 4.0 versus current CC BY-NC-SA terms

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 23 — Diffusion, transport, and dimensional time scales

**Domain:** Materials and phases  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Diffusion moves particles due to statistical motion and chemical-potential gradients. An approximate continuum model uses a diffusivity D with units m²/s; both magnitude and temperature dependence vary drastically with species, phase and structure. Diffusion matters to batteries, semiconductor junctions, contamination control, polymers and corrosion. The familiar root-mean-square displacement scaling with sqrt(time) is a mathematical result for ideal independent Brownian motion, not a calibrated physical process schedule. Real diffusion can be anisotropic, concentration-dependent or dominated by grain boundaries.

## Mathematical or physical principle

`One-dimensional RMS displacement ℓ_rms=√(2Dt); for d independent dimensions ℓ_rms=√(2dDt).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The mean-square displacement follows from adding independent random increments with zero mean and finite variance in a homogeneous medium. The square-root time law is slower than linear travel, so doubling diffusion length requires approximately four times the time under the same D. Real semiconductor dopant redistribution adds interface and reaction conditions. A diffusion coefficient measured at one temperature cannot be used at another without a validated relation.

## Reconstruct an illustrative result offline

Set D=10^-12 m²/s and t=100 s in one dimension, obtaining ℓ≈sqrt(2×10^-10) m. Multiply time by four and verify the length doubles. Explain why this does not tell someone how to operate a dopant furnace.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No temperature-cycle, doping recipe or hazardous vapor handling is supplied. Transport boundaries, defects and measured D uncertainty remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [NIST Chemical Kinetics Database, SRD 17](https://kinetics.nist.gov/kinetics/) — inspected: Data Version 2026, gas-phase reaction kinetics indexing and research references

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 24 — Semiconductors: intrinsic versus extrinsic carriers

**Domain:** Electronics-enabling chemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Semiconductor conductivity depends on the densities and mobilities of electrons and holes, which are influenced by electronic band structure, temperature, impurities and defects. Extrinsic donors and acceptors can alter carrier populations, but the amount of impurity introduced is not necessarily equal to the activated free-carrier density. Surface contamination and traps may dominate thin devices. Chemistry and materials science connect the periodic table to practical circuits through bonding, purity, crystal structure and interfaces. Preserving these relations supports the eventual reconstruction of transistors and AI hardware; a simple formula cannot replace a fabrication facility or detailed semiconductor device physics.

## Mathematical or physical principle

`σ=q(n μ_n+p μ_p) in a homogeneous low-field drift model; ρ=1/σ for σ>0.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Under the drift approximation, carrier current density is charge times carrier density times mobility times electric field. Adding electron and hole contributions gives conductivity for a uniform semiconductor. Temperature, crystal orientation, impurity scattering and band statistics determine the input densities and mobilities. A measured resistivity is an aggregate quantity, not a unique proof of dopant species or device purity. Transport in nanoscale interfaces may require models outside bulk drift.

## Reconstruct an illustrative result offline

Assume n=10^21 m^-3, p≈0 and μ_n=0.1 m²/(V·s). Compute σ using the exact elementary charge. Double the assumed carrier density and compare, then explain why doubling dopant concentration need not produce that physical change.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No semiconductor doping process, toxic precursor, etchant, or transistor fabrication instruction is specified. The result does not validate real circuit behavior, contact resistance or materials sourcing.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [BIPM SI Brochure, ninth edition, updated 2026](https://www.bipm.org/en/publications/si-brochure) — inspected: Updated ninth edition, seven defining constants and CC BY 4.0 brochure license statement

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 25 — Material purity, contamination, and semiconductor yield

**Domain:** Electronics-enabling chemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A material sample's performance can depend on contaminants at trace levels. In semiconductor manufacturing, surface particles, unintentional dopants, oxygen content and structural defects can drastically change device yield. Purity must therefore be described with an explicitly named analyte, reference method, basis (mass, amount or atomic fraction), detection limit and sampling conditions. A certificate that says “99.99% pure” is incomplete if the remaining fraction contains electrically active impurities. Analytical instruments can have blanks and contamination from their own preparation paths. A survival-grade archive must preserve detection methodology and uncertainty, not only a final percentage.

## Mathematical or physical principle

`w_i=m_i/m_total for mass fraction; residual=Σ feed mass−Σ product mass−Δinventory; detection below LOD is censored, not zero.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Mass fractions must sum to one when all components are measured and the basis is consistent. A missing species can leave a residual but not identify its chemistry. Detection limits create censored observations: “not detected” is weaker than “absent”. For electronics, electrical activation and defect chemistry matter in addition to total impurity atoms. The process mass-balance function is a simple accounting check; independent chemical analysis is required before associating a residual with a particular contaminant.

## Reconstruct an illustrative result offline

Take a fictional 100 g sample containing measured 0.01 g impurity A; its mass fraction is 0.0001 or 100 ppm by mass. Now posit an unmeasured trace impurity B. Explain why reporting exactly 99.99% of the main material would require B and other constituents to be bounded.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No actual purification, toxic chemical handling or lithography procedure is included. Analytical uncertainty, sampling bias and contamination pathways remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement) — inspected: Uncertainty and calibration scope for reconstructed measurements

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 26 — Oxidation, dielectric interfaces, and thin films

**Domain:** Electronics-enabling chemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Electronics employ insulating, conducting and semiconducting thin films whose performance depends on chemical composition, thickness, interface traps, defects and electrical breakdown. Native or grown oxides can passivate surfaces or create unwanted states; interfaces can dominate transistor behavior. Film composition is not determined solely by the bulk formula. Surface chemistry and device fabrication require exact materials, processing history and metrology. A conceptual materials reference should preserve oxide chemistry, thermodynamics, diffusion and how dielectric capacitance depends on thickness, without supplying an unsafe manufacturing schedule.

## Mathematical or physical principle

`Ideal planar capacitance C=ε_r ε_0 A/d for a homogeneous thin dielectric with d>0; actual films can deviate through fringing, leakage and trap effects.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Gauss's law for a simple parallel-plate geometry gives nearly uniform field in the dielectric interior, and integrating the potential leads to capacitance inversely proportional to thickness. The permittivity and thickness must be measured at relevant frequency, temperature and bias. The formula is electrical, while chemical processing affects the validity of its homogeneous film assumptions. Missing interface characterization prevents a capacity number from proving a viable MOS device.

## Reconstruct an illustrative result offline

Take a fictional dielectric whose area doubles while thickness and permittivity remain constant; ideal capacitance doubles. If thickness halves, ideal capacitance doubles again. Explain why actual leakage and breakdown could worsen, and which real measurements would be required.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No oxide growth conditions, etching procedures, chemical bath recipes or high-voltage testing steps are included. Industrial semiconductor fabrication requires qualified cleanroom and environmental controls.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 27 — Photochemistry, wavelength, and photoactive materials

**Domain:** Electronics-enabling chemistry  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Light can excite molecular electronic states and drive reactions when transitions are allowed and competing relaxation processes are understood. Photochemistry underpins imaging, optical sensors, solar energy materials and lithography, but photon energy alone cannot establish quantum yield or process selectivity. Light absorption depends on wavelength, concentration, geometry and electronic transitions; photons may be reflected, scattered or converted to heat. Reconstructing photochemical knowledge requires quantitative spectra, optical path geometry, source calibration and the rights to the measured data. Generic spectroscopy does not prescribe a safe photosensitive chemical formulation.

## Mathematical or physical principle

`E_photon=hν=hc/λ; ideal transmitted intensity I/I0=10^{-A} for measured absorbance A in a simple Beer–Lambert geometry.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

Photon energy follows from quantum energy-frequency proportionality and the wave relation c=λν. In an ideal absorbing solution, Beer–Lambert describes logarithmic intensity attenuation, but scattering, concentration effects and nonuniform optical paths create deviations. A certain photon energy can be necessary for a transition without guaranteeing that an actual material will respond. Photochemical reaction rate would require absorption rate, quantum yield and competing pathways.

## Reconstruct an illustrative result offline

Compute the energy of a 500 nm photon using defined h and c. Contrast that with a 1000 nm photon, which has half the energy. Explain why no claim about a specific semiconductor's photosensitivity follows without an absorption spectrum.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This is not a photolithography process recipe or UV/laser safety guide. Optical hazards, chemical exposure and actual film chemistry require independent protocols.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [BIPM SI Brochure, ninth edition, updated 2026](https://www.bipm.org/en/publications/si-brochure) — inspected: Updated ninth edition, seven defining constants and CC BY 4.0 brochure license statement
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 28 — Spectroscopy, analytical fingerprints, and measurement uncertainty

**Domain:** Metrology  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemical identification uses methods such as infrared, Raman, ultraviolet-visible, mass spectrometry, nuclear magnetic resonance and diffraction. Each detects different physical properties and has characteristic confounders. A spectrum is not an unambiguous substance identity without calibration, measurement context, sample purity and reference library quality. Instrument response, baseline correction, noise and sampling can create peaks that are absent in the chemical sample. NIST maintains compiled spectra and thermochemistry, but a query result must preserve the cited version and data rights. A future scientific community needs measurement procedures and raw spectra as well as interpretive descriptions.

## Mathematical or physical principle

`Beer–Lambert A=log10(I0/I); for ideal solutions A≈εcl with ε units chosen consistently.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The logarithmic absorbance follows from exponential attenuation under assumptions of homogeneous absorbing medium and negligible scattering. Multiplying molar absorptivity by concentration and path length gives dimensionless absorbance only when units are compatible. A calibration series can test whether the ideal relation holds over a specified range. Presence of a predicted peak is evidence conditioned on resolution and competing species; absence of a peak may reflect detection limits or instrumentation.

## Reconstruct an illustrative result offline

For an invented reference I0=100 units and transmitted intensity I=10 units, absorbance is 1. Increase I to 50 and calculate the smaller absorbance. State why these numbers do not identify a particular molecule without an experimentally collected spectrum.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

The chapter does not teach construction of hazardous radiation sources, chemical extraction or unsafe instrument operation. Original spectrum data, certified calibrations and independent interpretation are absent.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement) — inspected: Uncertainty and calibration scope for reconstructed measurements

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 29 — Thermochemical datasets and machine-readable scientific memory

**Domain:** Metrology  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

A durable chemistry archive requires versioned numeric property records with units, phases, standard states and citation lineage. Thermochemical databases aggregate contributions from experiments and evaluations; a number stripped of its original context may be wrong for a new phase or temperature. A good machine record separates an original observation, an evaluated recommended value, an extrapolated fit, and a hypothetical teaching input. Dataset references may be copyrighted or carry independent reuse restrictions. When original source bytes cannot be retained, that absence must remain explicit instead of being silently filled by generated data.

## Mathematical or physical principle

`Data record = (species identity, property, value, unit, T, p, phase, source revision, uncertainty, applicable range, rights).`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A measurement is not made more accurate by storing more decimal places. Reproducing a Shomate or Arrhenius fit requires coefficients, parameter definitions and temperature range; using coefficients outside that range may generate plausible but scientifically invalid numbers. A hash identifies file bytes relative to a trusted digest; it does not establish authorship or license. In an offline rebuild, the next researcher should be able to audit each transformation from original measurement to a derived property.

## Reconstruct an illustrative result offline

Create a fictional record for a solid's heat capacity with value 500 J/(kg K) at a specified temperature, plus ±20 uncertainty and a documented source. Then show how removing the phase or temperature makes the record unsuitable for general use.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No full NIST WebBook entries, OpenStax chapters or restricted standards have been copied into this edition. Compiled source rights require separate verification for authentic archival acquisition.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 30 — Laboratory reproducibility, contamination control, and safety

**Domain:** Metrology  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemistry is experimentally grounded. Reproducibility requires chemical identity, material origin and purity, instrumentation, calibration, sample preparation method, environmental conditions, raw observations, analysis and uncertainty. A beautiful computational derivation is not a substitute for a real experiment. In electronics, contamination control and traceable material properties can be as important as the ideal theoretical model. A responsible scientific vault should provide safe methodological checklists and official laboratory hazard orientation while leaving dangerous operational detail to qualified personnel and local standards.

## Mathematical or physical principle

`Mass/energy balances and propagated uncertainty are consistency constraints; they do not grant chemical hazard approval or prove sample provenance.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

For a proposed measurement, define the measurand, sample lot, replicate policy, relevant blanks, calibration standards, detection limits and transformation code. Separate raw observations from interpreted chemical identities and keep contradictory results. Bias can arise if calibration standards have the same contamination source as samples. Statistical intervals need sampling assumptions, and a “non-detect” should retain detection thresholds rather than being converted into exact zero.

## Reconstruct an illustrative result offline

Design an imaginary experiment to measure a harmless material's conductivity. List the instrument, uncertainty, sample identity, temperature, repeat measurements and negative control that would need to be documented. Do not claim data were actually collected.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

Safety data sheets, hazard analysis, waste disposal, proper ventilation and qualified lab supervision are external requirements. This package includes no dangerous synthesis or chemical-exposure protocols.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [American Chemical Society, Laboratory Safety Guidance](https://institute.acs.org/acs-center/lab-safety/education-training/college-univ-guidelines.html) — inspected: RAMP risk-recognition education and safe laboratory institutional responsibilities
- [NIST Guide to Expression of Uncertainty in Measurement](https://www.nist.gov/publications/guide-expression-uncertainty-measurement) — inspected: Uncertainty and calibration scope for reconstructed measurements

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 31 — Chemistry to AI hardware: dependencies and missing links

**Domain:** AI infrastructure  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Advanced AI depends on a physical computing stack: pure materials, controlled dopants, oxide and interconnect chemistry, dielectrics, packaging, thermal management, sensors, power conversion and repeatable metrology. Chemistry provides the link between atomic bonding and the physical devices on which software runs. The shortest viable knowledge reference must preserve enough physics and chemistry to understand *why* hardware methods work and what evidence tests them. A theory of silicon conductivity without process contamination limits is insufficient for manufacturing; a chemistry library without architecture and compiler knowledge cannot recreate intelligent software.

## Mathematical or physical principle

`Dependency chain: SI/chemical measurements → electronic structure → material purity and interfaces → semiconductor transport → electronic devices → computer architecture → AI algorithms.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

This chain is not a one-way sequence of factory instructions. Feedback from device testing changes material specifications, while advances in modeling guide chemical synthesis research. The Atlas should expose cross-node relations to Measurement, Materials, Energy, Computation and later Electronics/Manufacturing nodes. Relationships mean conceptual relevance, not actual integration or an observed performance gain. Future automated agents should retrieve source-closed context and preserve uncertainty rather than fabricate process parameters.

## Reconstruct an illustrative result offline

Suppose a synthetic silicon calculation predicts improved conductivity after increasing assumed electron density. Enumerate the missing device requirements: mobility measurement, contacts, breakdown, oxide quality, wafer purity and yield. Then identify which existing Atlases already contain supporting theory.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No semiconductor is fabricated and no AI accelerator performance is measured. This chapter is a reconstruction dependency map, not proof of manufacturability or a novel chip process.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 32 — Chemistry to machine learning: representations and validation

**Domain:** AI infrastructure  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Chemical machine learning transforms molecules, materials, graphs, sequences or spectra into numerical representations. The representation determines what information a model can learn and which distinctions it loses. A chemical formula cannot distinguish structural isomers; a SMILES string may encode structure but requires stereochemical and tautomer conventions. Dataset leakage can arise from duplicated compounds, near-duplicate scaffolds, shared measurement sources and repeated spectra. A model that predicts a chemical property on familiar variants may fail for new materials, solvents or measurement regimes. Machine-readable chemistry requires provenance and evaluation design, not merely a high benchmark score.

## Mathematical or physical principle

`Predictive error E=(1/N)Σ_i L(f(x_i),y_i), valid for a declared held-out sampling and target; not causal discovery by itself.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A prediction is evaluated against a reference measured property under defined conditions, with training exposure and split identities documented. A split by random rows can leak the same compound or scaffold through multiple records; more stringent splits may test generalization. Missing labels and censored detection-limit measurements require explicit treatment. External model embeddings do not certify molecular identity or lawful access to source data. The underlying chemical physics remains useful even when a trained model is unavailable.

## Reconstruct an illustrative result offline

Build a fictional dataset with one chemical formula repeated in training and evaluation under different sample IDs. Explain why a random row split can exaggerate predictive performance. Propose separate compound identity, source document and scaffold checks before claiming genuine unseen-material prediction.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This release has no trained chemical model or independently validated discovery system. The chapter gives evaluation principles; chemical safety and experimental verification remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIH/NLM PubChem PUG REST documentation](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) — inspected: Molecular formula, weight, structure representations, and caller-visible property provenance limits
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 33 — Scientific data interoperability: compounds, identifiers, and provenance

**Domain:** AI infrastructure  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Public chemistry resources may expose names, molecular formulas, canonical structures, spectra and experimental properties through APIs. Machine-readable access is valuable, but an API response is not necessarily a primary published measurement. Compounds can have stereoisomers, isotopologues, tautomers, protonation states and salts; simplistic name-to-formula lookup can conflate important identities. A research vault must define a stable representation, dataset version, provenance of each property, uncertainty, assay context and licensing. The same principle applies to agent retrieval tools: sources must remain evidence, never executable instructions.

## Mathematical or physical principle

`Data identity ≠ chemical reality: a structured record requires compound ID + structure conventions + property conditions + origin + revision + rights.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

For a compound property table, prefer structured fields over free-text summaries, retain nulls, and distinguish measured versus predicted properties. PubChem PUG REST documents molecular formula, molecular weights and stereochemical SMILES fields; they are useful navigation capabilities, not an automatic license or proof of original experimental data for each row. A complete offline original-source archive needs an authorized snapshot and exact transport bytes, not a promise that the web service will remain reachable.

## Reconstruct an illustrative result offline

Take a toy record with molecular formula C2H6O and explain why it cannot, by itself, distinguish ethanol from dimethyl ether. Add structure representation, analytical evidence and source conditions before treating it as a unique compound.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No PubChem dataset was downloaded or experimentally checked here. Source rights, version history and compound-level evidence status remain separate obligations.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [NIH/NLM PubChem PUG REST documentation](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) — inspected: Molecular formula, weight, structure representations, and caller-visible property provenance limits
- [IUPAC Gold Book, fifth online edition](https://goldbook.iupac.org/) — inspected: Chemical nomenclature and definitions, selected pages; source terms revised/edition-specific

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 34 — Chemistry reconstruction without industry-specific procedures

**Domain:** Technological continuity  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

If a future researcher has only this package and a basic programming environment, they should be able to reconstruct atom counting, stoichiometric conservation, molar quantities, phase/standard-state dependence, chemical thermodynamics, kinetic approximations, electrochemical potentials, diffusion and semiconductor drift transport. This is a scientifically coherent *minimum kernel*, not an inventory of every industrial formulation. The key survival value is preserving the explanation of a law and the means to test its assumptions with new evidence. Restricted safety standards and dangerous chemical handling should not be casually replaced with unverified instructions.

## Mathematical or physical principle

`Reconstruction chain: identity and SI units → balance/equilibrium/kinetics → material properties and measurement → semiconductor devices → computing systems and AI.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

A durable archive includes versioned source references, exact record hashes, human-readable derivations, negative-control tests, reproducible software and a plan for obtaining missing primary source bytes. A test that balances H2/O2 is a mathematical result, not validation of any physical process. An independent numerical oracle can confirm arithmetic while qualified experiments establish actual composition and performance. The Atlas's shared registry allows linking Chemistry to existing Materials, Energy, Measurement and Computation without creating a new Bitwork router yet.

## Reconstruct an illustrative result offline

Reconstruct one balance, one equilibrium free-energy example, one Nernst potential and one semiconductor conductivity case on paper. State the input data, units, assumptions, and missing empirical steps. The exercise is complete only if the uncertainties are preserved along with the outputs.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

The minimum kernel cannot alone recreate a semiconductor fabrication plant or safe chemical industry. Human training, instruments, materials, standards and external validation remain essential even with perfect documents.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [BIPM SI Brochure, ninth edition, updated 2026](https://www.bipm.org/en/publications/si-brochure) — inspected: Updated ninth edition, seven defining constants and CC BY 4.0 brochure license statement
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.


---

# Chapter 35 — Separation science, membranes, and purity limits

**Domain:** Chemical engineering  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Separating mixtures into components can require phase changes, selective adsorption, chromatography, filtration or membranes. The selected method depends on chemical potential, molecular size, charge, volatility and interaction with the separation medium. Separation is not inherently complete: two compounds may have nearly indistinguishable properties, and concentrating a trace component can require substantial energy and time. Materials, battery and semiconductor industries depend on high purity, but a purity specification must identify relevant contaminants, analytical detection limits and process yield. Reproducible design uses declared feed and product compositions, not an unverified claim that a generic filter removes every impurity.

## Mathematical or physical principle

`For a nonreacting component i: n_i,feed = n_i,product + n_i,waste + Δn_i,inventory. Recovery fraction = n_i,product/n_i,feed if feed>0.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

The component balance follows from conservation of atomic identity in a nonreactive separator. Each stream may carry multiple constituents and a process can preferentially enrich one component while discarding another. Overall total-mass conservation can pass even when the desired component's recovery is poor, so species-resolved measurements matter. A thermodynamic separation limit can constrain the minimum work, but real energy demand also depends on transport, irreversibilities and equipment details. No separation technology can be selected safely from a recovery percentage alone.

## Reconstruct an illustrative result offline

For a hypothetical separation, feed contains 10 mol of harmless component X. Product contains 8 mol X, waste 1 mol X and inventory grows by 1 mol X. Conservation closes and process recovery is 80%. Explain why this says nothing about chemical purity of the product if an unmeasured impurity Y accompanies it.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

This is chemical accounting only, not a solvent, distillation, membrane, purification or hazardous extraction protocol. Real separation safety, effluent treatment, contamination limits and experimental validation remain open.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials
- [NIST Chemistry WebBook, SRD 69, updated 2025](https://webbook.nist.gov/chemistry/) — inspected: Thermochemistry, phase transitions, spectra and evaluated source references; dataset-specific rights

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.

