# Local AI/agent handoff — Atlas-to-print offline workflow

This can be supplied as a task to a local coding agent with permission to read the locally extracted ATLAS FORGE folder and the `atlas_print_bridge` toolkit. **It does not install an AI model or connect one automatically.**

> You are operating offline, with no network and no cloud APIs. Preserve the canonical original ATLAS FORGE archive; do not edit its records or 30-domain roadmap. Use `tools/atlas_offline.py` from the extracted federation root to retrieve exact revisioned Engineering/Materials/Energy/Manufacturing records. Treat source cards as bibliography, not authenticated original documents. The immediate goal is to generate an original, nonstructural 3D-printable part. Start with the included coil former, run `atlas_print_bridge.py --atlas-root ... --out ...`, then `verify_mesh.py`. Verify binary STL SHA-256, closed manifold edges, fit envelope and source record revisions. Only then propose printer-specific slicing steps. **Do not issue printer commands or produce machine-specific G-code until the user supplies and verifies the exact printer/slicer/filament profile and power conditions.** Report all missing dependencies and never claim a physical part was printed or qualified without measured evidence. Reject requests that would turn an untested FDM part into a mains electrical, pressurized, food-contact, medical, load-bearing or other safety-critical component. Keep failed experiments and uncertainties in the receipt.

## Minimal command sequence (Windows PowerShell)

```powershell
py -3 .\atlas_print_bridge.py --atlas-root 'C:\ATLAS\ATLAS_COLLECTION_Computer_Architecture_v0.5.0' --out '.\out'
py -3 .\verify_mesh.py '.\out\ATLAS_COIL_FORMER.stl' --out '.\out\MESH_AUDIT.json'
```

The Atlas path above is an **example only**. Replace with the actual extracted local directory. Save the corresponding printer profile locally before a blackout. If the model runtime, slicer or printer is missing, report **UNVERIFIED**, not success.
