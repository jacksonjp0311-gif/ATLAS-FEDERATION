# ATLAS FORGE — First 24 hours of an extended grid/network outage

**Purpose:** protect people first, preserve offline knowledge second, fabricate only what can be safely powered and inspected. A short power outage does not mean civilization has collapsed. Follow official emergency instructions when applicable.

## 0–2 hours: protect people and power

- Account for household members, medically necessary devices, communications, food/water, heat/cooling and safe shelter.
- Use only manufacturer-approved, properly installed power equipment. **Never run a fuel generator indoors**, near open windows, or within attached garages; never backfeed home wiring. Use carbon monoxide alarms.
- Preserve batteries for lighting, communications, refrigeration or medically critical loads before recreational or nonessential 3D prints.
- Do not use Atlas reference models to certify water potability, medical treatment, combustion equipment, high-voltage wiring, load-bearing structures or pressurized systems.

## 2–6 hours: prove knowledge survives disconnected

- Confirm a full **local** copy of the 11-part ATLAS FORGE v0.5.0 archive, `FULL_ARCHIVE_PARTS_MANIFEST.json`, and `RESTORE_FULL_ATLAS.py`. Files available only in a cloud account are **not available offline**.
- Open the local `SURVIVAL/ATLAS_OFFLINE_PORTAL.html` in a browser or run `python tools/atlas_offline.py catalog`, `audit`, `gaps`, and an example search.
- Prefer two independent storage devices, a printed paper quick guide, and one untouched original release. Verify SHA-256 when restoring.
- If using a local LLM, confirm the model, tokenizer, runtime, retrieval tools, and Python all start disconnected. Basic Atlas lookup does not require a model.

## 6–12 hours: map actual capability

- Inventory **printer model, nozzle, filament type, dry material stock, spare parts, calipers, installed slicer, saved printer/filament profiles and G-code transfer route**.
- Measure actual energy draw (especially initial bed/hotend heating and steady printing); evaluate with `power_budget.py` rather than invented watts.
- Ensure an offline drawing/slicing workflow is installed. A watertight STL is **not** yet G-code. Do not install unknown executable software from untrusted USB media during an emergency.
- Choose one small nonstructural test part, not a critical heat/pressure/water/electrical component.

## 12–24 hours: controlled physical reconstruction trial

- Generate `ATLAS_COIL_FORMER.scad` and `.stl` with `atlas_print_bridge.py`, optionally checking exact record revisions against the offline Atlas.
- Run `verify_mesh.py` before slicing. Check build volume, support geometry, available power, and actual filament profile.
- Slice locally to printer-specific G-code; review the preview, feed path, supports and heated-bed compatibility. Do not assume the model knows your machine.
- Make a physical test print **only when power, ventilation, machine, filament, and safety conditions are ready**.
- Inspect with calipers; record measured hole diameter, flange diameter, height, warping and layer adhesion. Reject an unacceptable part and preserve the failure record. Do not install it in a safety-critical assembly.

## Pass/fail criteria

An end-to-end pass requires: local archive access, local retrieval, source to STL generation, STL integrity, local slicing to correct G-code, actual printer operation on approved power, and physical measurement meeting a documented tolerance. **Today's dry run passes through digital geometry only.**
