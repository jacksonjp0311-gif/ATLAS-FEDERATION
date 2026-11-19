"""RFC 6962-style CT hash-tree educational reference; not a signed CT log."""
from __future__ import annotations
from hashlib import sha256

def leaf_hash(leaf: bytes) -> bytes:
    if type(leaf) is not bytes: raise TypeError("leaf bytes required")
    return sha256(b"\x00" + leaf).digest()

def node_hash(left: bytes, right: bytes) -> bytes:
    if type(left) is not bytes or type(right) is not bytes or len(left)!=32 or len(right)!=32:
        raise ValueError("invalid node digests")
    return sha256(b"\x01" + left + right).digest()

def _split(n: int) -> int:
    if n<2: raise ValueError("need at least two leaves")
    return 1 << ((n-1).bit_length()-1)

def tree_hash(leaves: list[bytes] | tuple[bytes,...]) -> bytes:
    if not isinstance(leaves,(list,tuple)): raise TypeError("leaves must be ordered list/tuple")
    if not leaves: return sha256(b"").digest()
    if len(leaves)==1: return leaf_hash(leaves[0])
    k=_split(len(leaves))
    return node_hash(tree_hash(leaves[:k]),tree_hash(leaves[k:]))

def inclusion_proof(leaves: list[bytes] | tuple[bytes,...], index: int) -> tuple[bytes,...]:
    if not isinstance(leaves,(list,tuple)) or type(index) is not int or not 0<=index<len(leaves):
        raise ValueError("invalid leaf index / set")
    if len(leaves)==1: return ()
    k=_split(len(leaves))
    if index<k: return inclusion_proof(leaves[:k],index)+(tree_hash(leaves[k:]),)
    return inclusion_proof(leaves[k:],index-k)+(tree_hash(leaves[:k]),)

def verify_inclusion(leaf:bytes,index:int,size:int,proof:tuple[bytes,...],root:bytes)->bool:
    if type(leaf) is not bytes or type(index) is not int or type(size) is not int or type(root) is not bytes or len(root)!=32:
        return False
    if not (0<=index<size<=2**32) or not isinstance(proof,tuple) or any(type(x) is not bytes or len(x)!=32 for x in proof):
        return False
    # Rebuild via the same balanced tree decomposition, consuming the proof
    # from the bottom and requiring *exactly* one sibling at each split.
    def rebuild(lo:int, n:int, i:int, cursor:list[int])->bytes:
        if n==1: return leaf_hash(leaf)
        k=_split(n)
        if i<k:
            l=rebuild(lo,k,i,cursor)
            if cursor[0]>=len(proof):raise ValueError("short proof")
            r=proof[cursor[0]];cursor[0]+=1
        else:
            r=rebuild(lo+k,n-k,i-k,cursor)
            if cursor[0]>=len(proof):raise ValueError("short proof")
            l=proof[cursor[0]];cursor[0]+=1
        return node_hash(l,r)
    try:
        idx=[0]
        result=rebuild(0,size,index,idx)
        return idx[0]==len(proof) and result==root
    except (ValueError,RecursionError):return False
