"""SQLite single-acceptor stable-state teaching model (NOT power cut verified).

A local BEGIN IMMEDIATE transaction persists a promise and an accepted proposal.
Paxos safety depends on a faithful stable-storage implementation; SQLite's
settings are configuration assertions, not measurements of physical durability.
"""
from pathlib import Path
from contextlib import closing
import sqlite3

def _connect(path):
    conn = sqlite3.connect(str(Path(path)), timeout=5, isolation_level=None)
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA synchronous=FULL')
    conn.execute('CREATE TABLE IF NOT EXISTS acceptor (id INTEGER PRIMARY KEY CHECK(id=1), promised INTEGER NOT NULL, accepted_n INTEGER NOT NULL, accepted_value TEXT)')
    conn.execute('INSERT OR IGNORE INTO acceptor VALUES (1,-1,-1,NULL)')
    return conn

class DurableAcceptor:
    def __init__(self, path): self.path = Path(path)
    def read(self):
        with closing(_connect(self.path)) as c:
            return c.execute('SELECT promised,accepted_n,accepted_value FROM acceptor WHERE id=1').fetchone()
    def _transition(self, ballot, value, kind):
        if type(ballot) is not int or ballot < 0 or (kind == 'accept' and not isinstance(value, str)):
            raise ValueError('ballot must be nonnegative integer; value must be text')
        c = _connect(self.path)
        try:
            c.execute('BEGIN IMMEDIATE')
            p, n, v = c.execute('SELECT promised,accepted_n,accepted_value FROM acceptor WHERE id=1').fetchone()
            if kind == 'promise':
                outcome = (n, v) if ballot > p else None
                if outcome is not None:
                    c.execute('UPDATE acceptor SET promised=? WHERE id=1', (ballot,))
            elif kind == 'accept':
                if ballot == n and v != value:
                    raise ValueError('ballot reuse with a conflicting value')
                outcome = ballot >= p
                if outcome:
                    c.execute('UPDATE acceptor SET promised=?,accepted_n=?,accepted_value=? WHERE id=1', (ballot, ballot, value))
            else: raise ValueError('unknown transition')
            c.execute('COMMIT')
            return outcome
        except BaseException:
            if c.in_transaction: c.execute('ROLLBACK')
            raise
        finally:
            c.close()
    def promise(self, ballot):return self._transition(ballot, None, 'promise')
    def accept(self, ballot, value):return self._transition(ballot, value, 'accept')
