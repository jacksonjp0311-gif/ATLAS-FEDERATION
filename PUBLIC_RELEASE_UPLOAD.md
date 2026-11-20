# Publish the verified public derivative asset

**Current status: upload is pending.** The source can be browsed in the existing repository. The current publishing connection cannot upload a binary release asset, and an authenticated release-upload session is unavailable. These are continuation instructions, not an upload receipt.

Use an already authorized GitHub session with release-write access to `jacksonjp0311-gif/ATLAS-FEDERATION`. This procedure does not create credentials or change repository security settings.

## Candidate identity

| Field | Required value |
| :--- | :--- |
| Release tag | `compiler-design-v0.2.0-public` |
| ZIP filename | `ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip` |
| Byte length | 731,933,585 |
| SHA-256 | `9e91db0327913626c9faf56e5221a5016aadeef0509b45c56ffc667bb863090f` |

Use only this **public derivative**. The complete original archive is a different private artifact and is not an upload input.

## Verify the local candidate

From a checkout of the final published source commit, place the verified ZIP and its matching `.zip.sha256` sidecar in a user-chosen `./release-candidate/` directory. Verify the ZIP before uploading:

```sh
python - <<'PY'
from pathlib import Path
import hashlib
p = Path("release-candidate/ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip")
h = hashlib.sha256()
with p.open("rb") as f:
    for block in iter(lambda: f.read(1024 * 1024), b""):
        h.update(block)
if p.stat().st_size != 731933585 or h.hexdigest() != "9e91db0327913626c9faf56e5221a5016aadeef0509b45c56ffc667bb863090f":
    raise SystemExit("Candidate identity mismatch; stop.")
print("Verified public derivative candidate.")
PY
```

Check existing tags/releases first. If `compiler-design-v0.2.0-public` already exists, inspect its target and assets and reuse a verified matching release; do not overwrite or duplicate it. Set `ATLAS_PUBLIC_SOURCE_COMMIT` to the **exact full 40-character source commit from the final publication report**, not a branch name or an earlier partial-source commit. Confirm that this checkout is that commit.

## Create the release with its assets

Run this only after the identity check and the existing-release check succeed. The command creates the release and uploads the assets together; no empty release is needed.

```sh
set -eu
: "${ATLAS_PUBLIC_SOURCE_COMMIT:?Set the verified full public source commit from the publication report}"
test "$(git rev-parse HEAD)" = "$ATLAS_PUBLIC_SOURCE_COMMIT"
gh auth status
gh release create compiler-design-v0.2.0-public \
  ./release-candidate/ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip \
  ./release-candidate/ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip.sha256 \
  ./canonical/PUBLIC_OMISSION_MANIFEST.json \
  ./canonical/FILE_MANIFEST.json \
  ./evidence/publication/PUBLIC_DERIVATIVE_VERIFICATION.json \
  --repo jacksonjp0311-gif/ATLAS-FEDERATION \
  --target "$ATLAS_PUBLIC_SOURCE_COMMIT" \
  --title "Compiler Design v0.2.0 — public derivative" \
  --notes-file ./canonical/PUBLIC_DERIVATIVE_NOTICE.md
```

If authentication or upload fails, preserve the candidate and report the actual result. Do not claim delivery from a created tag or a partial upload.

## Re-download and verify

Use a new empty directory and download the actual release asset, not GitHub's generated source archive:

```sh
mkdir ./public-release-verify
gh release download compiler-design-v0.2.0-public \
  --repo jacksonjp0311-gif/ATLAS-FEDERATION \
  --pattern ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip \
  --pattern ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip.sha256 \
  --dir ./public-release-verify
python - <<'PY'
from pathlib import Path
import hashlib
p = Path("public-release-verify/ATLAS_COLLECTION_Compiler_Design_v0.2.0-public.zip")
h = hashlib.sha256()
with p.open("rb") as f:
    for block in iter(lambda: f.read(1024 * 1024), b""):
        h.update(block)
if p.stat().st_size != 731933585 or h.hexdigest() != "9e91db0327913626c9faf56e5221a5016aadeef0509b45c56ffc667bb863090f":
    raise SystemExit("Public download identity mismatch; stop.")
print("Public derivative download verified.")
PY
```

Record the exact release URL, source commit, asset byte length, SHA-256, and verification result. Update [release status](RELEASE_STATUS.md) and the [verification receipt](evidence/publication/PUBLIC_DERIVATIVE_VERIFICATION.json) only after the public download matches. The [restoration guide](RESTORATION.md) then applies to that verified asset.
