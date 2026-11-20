# 31. Ingest materials data without losing the physical meaning

## One dataset, many identities

A materials database often stores a property alongside a chemical formula and a scalar numerical value. That is not sufficient to determine whether two numbers refer to the same physical quantity. A robust record must distinguish *element vs compound vs mixture vs device*, exact composition, crystal structure/phase fractions, orientation, processing history, sample condition, environment and temperature, measurement mode and frequency, units, uncertainty, source license and provenance. When a property is computational, it additionally needs model class, functional or force field, code/library version, correction scheme, convergence settings and structural relaxation protocol.

## Provenance requirements

At minimum include: stable source ID and access URL; inspected portion; source record time and scientific publication/version; data licensing; acquisition type (author-measured, publisher table, transcription, calculation, simulation); local content hash where bytes are stored; original transport-byte hash if authenticated (otherwise `null`); transformation script and code version; row counts, parsing policy and validation outputs; missing values and selection mechanism; statistical aggregation level; and explanatory limitations. A hash authenticates a **representation's bytes**, not the authority or physical correctness of their contents.

## The copper example

Hahn1 and NIST WebBook copper data should not be merged into a single “copper curve.” Hahn1 is a nonlinear least-squares benchmark using published observations of a thermal expansion-related response; its response scaling was not authenticated in this package. NIST WebBook provides a compiled solid-copper thermodynamic fit for Cp, relative H and S, with explicitly defined temperature range and units. A naive database join on the string “copper” would erase the difference between measured response, fitted thermodynamic representation, uncertainty and physical sample. A correct join uses typed quantities and retains both evidence sources and their differences.

## Import and validation workflow

A well-formed importer must reject unknown material states, record raw and normalized units separately, verify conversion dimension, and keep the original source text/number when rights permit. For tables, validate row counts and ordering, normal ranges, missingness, scale factors and numeric parsing, and use read-only immutable snapshots. Multiple source pages can be different displays of the same underlying experiment; do not count them as independent replications. A benchmark dataset designed to verify a numerical solver can be useful for algorithms without proving physical materials performance.

## Versioning and rollback

The common contract includes record ID, revision, source closure, evidence maturity, original ID, rights and typed relationships. In this release all previous Materials record revisions are required to survive byte-identically in the new node. Added records and links get new revisions. No previous source is silently reinterpreted as newly verified. A curated model can be updated in a future release without rewriting old experiments. The source register records what was actually inspected, including access failures and partial views.

**Quality test:** can a consumer distinguish “published rounded table matches the local Shomate calculation” from “a real manufactured copper heat sink meets its service requirement”? If not, the record packaging has lost scientific meaning even when its JSON schema passes.
