# 25. Mass-loss corrosion rates are not maximum damage depths

**Sources:** NIST-hosted *Corrosion of Copper and Steel Alloys in the Presence of Acetobacter sp.* (Sowards and Mansfield, July 2013), notably its section labelled corrosion-rate measurements; a bounded ASTM G31 formula is displayed. [Publisher-hosted presentation](https://www.nist.gov/system/files/documents/mml/acmd/2013-07-22-Corrosion-of-Copper-and-Steel-Alloys-Sowards.pdf). The publisher PDF's extracted text was checked; a requested screenshot failed because the retrieval cache missed. We therefore do **not** claim a visually authenticated full-PDF review or a licensed reproduction of the ASTM standard.

## Define the measurement

An immersion coupon's corrected **mass loss W**, exposed **surface area A**, duration **t**, and measured **density ρ** can determine an average *equivalent uniform penetration*. For W in grams, A in cm², ρ in g/cm³ and t in hours:

`average penetration rate (mm/y) = 87600 W/(A ρ t)`.

The coefficient follows directly from `W/(Aρ)` cm thickness, times 10 mm/cm and 8760 hours per 365-day year. The NIST-hosted presentation prints 8.76×10⁴ for mm/y under the same units. Neither the exact standard nor all cleaning and specimen requirements are included in this Atlas. The qualified investigator must consult the applicable current standard and report the testing conditions.

## Worked result

A hypothetical coupon loses **0.10 g** after **240 h**, with **100 cm²** exposure area and **7.8 g/cm³** density. The arithmetic gives **0.0467948718 mm/y equivalent uniform penetration**. Doubling the corrected loss while holding the same area, time and density doubles this calculated average. These are **synthetic inputs**, not data from the NIST experiment and not a corrosion rate for all carbon steels.

## Where the simple estimate fails

A coupon can have substantial localized attack while its total mass loss is low. If the specimen has pits, under-deposit corrosion, crevice corrosion, galvanic coupling, biofilms, selective corrosion, or oxide retention, an average equivalent penetration can seriously understate the maximum local depth. Coupon cleaning may also remove substrate or leave corrosion products, so the corrected mass loss needs a laboratory procedure and uncertainty budget. Uniform area may change, time dependence need not be linear, and the application environment can differ substantially from the bath chemistry. Zero resolved mass loss does not establish zero corrosion or absence of pits.

**Minimum provenance:** source material grade and composition; processing/heat treatment; exposed area and masking; exact duration; solution composition/pH, dissolved oxygen and temperature; cleaning method and blank correction; instrument mass calibration, detection limit, density basis; macroscopic and microscopic damage inspection; replicate distribution; uncertainty and traceability; sample selection. Without this, output remains a geometry calculation on supplied numbers.

**Refuse the inference** “the wall has N years remaining” from coupon mass-loss arithmetic. Predicting life requires actual local wall-thickness records, local attack morphology, damage propagation, safety factors and engineering standards. The interface returns `not_inferred` fields for these targets.
