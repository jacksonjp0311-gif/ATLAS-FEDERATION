# ATLAS FORGE — Blackout fabrication readiness companion v0.1.0

**One original Atlas federation.** This is an additive, removable field test placed under `/ATLAS FORGE/Continuity_Toolkit/`, not a new research federation, not an update to `CURRENT_CHECKPOINT.json`, and not a completion claim for an original scientific domain.

## What works now (tested in the assistant's isolated runtime, not on your computer)

1. Exact v0.5.0 federation recovered from 11 verified volumes: 711,416,573 bytes, SHA-256 `ea4b1f70eeaabeec0ea5b553c27bf4b3e094efc1280b1067c3c4754247b3bf8e`.
2. Offline archive and graph audit: 15 nodes, 3,235 records, 2,415 qualified relationships, 9,364 verified file hashes, 4,830 exact relationship endpoint references.
3. Local literal search works without a model or internet; the original content is *not* a comprehensive hands-on CAD/slicer encyclopedia.
4. The new `atlas_print_bridge.py` creates a **nonstructural coil-winding former** with Python standard library only. Exact-revision links to six original Atlas records are included in `DESIGN_EVIDENCE.json` when given `--atlas-root`.
5. The binary STL passes native closed-edge and outward-normal verification. OpenSCAD independently renders the same object to STL and was compared in this test environment. **This proves digital geometry only.**
6. A current local AI agent, printer, printer profile, backup battery, 3D-print quality and an actual printed part are **not** verified.

## Immediate Windows offline command

Place this toolkit beside a *locally extracted* complete Atlas and run from PowerShell (replace the example path):

```powershell
.\BUILD_WINDOWS_OFFLINE.ps1 -AtlasRoot 'C:\ATLAS\ATLAS_COLLECTION_Computer_Architecture_v0.5.0'
```

Or run portable Python directly:

```powershell
py -3 .\atlas_print_bridge.py --atlas-root 'C:\ATLAS\ATLAS_COLLECTION_Computer_Architecture_v0.5.0' --out '.\ATLAS_PRINT_OUTPUT'
py -3 .\verify_mesh.py '.\ATLAS_PRINT_OUTPUT\ATLAS_COIL_FORMER.stl'
```

Modify printer geometry only within the script's checked bounds (`--flange-mm`, `--core-mm`, `--bore-mm`, `--barrel-length-mm`, `--shoulder-rise-mm`). Verify fit and 45-degree shoulder; do not assume a nominal 8.4 mm bore fits an 8.0 mm shaft on an uncalibrated printer.

## Never conflate these gates

`Atlas file hash PASS` → `knowledge link PASS` → `digital CAD/STL PASS` → `slicer/G-code UNKNOWN` → `powered printer UNKNOWN` → `physical part fit UNKNOWN` → `component performance NOT VERIFIED`.

No layer promotes the next automatically. A printable polymer coil former cannot produce copper wire, magnets, batteries or a fabricated CPU. FDM printed parts are not a substitute for tested safety-critical components.

## Included

- `READINESS_ASSESSMENT.md`, `READINESS_MATRIX.json`, `BLACKOUT_FIRST_24_HOURS.md`
- `atlas_print_bridge.py`, `verify_mesh.py`, `power_budget.py`, `BUILD_WINDOWS_OFFLINE.ps1`
- `LOCAL_HARDWARE_INVENTORY_TEMPLATE.json`, `RECONSTRUCTION_BOM.csv`, `LOCAL_AGENT_HANDOFF.md`
- `outputs/ATLAS_COIL_FORMER.scad`, `outputs/ATLAS_COIL_FORMER.stl`
- `outputs/MESH_AUDIT.json`, `outputs/DESIGN_EVIDENCE.json`, `outputs/PRINT_AND_INSPECT.md`
- `tests/` for zero-network repeatable checks and `TEST_LOG.txt`

## Sources for the manufacturing boundary

- Official OpenSCAD command-line reference: https://files.openscad.org/documentation/manual/Using_OpenSCAD_in_a_command_line_environment.html
- Official PrusaSlicer profile management: https://help.prusa3d.com/article/how-to-import-and-export-custom-profiles-in-prusaslicer_382766
- NIST on fused-filament geometry and mechanical property variation: https://www.nist.gov/publications/processing-structure-property-relationships-polycarbonate-samples-prepared-fused

This package is an executable proof of **offline knowledge-to-printable-geometry**, not a printer-field certification or full technological reconstruction.
