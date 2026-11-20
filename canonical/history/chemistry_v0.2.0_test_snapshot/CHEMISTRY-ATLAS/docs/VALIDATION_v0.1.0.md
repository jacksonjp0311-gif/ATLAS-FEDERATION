# Chemistry Atlas v0.1.0 — Executed validation and open scientific gates

**Status:** substantive first offline scientific reference, **not** scoped Chemistry v1, peer-reviewed chemical science, real semiconductor fabrication, or proven AI performance improvement.

## Executed source-tree software and arithmetic tests

- **1,811 tests passed, zero failures and skips** across 13 unchanged/historical and new suites. Earlier Energy v1 tests run against a verified exact ten-node historical registry, not Chemistry's eleven-node registry.
- **8,064 independently implemented NumPy comparisons passed** on original author-generated cases: formula/mole arithmetic, ideal gas, equilibrium Gibbs energy, Nernst electrochemistry, Arrhenius kinetics, semiconductor conductivity, diffusion and mass conservation. The largest absolute difference in tested numbers is 5.82077e-11, not a calibrated experimental error bound.
- Complete eleven-node metadata federation: **2,220 records, 1,391 typed relations and 480 bibliographic source cards**. All **71** source-linked context assemblies validate. `fastjsonschema` compiled the full schema over the corpus; independent Draft 2020-12 validation was limited to selected bounded examples.
- **3,226 earlier files byte-identical** to the complete previous Energy v1 archive, including 2,052 previous scientific records, 1,245 prior relations, all earlier domain code and original history.
- Clean offline wheel installation passed without source-tree imports, exposing Chemistry's 168 records and 140 local relationships. Six cross-domain related-to links exist only in the full federation, where targets are source-closed.
- Strict offline survival audit: **2220 records, 1391 relations, 480 bibliographic source cards**, **0 authenticated locally retained original publisher source files**.

## What tests do *not* establish

- Balancing neutral chemical equations is necessary atomic arithmetic, not a successful or safe synthesis. Charged species and isotopic reactions are deliberately unsupported.
- Standard atomic weights depend on isotope mixture and source; the reference requires caller-supplied masses. Published SI defining constants have exact numerical values, but actual samples are not automatically exact.
- Nernst electrochemical potentials require activities and externally verified standard potentials; no working cell, battery safety, or practical electrolyte synthesis was validated.
- Semiconductor carrier transport assumes caller-supplied mobility and density; no impurity activation, oxide fabrication, processor demonstration or AI acceleration was measured.
- Original publisher texts were not archived. The OpenStax Chemistry 2e license is edition-sensitive and public pages disagree on reuse terms, so its text was *not* copied.
- No safe chemical laboratory, industrial process, environmental measurement or hazard assessment was certified. This package is an educational reference and preserves official safety guidance only as citations.

## Reproduction after sealing

From extracted root: `python tools/check_manifest.py verify .`, `python tools/survival_audit.py --root . --check-files`, and `python tools/check_collection.py --out /external_unique_path`. From Chemistry directory: `python -m chemistry_atlas`, `python -m unittest discover -s tests -q`, `python tools/numerical_oracle.py` (requires NumPy). The *final external audit* records the post-extraction replay rather than assuming it passed from source.
