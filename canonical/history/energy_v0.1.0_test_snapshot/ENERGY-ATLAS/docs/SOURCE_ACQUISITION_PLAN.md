# Energy Atlas 0.1 — primary-source preservation and licensing plan

**Strict source status:** 20 new bibliographic source cards, **0 original upstream publisher files obtained**, and 455 source cards across the ten-node collection with **0 authenticated primary publisher transport files**. The public original explanatory text and code are available offline, but no equivalent offline mirror of original scientific publications exists.

## Priorities (in rights-aware order)

1. **NIST/CODATA recommended constants and BIPM SI definitions:** identify exact published edition (2022 CODATA recommended constants, 2025 Reviews of Modern Physics paper; current SI Brochure revision), determine data reuse terms, obtain authentic publisher bytes and original SHA-256. Keep numerical value/uncertainty/reference-date distinctions and derived exact SI values separate. NIST states that its uncopyrighted material is generally public information, with exclusions for copyrighted material; BIPM has its own reproduction rules.
2. **DOE/EIA government-authored technical pages:** DOE web policies treat government information as public domain but warn that some third-party materials are protected. Acquire exact *eligible* pages and data tables with attribution, preserving the original HTML/CSV transport bytes, date, URL and SHA. Do not mirror embedded imagery if third-party ownership is uncertain.
3. **NIST Chemistry WebBook reference data:** verify the specific standard-reference-data terms and individual source licenses. A compiled database is not automatically identical to public-domain government narrative content.
4. **Sandia PVPMC and related NREL/PVWatts modelling documentation:** retain version numbers, exact model equations, licensing, calibration references and the original published problem scope. The local Python function is a deliberately simplified educational approximation, not a reproduction of a real PVWatts installation.
5. **Energy measurement and field trial data:** acquire authorized calibration records, real performance curves, standardized test protocols, site weather and energy data, and independ­ent expert review. Do not substitute hypothetical examples for measurements.

## Attempted acquisition in this edition

Attempted to retrieve the NIST ASCII recommended constants table directly over HTTPS. The sandbox cannot resolve the site through its network path and the download did not succeed. **No publisher transport bytes were archived**, and no source card was upgraded. Instead the release contains `evidence/physical_constants_reference.json`, a labeled original project-created derived table referencing NIST/BIPM. It is *not* the NIST original source file.

## Mandatory evidence before changing source grade

Record source identity, publisher, URL, retrieved timestamp, exact bytes, SHA-256 of original bytes, clear license/attribution, redistribution conditions, original revision and independent provenance review. A matching hash is byte-level fixity relative to an expected digest; it is **not** proof of author identity, correct scientific claims or legal permissions.

## Survival drills

1. Extract a sealed distribution with the network disabled and run the file-manifest/source-closure audits.
2. Choose three energy laws; reproduce their derivations with plain text and arithmetic independent of the Python package.
3. Use separate calibration/experimental evidence when available; clearly mark its absence otherwise.
4. Restore onto different hardware, test all source references and record missing dependency and rights restrictions.
5. Maintain multiple independently verified geographical copies only when a suitable archival destination and permissions are actually available.

**Reconstruction is not a safety license.** Real electrical, pressure, battery and nuclear system work requires qualified engineering, authorizations and applicable technical standards.
