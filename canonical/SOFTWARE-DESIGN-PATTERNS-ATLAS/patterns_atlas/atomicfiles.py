"""Content-addressed immutable blobs + atomically published local head pointers.

Atomic same-filesystem replace protects visibility of a pointer on supported OS,
not physical power-loss survival, cryptographic authorization, or malicious
filesystem attack resistance. No symlink traversal or arbitrary path writes.
"""
from __future__ import annotations
from pathlib import Path
import hashlib,os,re,tempfile

_KEY=re.compile(r'^[a-z][a-z0-9_.-]{0,63}$')
_HASH=re.compile(r'^[0-9a-f]{64}$')

class SnapshotError(ValueError):pass

class ContentStore:
    def __init__(self,root):
        self.root=Path(root)
        if self.root.is_symlink():raise SnapshotError('symlink root refused')
        self.root.mkdir(parents=True,exist_ok=True)
        self.root=self.root.resolve()
        for name in ('blobs','heads'):
            p=self.root/name
            if p.is_symlink():raise SnapshotError('symlink directory refused')
            p.mkdir(exist_ok=True)

    def _atomic(self,target,data):
        if len(data)>1_048_576:raise SnapshotError('file exceeds 1 MiB bound')
        if target.is_symlink():raise SnapshotError('symlink leaf refused')
        fd,tmp=tempfile.mkstemp(prefix='.atlas-',dir=str(target.parent))
        try:
            with os.fdopen(fd,'wb') as stream:
                stream.write(data);stream.flush();os.fsync(stream.fileno())
            os.replace(tmp,target)
            # Directory fsync is platform-dependent; best effort, not a proof.
            if os.name=='posix':
                try:
                    d=os.open(target.parent,os.O_RDONLY)
                    try:os.fsync(d)
                    finally:os.close(d)
                except OSError:pass
        finally:
            if os.path.exists(tmp):os.unlink(tmp)

    def put(self,data:bytes):
        if type(data) is not bytes or not 1<=len(data)<=1_048_576:raise SnapshotError('bounded nonempty bytes required')
        digest=hashlib.sha256(data).hexdigest()
        path=self.root/'blobs'/digest
        if path.is_symlink():raise SnapshotError('symlink blob refused')
        if path.exists():
            if path.read_bytes()!=data:raise SnapshotError('existing digest path corrupted')
        else:self._atomic(path,data)
        return digest

    def get(self,digest):
        if type(digest) is not str or not _HASH.fullmatch(digest):raise SnapshotError('invalid digest')
        path=self.root/'blobs'/digest
        if path.is_symlink() or not path.is_file():raise SnapshotError('missing or symlink blob')
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=digest:raise SnapshotError('blob content mismatch')
        return data

    def publish(self,tag,digest):
        if type(tag) is not str or not _KEY.fullmatch(tag):raise SnapshotError('invalid tag')
        self.get(digest)
        head=self.root/'heads'/tag
        previous=head.read_text().strip() if head.exists() and not head.is_symlink() else None
        self._atomic(head,(digest+'\n').encode())
        return {'tag':tag,'previous_sha256':previous,'current_sha256':digest,
                'atomic_visibility_modeled':True,'physical_power_loss_guaranteed':False}

    def resolve(self,tag):
        if type(tag) is not str or not _KEY.fullmatch(tag):raise SnapshotError('invalid tag')
        p=self.root/'heads'/tag
        if p.is_symlink() or not p.is_file():raise SnapshotError('missing or symlink pointer')
        token=p.read_text().strip()
        return {'sha256':token,'data':self.get(token)}
