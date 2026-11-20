# Calibration and traceability: structural audit (v0.3)

An unbroken sequence of documented comparisons to a reference is necessary, but is not sufficient to establish metrological traceability. Correctness requires relevant calibration reports, stated uncertainty contributions, competent laboratory practices, applicable measurement conditions, and authenticity checks. This library **does not** issue calibration certificates.

Use `measurement_atlas.traceability.audit_chain(nodes,edges,measurement_id=...)` to inspect graph connectivity. Nodes carry `id`, `kind`, `description`, `source_url`, and optional `valid_through` (YYYY-MM-DD). Edges point from a measured item to its calibration/reference parent. Flagged missing documentation, expired dates, cycles, and missing terminal reference standards are reasons for follow-up rather than a certification verdict.

**Primary reading route:** [NIST TN 1297](https://www.nist.gov/pml/nist-technical-note-1297) for uncertainty; [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure) for SI definitions; [JCGM 100 GUM](https://www.bipm.org/en/committees/jc/jcgm/publications) for formal uncertainty guidance. These are navigational links; no full-document or calibration-certificate audit was performed for v0.3.
