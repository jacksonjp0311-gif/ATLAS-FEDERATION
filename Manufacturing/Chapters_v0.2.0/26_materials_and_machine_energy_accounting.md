# Chapter 26: Mass and energy constraints are reconstruction invariants

**ATLAS FORGE — original canonical fourteen-node federation / Manufacturing v0.2.0.**

**Evidence grade:** independently executable mathematical reference and original authored reconstruction. No physical machine, device, original publisher bytes or expert scientific review have been verified.

## Reconstruction objective and governing invariant

`m_in=m_part+m_scrap+m_recoverable+Δinventory; P=energy/time`

## Scientific derivation and engineering reasoning

Conservation laws offer a way to detect inconsistency before constructing a process. For an operation with measured stock mass m_in, finished part mass m_part, chips/scrap m_scrap and recoverable material m_rec, the remainder must be recorded as inventory, residue, loss or measurement discrepancy. Mass balance does not say the process is efficient, safe or qualified; it only exposes missing accounting.

Existing Manufacturing v0.1 models provide bounded cutting power and removed-volume calculations under hypothetical uniform chip-load assumptions. Mechanical input power must exceed ideal cutting power when efficiency is below one. Combining energy estimates with a resource schedule supports a synthetic lower-bound budget, but machine acceleration, auxiliary loads, lubrication, spindle idle power and thermal dissipation are not included.

Worked scenario: a declared material density times removal volume gives removed mass. Independently compute material removal rate from feed and geometry and multiply by specific cutting energy, then divide by efficiency for an illustrative input-power lower bound. A mismatch beyond declared uncertainty triggers investigation; no numeric output authorizes an actual spindle speed.

The continuity ledger must connect material identity, specimen geometry and measured mass to the measurement chain. No physical material was cut or measured in this Atlas edition.

## Algorithm and independent falsification

Reference method: `manufacturing_atlas.v02_models.manufacturing_atlas.models.cutting_estimate; resource_bounded_schedule`. Verify dimensional assumptions and finite inputs, deliberately inject a missing prerequisite or invalid case, then compare against a separately derived NumPy/SciPy or algebraic reference in `evidence/independent_oracle_v02.py`. A computed result is not a physical calibration certificate.

## Evidence and applicability boundaries

Reference energy and mass relationships are not validated machine setpoints or real tool performance.

Bibliography card: `NIST-AM-QUAL`. These links identify public NIST sources for future verification. Their publisher-original document bytes, redistribution rights and source-to-equation locators were **not** authenticated or archived for this edition. The existing Measurement, Materials, Electronics, Chemistry and Mathematics & Physics nodes provide exact-revision dependencies; no new router is introduced.
