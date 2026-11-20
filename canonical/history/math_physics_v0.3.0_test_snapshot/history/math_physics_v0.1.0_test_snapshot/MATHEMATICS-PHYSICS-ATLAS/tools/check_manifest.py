"""Verify or generate a file inventory; hashes establish bytes, not truth."""
from pathlib import Path
import argparse,hashlib,json,sys
IGNORED={"__pycache__",".pytest_cache",".git",".venv","build","output"}
def members(root):
    return {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file() and p != root/"FILE_MANIFEST.json"
            and not any(x in IGNORED or x.endswith(".egg-info") for x in p.relative_to(root).parts)
            and not p.name.endswith(".pyc")}
def main():
    a=argparse.ArgumentParser();a.add_argument("action",choices=["generate","verify"]);a.add_argument("root",type=Path);x=a.parse_args()
    root=x.root.resolve();p=root/"FILE_MANIFEST.json";actual=members(root)
    if x.action=="generate":
        if p.exists():raise SystemExit("Refusing to overwrite an existing inventory; review before regenerating")
        p.write_text(json.dumps({"schema":"atlas.file-inventory/1","files":actual,"claim":"byte consistency only; not a digital signature or scientific certification"},indent=2)+"\n")
        print(json.dumps({"result":"generated","files":len(actual)}));return
    expected=json.loads(p.read_text())["files"];changed=sorted(k for k in set(actual)|set(expected) if actual.get(k)!=expected.get(k))
    print(json.dumps({"result":"passed" if not changed else "failed","files":len(actual),"changed_missing_or_extra":changed}));raise SystemExit(bool(changed))
if __name__=="__main__":main()
