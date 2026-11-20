"""Local SQLite command journal: idempotent *database* effects with replayable hash chain.

This is NOT exactly-once delivery to external devices or other databases. The
reducer must be deterministic, pure, side-effect-free and bounded. SQLite FULL
synchronization follows local OS/storage semantics; physical power-loss tests
and calibrated disks are outside this reference implementation.
"""
from __future__ import annotations
from pathlib import Path
import hashlib,json,re,sqlite3
from .contracts import canonical_bytes,digest,ContractError

_KEY=re.compile(r'^[a-zA-Z0-9_.-]{1,80}$')

class JournalError(ValueError):pass

class CommandJournal:
    def __init__(self,path):
        self.path=Path(path)
        if not self.path.parent.is_dir():raise JournalError('parent directory missing')
        self.db=sqlite3.connect(str(self.path),timeout=5,isolation_level=None)
        self.db.execute('PRAGMA busy_timeout=5000')
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.execute('PRAGMA synchronous=FULL')
        self.db.execute('CREATE TABLE IF NOT EXISTS commands(seq INTEGER PRIMARY KEY, command_id TEXT UNIQUE NOT NULL, payload_sha TEXT NOT NULL, payload_json TEXT NOT NULL, result_json TEXT NOT NULL, prev_sha TEXT NOT NULL, entry_sha TEXT NOT NULL)')
        self.db.execute('CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value TEXT NOT NULL)')
        self.db.execute("INSERT OR IGNORE INTO meta(key,value) VALUES('format_version','1')")
        if self.db.execute("SELECT value FROM meta WHERE key='format_version'").fetchone()[0]!='1':raise JournalError('unsupported schema edition')

    def close(self):self.db.close()
    def __enter__(self):return self
    def __exit__(self,*args):self.close()

    def execute(self,command_id,payload,reducer):
        if type(command_id) is not str or not _KEY.fullmatch(command_id):raise JournalError('invalid bounded command ID')
        if type(payload) is not dict or not callable(reducer):raise JournalError('mapping and pure reducer required')
        raw=canonical_bytes(payload).decode('utf-8');payload_sha=hashlib.sha256(raw.encode()).hexdigest()
        self.db.execute('BEGIN IMMEDIATE')
        try:
            existing=self.db.execute('SELECT payload_sha,result_json,seq,entry_sha FROM commands WHERE command_id=?',(command_id,)).fetchone()
            if existing is not None:
                if existing[0]!=payload_sha:raise JournalError('reused ID has conflicting payload')
                result=json.loads(existing[1]);self.db.execute('COMMIT')
                return {'result':result,'new_commit':False,'sequence':existing[2],'entry_sha256':existing[3]}
            last=self.db.execute('SELECT seq,entry_sha FROM commands ORDER BY seq DESC LIMIT 1').fetchone()
            seq=last[0]+1 if last else 1;prev=last[1] if last else '0'*64
            # ONLY deterministic pure reducers. External side effects cannot be
            # rolled back by this local DB transaction and may be duplicated.
            result=reducer(json.loads(raw))
            result_json=canonical_bytes(result).decode('utf-8')
            entry={'seq':seq,'command_id':command_id,'payload_sha':payload_sha,
                   'payload_json':raw,'result_json':result_json,'prev_sha':prev}
            eh=digest(entry)
            self.db.execute('INSERT INTO commands(seq,command_id,payload_sha,payload_json,result_json,prev_sha,entry_sha) VALUES(?,?,?,?,?,?,?)',(seq,command_id,payload_sha,raw,result_json,prev,eh))
            self.db.execute('COMMIT')
            return {'result':result,'new_commit':True,'sequence':seq,'entry_sha256':eh}
        except Exception:
            self.db.execute('ROLLBACK')
            raise

    def verify_replay(self):
        rows=self.db.execute('SELECT seq,command_id,payload_sha,payload_json,result_json,prev_sha,entry_sha FROM commands ORDER BY seq').fetchall()
        prev='0'*64
        for index,row in enumerate(rows,1):
            seq,cmd,ps,pjson,rjson,recorded_prev,eh=row
            if seq!=index or recorded_prev!=prev:raise JournalError('gap, reorder, or prev-chain mismatch')
            try:payload=json.loads(pjson);result=json.loads(rjson)
            except ValueError as exc:raise JournalError('corrupted JSON row') from exc
            if hashlib.sha256(canonical_bytes(payload)).hexdigest()!=ps:
                raise JournalError('payload has been modified')
            if canonical_bytes(payload).decode()!=pjson or canonical_bytes(result).decode()!=rjson:
                raise JournalError('noncanonical or altered result')
            entry={'seq':seq,'command_id':cmd,'payload_sha':ps,'payload_json':pjson,'result_json':rjson,'prev_sha':prev}
            if digest(entry)!=eh:raise JournalError('hash chain corrupted')
            prev=eh
        return {'schema':'atlas.pattern-command-journal/1','rows':len(rows),
                'head_sha256':prev,'valid':True,
                'external_exactly_once_delivery_proven':False,'power_loss_hardware_characterized':False}

    def records(self):
        return tuple({'command_id':row[0],'result':json.loads(row[1]),'sequence':row[2]}
                     for row in self.db.execute('SELECT command_id,result_json,seq FROM commands ORDER BY seq'))
