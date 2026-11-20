# ATLAS FORGE / Software Recovery — Offline Field Card

**Inputs:** an intact copy of the canonical Atlas archive, a working local Python runtime, enough safe electrical power, writable storage, and verified media hashes.

1. Verify the archive's SHA-256 against its independent manifest before extracting.
2. Search for the application/record needed and preserve its exact revision.
3. Run `python -m patterns_atlas` in a disposable directory. Expect a two-entry SQLite ledger and a recovered snapshot.
4. Test duplicate IDs, corruption refusal, and one injected interruption. Require explicit pass/fail receipts.
5. For real external equipment, treat all actions as unverified until separate instrument/output evidence is gathered. **Never** assume retry is safe just because software returned an error.
6. Keep two offline copies, write-protected if possible, plus printed recovery instructions. Maintain hardware battery and storage-health records.

**HOLD:** no real controlled power-cut experiments, no distributed exactly-once delivery, no authenticated external firmware or qualified safety approval.
