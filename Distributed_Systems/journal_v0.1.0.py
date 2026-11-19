"""Transactional local SQLite deduplication; NOT exactly-once external actions."""
from pathlib import Path
import sqlite3,hashlib,json

def apply_once(path,key,delta):
    if not isinstance(key,str) or not key or type(delta)!=int:raise ValueError('invalid key/delta')
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(path) as db:
        db.execute('PRAGMA journal_mode=WAL')
        db.execute('PRAGMA synchronous=FULL')
        db.execute('CREATE TABLE IF NOT EXISTS commands(k TEXT PRIMARY KEY, delta INTEGER NOT NULL)')
        db.execute('CREATE TABLE IF NOT EXISTS tally(id INTEGER PRIMARY KEY CHECK(id=1), total INTEGER NOT NULL)')
        db.execute('INSERT OR IGNORE INTO tally(id,total) VALUES (1,0)')
        cur=db.execute('SELECT delta FROM commands WHERE k=?',(key,)).fetchone()
        if cur is not None:
            if cur[0]!=delta:raise ValueError('same idempotency key with different payload')
        else:
            db.execute('INSERT INTO commands VALUES (?,?)',(key,delta))
            db.execute('UPDATE tally SET total=total+? WHERE id=1',(delta,))
        return db.execute('SELECT total FROM tally WHERE id=1').fetchone()[0]

def canonical_event(record):
    return json.dumps(record,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf8')

def extend_chain(prior,event):
    if not isinstance(prior,str) or len(prior)!=64 or any(c not in '0123456789abcdef' for c in prior):raise ValueError('invalid chain head')
    return hashlib.sha256(bytes.fromhex(prior)+canonical_event(event)).hexdigest()

def verify_chain(events,heads,genesis='0'*64):
    if len(events)!=len(heads):return False
    h=genesis
    for e,expected in zip(events,heads):
        h=extend_chain(h,e)
        if h!=expected:return False
    return True
