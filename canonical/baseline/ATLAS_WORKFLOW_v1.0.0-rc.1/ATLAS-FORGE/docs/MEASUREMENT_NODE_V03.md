# Measurement Atlas integration in Forge v0.3

Measurement Atlas v0.3 is enabled by default as a reference node. Its five original NIST section-heading packets and one original reference record remain editorial navigation metadata. The actual numerical library stays in its separate MEASUREMENT-ATLAS v0.3 distribution; this node **does not** execute the model or import calibration certificates.

Forge's bundled reference snapshot is pinned to SHA-256 digests of `data/packets.jsonl`, `data/sources.json`, and `atlas_manifest.json`; integrity failures reject the node. The original v0.1 snapshot is retained for historical comparison.

The numerical package adds first-order uncertainty budgets, Type B uniform/triangular distribution assumptions, and calibration-chain documentation checks. No physical measurements or independent certifications are newly included. For numerical use, install the separate package. For reference navigation, use Forge search. Tested pathways are distinct; referencing an interface does not establish a live connection to a desktop application.
