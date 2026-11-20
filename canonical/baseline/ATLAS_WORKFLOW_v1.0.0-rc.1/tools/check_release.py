#!/usr/bin/env python3
"""Create or verify a source-tree SHA-256 manifest. Not an authenticity signature.

Generated caches, environment directories and build outputs are excluded. On a
release tree, verify compares both membership and bytes. Call create deliberately
only after an independently reviewed change; rehashing does not establish truth.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import sys

EXCLUDED = {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache', 'build', 'dist', 'output'}

def members(root):
    result = {}
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if any(x in EXCLUDED or x.endswith('.egg-info') for x in rel.parts):
            continue
        if p.is_symlink():
            raise ValueError(f'Symlink not admitted: {rel}')
        if p.is_file() and p.suffix not in {'.pyc', '.pyo'} and rel.as_posix() != 'MANIFEST.sha256':
            result[rel.as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('operation', choices=['create', 'verify'])
    ap.add_argument('root', type=Path)
    a = ap.parse_args()
    try:
        root = a.root.resolve(strict=True)
        if not root.is_dir():
            raise ValueError('Root must be a directory')
        actual = members(root)
        manifest = root / 'MANIFEST.sha256'
        if a.operation == 'create':
            manifest.write_text(''.join(f'{digest}  {path}\n' for path, digest in actual.items()), encoding='utf-8')
        expected = {}
        for line in manifest.read_text(encoding='utf-8').splitlines():
            digest, path = line.split('  ', 1)
            posix = PurePosixPath(path)
            if len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest) or posix.is_absolute() or '..' in posix.parts or '\\' in path or path in expected:
                raise ValueError('Malformed or duplicate manifest entry')
            expected[path] = digest
        errors = [p for p in sorted(set(expected)|set(actual)) if expected.get(p) != actual.get(p)]
        print(json.dumps({'valid': not errors, 'files': len(actual), 'mismatched_or_missing_paths': errors, 'authorship_or_scientific_truth_proven': False}, indent=2))
        return 2 if errors else 0
    except (OSError, ValueError) as exc:
        print(json.dumps({'valid': False, 'error': str(exc)}))
        return 2

if __name__ == '__main__':
    sys.exit(main())
