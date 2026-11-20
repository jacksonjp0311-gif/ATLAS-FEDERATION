"""Generate or verify a byte-exact source-release manifest. Standard library only."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

EXCLUDED = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "build", "dist", "output"}
MANIFEST = "MANIFEST.sha256"

def members(root: Path) -> list[Path]:
    result = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(p in EXCLUDED or p.endswith(".egg-info") for p in rel.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"symlinks are not release files: {rel.as_posix()}")
        if path.is_file() and rel.as_posix() != MANIFEST and path.suffix not in {".pyc", ".pyo"}:
            result.append(path)
    return sorted(result, key=lambda p: p.relative_to(root).as_posix())

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def generate(root: Path) -> dict:
    paths = members(root)
    text = "".join(f"{digest(p)}  {p.relative_to(root).as_posix()}\n" for p in paths)
    (root/MANIFEST).write_text(text, encoding="utf-8", newline="\n")
    return {"valid": True, "action": "generated", "files": len(paths)}

def verify(root: Path) -> dict:
    expected = {}
    for line in (root/MANIFEST).read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match: raise ValueError("malformed manifest line")
        sha, name = match.groups()
        p = Path(name)
        if name in expected or p.is_absolute() or ".." in p.parts or ":" in name or "\\" in name:
            raise ValueError("duplicate or unsafe manifest path")
        expected[name] = sha
    actual = {p.relative_to(root).as_posix(): digest(p) for p in members(root)}
    missing = sorted(expected.keys()-actual.keys())
    added = sorted(actual.keys()-expected.keys())
    changed = sorted(k for k in expected.keys() & actual.keys() if expected[k] != actual[k])
    return {"valid": not (missing or added or changed), "files": len(actual),
            "missing": missing, "added": added, "changed": changed}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["generate", "verify"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try: result = (generate if args.action == "generate" else verify)(args.root.resolve())
    except (OSError, ValueError) as exc: result = {"valid": False, "error": str(exc)}
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 2

if __name__ == "__main__":
    sys.exit(main())
