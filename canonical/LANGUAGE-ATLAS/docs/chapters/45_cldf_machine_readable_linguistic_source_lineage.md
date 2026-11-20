# 45. Cross-Linguistic Data Formats and reproducible scholarly evidence

An archive of linguistic measurements must be more than a spreadsheet. The Cross-Linguistic Data Formats (CLDF) specification builds on the W3C CSV on the Web model and uses UTF-8 CSV data with a JSON metadata description. It supplies conventional data modules and field meanings, identifiers, foreign-key relationships, sources and standards for null values. A reproducible human-language knowledge base needs a similar separation between observed claims, their sources, the analysis performed, and the derived quantitative results.

## Why column metadata matters

A column labeled `Language` may contain names, codes or local IDs; `Form` may contain orthography or IPA tokens; `Value` can be a coded observation or missing. Without precise field semantics, future readers may conflate no data with the linguistic absence of a feature. CLDF's documented missingness model distinguishes a row not extracted from source from a row whose source explicitly marks a value as null. Both can require different analysis.

A source reference should point to a stable bibliographic record, with page or context where known. Data transformations need exact code, version and parameters. If a researcher normalizes Unicode strings, removes punctuation, combines dialects or maps IPA symbols, the resulting dataset must not be represented as raw observation. The original file bytes, if lawfully retained, need independent hashes, source rights and a transformation lineage.

## Reproduction path

For a single fictitious language-feature dataset, create `languages.csv` with stable IDs, `features.csv` with explicitly nullable values, `sources.bib`, and metadata describing table/field relationships. Check referential integrity and source identifiers before aggregating. Record which table records are user-created examples versus observed community data. For a real dataset, do not assume that the CLDF schema implies legal rights to redistribute recordings or texts.

The current Atlas uses its own common JSONL contract; it does **not** claim full CLDF 1.3 conformance or a complete CLDF importer. This chapter teaches how an independently understandable source format supports survival beyond a particular database or web server.

**Source:** Official CLDF specification (public GitHub and CLDF project site), selected conformance and source-provenance sections. The exact specification bytes have not been archived locally.
