# Investigation 13 — Correct mass loss does not establish maximum corrosion damage

**Stated observations:** none. The input is a constructed laboratory coupon scenario, not a published experiment or field sample. A hypothetical specimen starts and ends with a corrected mass loss of 0.1 g, has 100 cm² exposed area, is immersed for 240 h, and has an assumed density of 7.8 g/cm³.

**Model.** Equivalent average uniform penetration `87600 W/(Aρt)` gives **0.0467948718 mm/year**. This equals geometric conversion of the hypothetical loss into a mean thickness. A second hypothetical coupon losing 0.2 g under identical conditions returns exactly twice the average rate. The software unit tests check proportionality and reject negative loss and zero area/duration/density.

**Failure mode.** Suppose almost all attack is concentrated at one small crevice. The same overall mass loss could be compatible with a deep local pit or a shallow uniform film because the mass integral does not uniquely specify its spatial distribution. The output must therefore never be relabeled as the maximum pit depth, minimum remaining wall thickness, or safe-life estimate. A specimen with zero resolved mass loss also does not prove absence of galvanic or localized damage.

**What would be needed.** Full solution and specimen preparation records, cleaning/blank corrections, initial and final calibrated masses, cross-sectional damage mapping, pit-depth distribution, exposed-area map, replicate specimens, microstructural information, and actual service environment. A governing corrosion standard may require licensed access and qualified execution.

**Source inspection boundary.** The formula and 8.76×10⁴ mm/y factor occur in a NIST-hosted presentation attributed to Sowards and Mansfield, referencing ASTM G31. The text was retrieved, but web PDF screenshot verification failed due to cache access. This release records that limitation; it does not claim a fully inspected current ASTM practice. [NIST source link](https://www.nist.gov/system/files/documents/mml/acmd/2013-07-22-Corrosion-of-Copper-and-Steel-Alloys-Sowards.pdf).

**Outcome:** a verifiable arithmetic teaching case coupled to a required refusal on localized failure or remaining service life.
