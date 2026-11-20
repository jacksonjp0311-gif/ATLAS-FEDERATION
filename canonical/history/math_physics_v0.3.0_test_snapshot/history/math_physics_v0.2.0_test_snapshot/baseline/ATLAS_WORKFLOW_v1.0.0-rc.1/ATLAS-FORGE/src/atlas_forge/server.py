"""Loopback-only, read-only HTTP interface. No CORS, writes or upstream execution."""
from __future__ import annotations
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from importlib.resources import files
from urllib.parse import parse_qs, urlsplit
import json
from .federation import Federation

def make_server(federation: Federation | None = None, port: int = 8766, common_root=None) -> ThreadingHTTPServer:
    if type(port) is not int or not 0 <= port <= 65535:raise ValueError('invalid port')
    fed=federation or Federation()
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):pass
        def _send(self, status, data, mime='application/json; charset=utf-8'):
            self.send_response(status)
            self.send_header('Content-Type',mime)
            self.send_header('Content-Length',str(len(data)))
            self.send_header('X-Content-Type-Options','nosniff')
            self.send_header('Cache-Control','no-store')
            self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
            self.end_headers();self.wfile.write(data)
        def _json(self,status,obj):self._send(status,json.dumps(obj,ensure_ascii=False).encode('utf-8'))
        def do_GET(self):
            # Rebinding/cross-site defense: serve only to our explicit loopback origin.
            allowed=f'127.0.0.1:{self.server.server_port}'
            if self.headers.get('Host')!=allowed:
                self._json(403,{'error':'loopback Host required'});return
            origin=self.headers.get('Origin')
            if origin and origin!=f'http://{allowed}':
                self._json(403,{'error':'cross-origin reads not enabled'});return
            u=urlsplit(self.path)
            if len(self.path)>8192:self._json(414,{'error':'request too long'});return
            q=parse_qs(u.query,keep_blank_values=True)
            try:
                if u.path=='/':
                    text=(files('atlas_forge')/'resources'/'common_portal.html').read_text(encoding='utf-8')
                    self._send(200,text.encode(),'text/html; charset=utf-8')
                elif u.path=='/legacy':
                    text=(files('atlas_forge')/'resources'/'portal.html').read_text(encoding='utf-8')
                    self._send(200,text.encode(),'text/html; charset=utf-8')
                elif u.path=='/hero.png':
                    self._send(200,(files('atlas_forge')/'resources'/'hero.png').read_bytes(),'image/png')
                elif u.path in {'/portal.js','/portal.css','/common_portal.js','/common_portal.css'}:
                    p=files('atlas_forge')/'resources'/u.path.lstrip('/')
                    self._send(200,p.read_bytes(),'text/javascript; charset=utf-8' if u.path.endswith('.js') else 'text/css; charset=utf-8')
                elif u.path.startswith('/api/common/'):
                    from .common import AtlasStore
                    store=AtlasStore(common_root)
                    endpoint=u.path.rsplit('/',1)[-1]
                    allowed_params={'nodes':set(),'verify':set(),'search':{'q','node','limit'},'context':{'q','node','limit','max_bytes'},
                                    'fetch':{'id','revision'},'neighbors':{'id','revision','depth','max_edges'}}
                    if endpoint not in allowed_params:self._json(404,{'error':'not found'});return
                    if set(q)-allowed_params[endpoint]:raise ValueError('unknown query parameters')
                    if any(len(v)!=1 for k,v in q.items() if k!='node'):raise ValueError('duplicate scalar query parameters')
                    if endpoint in {'nodes','verify'}:r=store.discover()
                    elif endpoint=='search':r=store.search(q.get('q',[''])[0],node_ids=q.get('node'),limit=int(q.get('limit',['8'])[0]))
                    elif endpoint=='context':r=store.assemble_context(q.get('q',[''])[0],node_ids=q.get('node'),limit=int(q.get('limit',['8'])[0]),max_context_bytes=int(q.get('max_bytes',['32768'])[0]))
                    elif endpoint=='fetch':r=store.fetch(q.get('id',[''])[0],q.get('revision',[''])[0])
                    else:r=store.neighbors(q.get('id',[''])[0],q.get('revision',[''])[0],depth=int(q.get('depth',['1'])[0]),max_edges=int(q.get('max_edges',['30'])[0]))
                    self._json(200,r)
                elif u.path in {'/api/nodes','/api/verify'}:
                    r=fed.discover();self._json(200 if r['valid'] else 503,r)
                elif u.path=='/api/search':
                    include=q.get('include_starters',['false'])[0]
                    if include not in {'true','false'}:raise ValueError('include_starters must be true or false')
                    r=fed.search(q.get('q',[''])[0],node_ids=q.get('node'),include_starters=include=='true',per_node=int(q.get('per_node',['5'])[0]))
                    self._json(200 if not r['errors'] else 503,r)
                else:self._json(404,{'error':'not found'})
            except (ValueError,OSError,TypeError,KeyError) as exc:self._json(400,{'error':str(exc)})
        def do_POST(self):self._json(405,{'error':'read-only service'})
        do_PUT=do_DELETE=do_PATCH=do_POST
    server=ThreadingHTTPServer(('127.0.0.1',port),Handler)
    server.daemon_threads=True
    return server

def serve(federation: Federation, port: int = 8766):
    with make_server(federation,port) as server:
        print(f'ATLAS FORGE: http://127.0.0.1:{server.server_port} (read-only; Ctrl+C to stop)',flush=True)
        try:server.serve_forever()
        except KeyboardInterrupt:pass
