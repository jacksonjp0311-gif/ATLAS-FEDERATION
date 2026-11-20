# ATLAS FORGE v0.2.0 release audit

**Date:** 11 November 2026. **Scope:** local source release and clean-installed wheel.
This audit concerns software integration and snapshot identity, not independent scientific review.

## What changed

Signal Atlas and Cymatics Atlas are implemented as independent, namespaced reference nodes.
Measurement Atlas remains a starter node excluded from default retrieval. Forge can discover,
verify, search and export the bundled knowledge offline through Python and CLI, with a local
read-only HTTP API and node portal. Upstream application code is not executed or merged.

| Node | Pinned source | Searchable records |
| --- | --- | ---: |
| Signal Atlas | v1.0, commit `234b65fdb4f64add7fa53d5ea8312a63bcf616b4` | 232 |
| Cymatics Atlas | v1.0.0, commit `21fba3ec77225d14ef81a6d761fa0922d8002d56` | 132 |
| Measurement Atlas | Local v0.1.0 starter | 6 |

Default searchable records: **364**. With starter opt-in: **370**. These counts combine different
record types, including source-navigation cards; they are not counts of independently verified findings.

## Executed checks

| Check | Actual outcome |
| --- | --- |
| Full Python test suite | **72 passed**, Linux, Python 3.13.5 |
| Original builder regressions | All original 19 tests retained and passing |
| New federation and HTTP regressions | 53 passing tests |
| All-node snapshot verification | Three nodes passed; nine local raw reference files |
| Published raw-file identity | Six imported published files match pinned upstream Git blob hashes |
| Schema validation | Registry and all three manifests passed Draft 2020-12 schema checks |
| Starter validation | Five packets and one source passed existing validator |
| JavaScript syntax | `node --check` passed |
| Wheel | Built locally without dependency downloads |
| Clean wheel installation | Installed offline in a new environment; imported outside the source tree |
| Installed-package checks | Three nodes, 364/370 exports, two-node search, installed HTTP API and portal assets passed |
| Browser rendering/interaction | Chromium desktop and mobile layouts passed with real Federation data through a test adapter |
| Browser console | No page errors; mobile test detected no horizontal overflow |
| Complete browser-to-HTTP session | **Not run successfully**: environment browser policy blocked loopback navigation |
| Windows execution | **Not executed here**; Windows launchers and CI matrix supplied |
| Hosted GitHub CI | **Not run for this local release** |

The browser test used local HTML/CSS/JavaScript and a fetch test adapter backed by the actual
Federation API. HTTP behavior was exercised separately over real loopback requests. These are
complementary tests, not a claim of full browser-to-server end-to-end coverage. Symlink-escape
checks run where the operating system permits creation of the symlink test fixture.

Receipts: [test log](receipts/tests.log), [browser checks](receipts/browser_results.json),
[clean-install smoke](receipts/wheel_smoke.json), and [import provenance](../registry/NODE_IMPORT_RECEIPT.json).

## Reproduce

```powershell
py -3 -m pip install -e .
py -3 -m unittest discover -s tests -v
py -3 -m atlas_forge verify-nodes
py -3 -m atlas_forge validate examples/MEASUREMENT-ATLAS
py -3 -m atlas_forge search "frequency uncertainty"
py -3 scripts/check_release.py verify
```

The release includes `MANIFEST.sha256`. The verifier checks missing, changed and extra source
files, ignoring documented build/cache directories. `.gitattributes` disables Git line-ending
conversion so pinned reference bytes survive Windows checkouts. Hashes are consistency checks,
not signatures; a party who can replace both content and expected hashes can replace the package.

## Boundaries

Only selected reference metadata and claims are imported. Upstream research PDFs, simulators,
websites and raw experimental datasets are not bundled. Their source citations and rights
remain in the records. No claim was promoted to stronger evidence by import. No independent
review, new physical experiment, retrieval-quality benchmark, model improvement or measured
research-cost reduction was performed. Ranking is deterministic lexical matching, not semantic
sufficiency verification. Reference snapshots are frozen, not live-synchronized.

The nine other roadmap domains remain proposals. The original repositories were not changed.
This release has not been pushed to GitHub or installed on the user's computer.
