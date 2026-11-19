"""Educational offline CLI smoke test, not a security validation."""
from . import hkdf_sha256,AuthenticatedSession,tree_hash
if __name__ == "__main__":
    a=AuthenticatedSession(b"p"*32,b"offline-case",b"reader",b"verifier","client")
    b=AuthenticatedSession(b"p"*32,b"offline-case",b"reader",b"verifier","server")
    encoded=a.send(b"intact reference")
    assert b.receive(encoded)==b"intact reference"
    print({"hkdf_bytes":len(hkdf_sha256(b"input",b"salt",b"label",32)),"authenticity_model":True,"confidentiality":False,"tree_root":tree_hash([b"a",b"b"]).hex()})
