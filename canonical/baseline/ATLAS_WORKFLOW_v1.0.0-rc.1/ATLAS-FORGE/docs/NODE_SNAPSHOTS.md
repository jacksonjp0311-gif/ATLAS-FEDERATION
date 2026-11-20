# Node snapshot provenance

The import receipt is [NODE_IMPORT_RECEIPT.json](../registry/NODE_IMPORT_RECEIPT.json). It records exact source commits, upstream paths, file sizes, SHA-256 hashes and compared Git blob IDs.

Signal Atlas uses its published v1.0 claim and source files. The available earlier owner archive was completed with the later records retrieved through GitHub. Both final files, including CRLF line endings, were compared to the Git blob IDs at `234b65fdb4f64add7fa53d5ea8312a63bcf616b4`; both matched. The node includes 82 claims and 150 source cards, not all upstream lessons, datasets or application code.

Cymatics Atlas uses four reference files that were already present in the retained v0.6.0 source package. Each file's Git blob ID was compared to the corresponding v1.0.0 file at `21fba3ec77225d14ef81a6d761fa0922d8002d56`; all four matched. Reusing the older bytes is therefore an exact data reuse, not an assumption that the releases were identical. Other upstream files and executable code are outside this node.

Measurement Atlas reuses the existing five-heading starter and its one NIST source card. It is not independently reviewed or newly published. Its original starter remains unchanged in examples.

No third-party full papers or raw external measurements were downloaded for this integration. Reference URLs have not been comprehensively rechecked for availability. Upstream correction notices and new releases do not propagate automatically. The metadata capture date is not a new scientific review date.

## v0.3 retention

Measurement Atlas v0.1 reference files remain byte-preserved at `nodes/measurement-atlas/0.1.0/`. The enabled Measurement v0.3 node pins three updated metadata files; mathematical functions reside only in the separate Measurement distribution. Signal and Cymatics snapshots and upstream Git pins are unchanged.

## v0.3 retention

Measurement Atlas v0.1 reference files remain byte-preserved at `nodes/measurement-atlas/0.1.0/`. The enabled Measurement v0.3 node pins three updated metadata files; mathematical functions reside only in the separate Measurement distribution. Signal and Cymatics snapshots and upstream Git pins are unchanged.
